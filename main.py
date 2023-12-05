import sys
import time
from PIL import Image
from design import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
from PyQt5.QtCore import Qt


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.eyeColor = None
        self.lipsColor = None

    def init_ui(self):
        self.ui.img.setAlignment(Qt.AlignCenter)
        self.ui.comboBox.addItems(['', 'Цензура', 'Blush', 'Дьявол', 'Собака', 'Очки', 'Шляпа', 'Шляпа и очки', 'Сердце', 'Мейкап', 'Moustache'])
        self.ui.comboBox.activated[int].connect(self.checked)
        self.ui.importFile.clicked.connect(self.choice_file)
        self.ui.pickEyesColor.clicked.connect(self.eyes_color_click)
        self.ui.pickLipsColor.clicked.connect(self.lips_color_click)

    def choice_file(self):
        path = QtWidgets.QFileDialog.getOpenFileName()[0]
        im = Image.open(path)
        im = im.convert("RGBA")
        data = im.tobytes("raw", "RGBA")
        qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_ARGB32)
        pixmap = QtGui.QPixmap.fromImage(qim)
        #pixmap = QPixmap(path)
        h = self.ui.img.height()
        w = self.ui.img.width()
        if pixmap.height() > pixmap.width():
            pixmap = pixmap.scaledToHeight(h)
        else:
            pixmap = pixmap.scaledToWidth(w)
        self.ui.img.setPixmap(pixmap)
        color = QtWidgets.QColorDialog.getColor()
        print(color.red(), color.green(), color.blue(), color.alpha())

    def eyes_color_click(self):
        color = QtWidgets.QColorDialog.getColor()
        self.eyeColor = color
        print('-', self.eyeColor.red(), self.eyeColor.green(), self.eyeColor.blue(), self.eyeColor.alpha())

    def lips_color_click(self):
        color = QtWidgets.QColorDialog.getColor()
        self.lipsColor = color
        print('+', self.lipsColor.red(), self.lipsColor.green(), self.lipsColor.blue(), self.lipsColor.alpha())

    def checked(self, item):
        if item == 1:
            pass
        elif item == 2:
            pass
        elif item == 3:
            pass
        elif item == 4:
            pass
        elif item == 5:
            pass
        elif item == 6:
            pass
        elif item == 7:
            pass
        elif item == 8:
            pass
        elif item == 9:
            print('make')


app = QtWidgets.QApplication(sys.argv)
window = MyWin()
window.show()
app.exec_()
