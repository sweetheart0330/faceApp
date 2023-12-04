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
        self.initui()

    def initui(self):
        self.ui.img.setAlignment(Qt.AlignCenter)
        self.ui.comboBox.addItems(['Цензура', 'Blush', 'Дьявол', 'Собака', 'Очки', 'Шляпа', 'Шляпа и очки', 'Сердце', 'Мейкап', 'Moustache'])
        self.ui.comboBox.activated[int].connect(self.checked)
        self.ui.importFile.clicked.connect(self.click)

    def click(self):
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

    def checked(self, item):
        if item == 8:
            pass


app = QtWidgets.QApplication(sys.argv)
window = MyWin()
window.show()
app.exec_()
