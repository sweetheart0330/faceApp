import sys
import time
from PIL import Image
from PIL import ImageDraw
from design import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
from PyQt5.QtCore import Qt

from Black_Rect_Filter import brect_filter
from Blush_Filter import blush_filter
from Devil_Filter import devil_filter
from Dog_Filter import dog_filter
from Glasses_Filter import glasses_filter
from Hat_Filter import hat_filter
from Hat_And_Glasses_Filter import hat_glas_filter
from Hearts_Filter import hearts_filter
from Make_Up import make_up_filter
from Moustache_Filter import moust_filter


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.eyesColor = None
        self.path = None
        self.imgPostProcess = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.eyeColor = None
        self.lipsColor = None
        self.picked_filter = None

    def init_ui(self):
        self.ui.img.setAlignment(Qt.AlignCenter)
        self.ui.eyesColorShower.setAlignment(Qt.AlignCenter)
        self.ui.lipsColorShower.setAlignment(Qt.AlignCenter)
        self.ui.comboBox.addItems(['', 'Цензура', 'Румянец', 'Дьявол', 'Собака', 'Очки', 'Шляпа', 'Шляпа и очки', 'Сердце', 'Мейкап', 'Moustache'])
        self.ui.comboBox.activated[int].connect(self.checked)
        self.ui.importFile.clicked.connect(self.choice_file)
        self.ui.pickEyesColor.clicked.connect(self.eyes_color_click)
        self.ui.pickLipsColor.clicked.connect(self.lips_color_click)
        self.ui.buttonProcess.clicked.connect(self.process)
        self.ui.buttonSave.clicked.connect(self.saveProcess)
        self.ui.makeUp.setVisible(False)

    def saveProcess(self):
        im = Image.fromarray(self.imgPostProcess)
        b, g, r = im.split()
        im = Image.merge("RGB", (r, g, b))
        im2 = im.convert("RGBA")
        path = QtWidgets.QFileDialog.getSaveFileName(initialFilter="Images (*.png *.jpg *.jpeg)", filter="Images (*.png *.jpg *.jpeg)")[0]
        im2.save(path)

    def process(self):
        if self.picked_filter is None:
            self.ui.imgPostProcess.setPixmap(QPixmap())
        elif self.picked_filter == make_up_filter:
            if self.ui.lipsCheck.isChecked():
                lipsColorRgb = [self.lipsColor.blue(), self.lipsColor.green(), self.lipsColor.red()]
            else:
                lipsColorRgb = [0, 0, 0]
            if self.ui.eyesCheck.isChecked():
                eyesColorRgb = [self.eyesColor.blue(), self.eyesColor.green(), self.eyesColor.red()]
            else:
                eyesColorRgb = [0, 0, 0]
            self.imgPostProcess = self.picked_filter(self.ui.lipsCheck.isChecked(), self.ui.eyesCheck.isChecked(),
                               self.ui.chbCheck.isChecked(), lipsColorRgb, eyesColorRgb, self.path)
        else:
            self.imgPostProcess = self.picked_filter(self.path)
        pixmap = self.pil2pixmap(self.imgPostProcess)
        h = self.ui.imgPostProcess.height()
        w = self.ui.imgPostProcess.width()
        if pixmap.height() > pixmap.width():
            pixmap = pixmap.scaledToHeight(h)
        else:
            pixmap = pixmap.scaledToWidth(w)
        self.ui.imgPostProcess.setPixmap(pixmap)

    def pil2pixmap(self, image):
        '''if im.mode == "RGB":
            r, g, b = im.split()
            im = Image.merge("RGB", (b, g, r))
        elif im.mode == "RGBA":
            r, g, b, a = im.split()
            im = Image.merge("RGBA", (b, g, r, a))
        elif im.mode == "L":
            im = im.convert("RGBA")'''
        if not (type(image) is Image.Image):
            im = Image.fromarray(image)
        else:
            im = image
        im2 = im.convert("RGBA")
        data = im2.tobytes("raw", "RGBA")
        qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_ARGB32)
        pixmap = QtGui.QPixmap.fromImage(qim)
        return pixmap

    def choice_file(self):
        self.path = QtWidgets.QFileDialog.getOpenFileName(filter="Images (*.png *.jpg *.jpeg)")[0]
        pixmap = QPixmap(self.path)
        '''test = hat_filter(self.path)
        image = Image.fromarray(test)
        pixmap = self.pil2pixmap(image)'''
        h = self.ui.img.height()
        w = self.ui.img.width()
        if pixmap.height() > pixmap.width():
            pixmap = pixmap.scaledToHeight(h)
        else:
            pixmap = pixmap.scaledToWidth(w)
        #self.ui.img.setPixmap(pixmap)
        self.ui.img.setPixmap(pixmap)

    def eyes_color_click(self):
        color = QtWidgets.QColorDialog.getColor()
        self.eyesColor = color
        image = Image.new("RGB", (self.ui.eyesColorShower.width()-3, self.ui.eyesColorShower.height()-3),
                          (200, 200, 200))
        ImageDraw.Draw(image).rectangle(((0, 0), image.size),
                                        fill=(self.eyesColor.blue(), self.eyesColor.green(), self.eyesColor.red()))
        pixmap = self.pil2pixmap(image)
        self.ui.eyesColorShower.setPixmap(pixmap)

    def lips_color_click(self):
        color = QtWidgets.QColorDialog.getColor()
        self.lipsColor = color
        image = Image.new("RGB", (self.ui.lipsColorShower.width() - 3, self.ui.lipsColorShower.height() - 3),
                          (200, 200, 200))
        ImageDraw.Draw(image).rectangle(((0, 0), image.size),
                                        fill=(self.lipsColor.blue(), self.lipsColor.green(), self.lipsColor.red()))
        pixmap = self.pil2pixmap(image)
        self.ui.lipsColorShower.setPixmap(pixmap)

    def checked(self, item):
        self.ui.makeUp.setVisible(False)
        if item == 0:
            self.picked_filter = None
        if item == 1:
            self.picked_filter = brect_filter
        elif item == 2:
            self.picked_filter = blush_filter
        elif item == 3:
            self.picked_filter = devil_filter
        elif item == 4:
            self.picked_filter = dog_filter
        elif item == 5:
            self.picked_filter = glasses_filter
        elif item == 6:
            self.picked_filter = hat_filter
        elif item == 7:
            self.picked_filter = hat_glas_filter
        elif item == 8:
            self.picked_filter = hearts_filter
        elif item == 9:
            self.picked_filter = make_up_filter
            self.ui.makeUp.setVisible(True)
        elif item == 10:
            self.picked_filter = moust_filter


app = QtWidgets.QApplication(sys.argv)
window = MyWin()
window.show()
app.exec_()
