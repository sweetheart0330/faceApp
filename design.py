# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Docs\Desktop\final_need_to_beautify.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1240, 700)
        MainWindow.setStyleSheet("QWidget{\n"
                                 "background-color:#D0EEFF;\n"
                                 "background-size:contain;\n"
                                 "}")
        QtGui.QFontDatabase.addApplicationFont(
            "C:/Users/Kate/PycharmProjects/pythonProject7/faceApp/fonts/Judson-Italic.ttf")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(180, 190, 320, 240))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img.sizePolicy().hasHeightForWidth())
        self.img.setSizePolicy(sizePolicy)
        self.img.setStyleSheet("QLabel{\n"
                               "background-color: white;\n"
                               "border-radius: 11px;\n"
                               "border: solid;\n"
                               "}\n"
                               "")
        self.img.setText("")
        self.img.setScaledContents(False)
        self.img.setObjectName("img")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(500, 70, 321, 41))
        self.comboBox.setStyleSheet("QComboBox{\n"
                                    "border:solid;\n"
                                    "background-color: rgba(255, 174, 223, 0.7);\n"
                                    "border-radius:11px\n"
                                    "}")
        self.comboBox.setObjectName("comboBox")
        self.importFile = QtWidgets.QPushButton(self.centralwidget)
        self.importFile.setGeometry(QtCore.QRect(330, 70, 131, 41))
        self.importFile.setStyleSheet("QPushButton{\n"
                                      "border:solid;\n"
                                      "background-color:  #FFAEDF;\n"
                                      "border-radius:11px;\n"
                                      "color: #3B1A70;\n"
                                      "font-family: \'Judson\';\n"
                                      "font-style: italic;\n"
                                      "font-weight: 400;\n"
                                      "font-size: 12px;\n"
                                      "}\n"
                                      "QPushButton:hover:!pressed{\n"
                                      "background-color:#C19BFF;\n"
                                      "}\n"
                                      "")
        self.importFile.setObjectName("importFile")
        self.makeUp = QtWidgets.QWidget(self.centralwidget)
        self.makeUp.setGeometry(QtCore.QRect(230, 450, 761, 211))
        self.makeUp.setObjectName("makeUp")
        self.pickEyesColor = QtWidgets.QPushButton(self.makeUp)
        self.pickEyesColor.setGeometry(QtCore.QRect(110, 130, 151, 31))
        self.pickEyesColor.setStyleSheet("/* Group 4 */\n"
                                         "\n"

                                         "background: #C19BFF;\n"
                                         "border-radius: 11px;\n"

                                         "position: absolute;\n"
                                         "width: 48px;\n"
                                         "height: 17px;\n"
                                         "left: 458px;\n"
                                         "top: 614px;\n"
                                         "\n"
                                         "font-family: \'Judson\';\n"
                                         "font-style: italic;\n"
                                         "font-weight: 400;\n"
                                         "font-size: 16px;\n"
                                         "line-height: 108.33%;\n"
                                         "/* or 17px */\n"
                                         "\n"
                                         "color: #FFFFFF;\n"
                                         "\n"
                                         "")
        self.pickEyesColor.setObjectName("pickEyesColor")
        self.pickLipsColor = QtWidgets.QPushButton(self.makeUp)
        self.pickLipsColor.setGeometry(QtCore.QRect(370, 130, 151, 31))
        self.pickLipsColor.setStyleSheet("/* Group 4 */\n"
                                         "\n"
                                         "position: absolute;\n"
                                         "width: 23px;\n"
                                         "height: 128px;\n"
                                         "left: 546px;\n"
                                         "top: 612px;\n"
                                         "\n"
                                         "transform: rotate(90deg);\n"
                                         "\n"
                                         "\n"
                                         "/* Rectangle 11 */\n"
                                         "\n"
                                         "position: absolute;\n"
                                         "width: 128px;\n"
                                         "height: 23px;\n"
                                         "left: 418px;\n"
                                         "top: 612px;\n"
                                         "\n"
                                         "background: #C19BFF;\n"
                                         "border-radius: 11px;\n"
                                         "\n"
                                         "\n"
                                         "/* choose */\n"
                                         "\n"
                                         "position: absolute;\n"
                                         "width: 48px;\n"
                                         "height: 17px;\n"
                                         "left: 458px;\n"
                                         "top: 614px;\n"
                                         "\n"
                                         "font-family: \'Judson\';\n"
                                         "font-style: italic;\n"
                                         "font-weight: 400;\n"
                                         "font-size: 16px;\n"
                                         "line-height: 108.33%;\n"
                                         "/* or 17px */\n"
                                         "\n"
                                         "color: #FFFFFF;\n"
                                         "\n"
                                         "")
        self.pickLipsColor.setObjectName("pickLipsColor")
        self.eyesColorShower = QtWidgets.QLabel(self.makeUp)
        self.eyesColorShower.setGeometry(QtCore.QRect(270, 40, 41, 41))
        self.eyesColorShower.setStyleSheet("QLabel{\n"
                                           "background-color: white;\n"
                                           "border: solid;\n"
                                           "border-radius:11px;\n"
                                           "}border-top-left-radius: 50px;")
        self.eyesColorShower.setText("")
        self.eyesColorShower.setObjectName("eyesColorShower")
        self.lipsColorShower = QtWidgets.QLabel(self.makeUp)
        self.lipsColorShower.setGeometry(QtCore.QRect(520, 40, 41, 41))
        self.lipsColorShower.setStyleSheet("QLabel{\n"
                                           "background-color: white;\n"
                                           "border: solid;\n"
                                           "border-radius:11px;\n"
                                           "}")
        self.lipsColorShower.setText("")
        self.lipsColorShower.setObjectName("lipsColorShower")
        self.eyesCheck = QtWidgets.QPushButton(self.makeUp)
        self.eyesCheck.setGeometry(QtCore.QRect(130, 30, 111, 51))
        self.eyesCheck.setStyleSheet("QPushButton{\n"
                                     "border:solid;\n"
                                     "background-color:  #FFAEDF;\n"
                                     "border-radius:11px;\n"
                                     "color: #3B1A70;\n"
                                     "border-image : url(icons/Group 1.png);"
                                     "}\n"
                                     "QPushButton:hover:!pressed{\n"
                                     "border-color:#C19BFF;\n"
                                     "border: 1px solid;\n"
                                     "border-image:url(icons/Group 1 (1).png);\n"
                                     "}\n"
                                     "\n"
                                     "")
        self.eyesCheck.setText("")
        self.eyesCheck.setCheckable(True)
        self.eyesCheck.setChecked(False)
        self.eyesCheck.setObjectName("eyesCheck")
        self.lipsCheck = QtWidgets.QPushButton(self.makeUp)
        self.lipsCheck.setGeometry(QtCore.QRect(380, 30, 111, 51))
        self.lipsCheck.setStyleSheet(
            "QPushButton{\n"
            "border:solid;\n"
            "background-color:  #FFAEDF;\n"
            "border-image : url(icons/Group 2.png);"
            "border-radius:11px;\n"
            "color: #3B1A70;\n"
            "}\n"
            "QPushButton:hover:!pressed{\n"
            "border-color:#C19BFF;\n"
            "border: solid;\n"
            "border-image:url(icons/Group 2 (1).png);\n"
            "}\n"
            "\n"
            "\n"
            "")
        self.lipsCheck.setText("")
        self.lipsCheck.setCheckable(True)
        self.lipsCheck.setObjectName("lipsCheck")
        self.label_5 = QtWidgets.QLabel(self.makeUp)
        self.label_5.setGeometry(QtCore.QRect(130, 90, 141, 21))
        self.label_5.setStyleSheet("/* change eye color */\n"
                                   "\n"
                                   "position: absolute;\n"
                                   "width: 115px;\n"
                                   "height: 17px;\n"
                                   "left: 418px;\n"
                                   "top: 581px;\n"
                                   "\n"
                                   "font-family: \'Judson\';\n"
                                   "font-style: italic;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px;\n"
                                   "line-height: 108.33%;\n"
                                   "/* or 17px */\n"
                                   "\n"
                                   "color: #3B1A70;\n"
                                   "\n"
                                   "")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.makeUp)
        self.label_6.setGeometry(QtCore.QRect(380, 90, 121, 21))
        self.label_6.setStyleSheet("/* change eye color */\n"
                                   "\n"
                                   "position: absolute;\n"
                                   "width: 115px;\n"
                                   "height: 17px;\n"
                                   "left: 418px;\n"
                                   "top: 581px;\n"
                                   "\n"
                                   "font-family: \'Judson\';\n"
                                   "font-style: italic;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px;\n"
                                   "line-height: 108.33%;\n"
                                   "/* or 17px */\n"
                                   "\n"
                                   "color: #3B1A70;\n"
                                   "\n"
                                   "")
        self.label_6.setObjectName("label_6")
        self.imgPostProcess = QtWidgets.QLabel(self.centralwidget)
        self.imgPostProcess.setGeometry(QtCore.QRect(610, 190, 320, 240))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgPostProcess.sizePolicy().hasHeightForWidth())
        self.imgPostProcess.setSizePolicy(sizePolicy)
        self.imgPostProcess.setStyleSheet("QLabel{\n"
                                          "background-color: white;\n"
                                          "border-radius: 11px;\n"
                                          "border: solid;\n"
                                          "}\n"
                                          "")
        self.imgPostProcess.setText("")
        self.imgPostProcess.setScaledContents(False)
        self.imgPostProcess.setObjectName("imgPostProcess")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 160, 47, 13))
        self.label.setStyleSheet("/* before */\n"
                                 "\n"
                                 "position: absolute;\n"
                                 "width: 41px;\n"
                                 "height: 16px;\n"
                                 "left: 392px;\n"
                                 "top: 158px;\n"
                                 "\n"
                                 "font-family: \'Judson\';\n"
                                 "font-style: italic;\n"
                                 "font-weight: 400;\n"
                                 "font-size: 15px;\n"
                                 "line-height: 108.33%;\n"
                                 "/* or 16px */\n"
                                 "\n"
                                 "color: #3B1A70;\n"
                                 "\n"
                                 "")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(740, 160, 47, 13))
        self.label_2.setStyleSheet("/* before */\n"
                                   "\n"
                                   "position: absolute;\n"
                                   "width: 41px;\n"
                                   "height: 16px;\n"
                                   "left: 392px;\n"
                                   "top: 158px;\n"
                                   "\n"
                                   "font-family: \'Judson\';\n"
                                   "font-style: italic;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 15px;\n"
                                   "line-height: 108.33%;\n"
                                   "/* or 16px */\n"
                                   "\n"
                                   "color: #3B1A70;\n"
                                   "\n"
                                   "")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(530, 300, 51, 31))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("icons/Group 10.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(610, 80, 71, 21))
        self.label_4.setStyleSheet("QLabel{\n"
                                   "color:#3B1A70;\n"
                                   "background-color: rgba(255, 174, 223, 0.3);\n"
                                   "font-family: \'Judson\';\n"
                                   "font-style: italic;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 12px;\n"
                                   "}")
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(950, 250, 131, 131))
        self.frame.setStyleSheet("padding: 5px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.buttonProcess = QtWidgets.QPushButton(self.frame)
        self.buttonProcess.setGeometry(QtCore.QRect(20, 20, 101, 31))
        self.buttonProcess.setStyleSheet("QPushButton{\n"
                                         "border:solid;\n"
                                         "background-color:  #FFAEDF;\n"
                                         "border-radius:11px;\n"
                                         "font-family: \'Judson\';\n"
                                         "font-style: italic;\n"
                                         "font-weight: 400;\n"
                                         "font-size: 12px;\n"
                                         "color: #3B1A70;\n"
                                         "}\n"

                                         "QPushButton:hover:!pressed{\n"
                                         "background-color:#C19BFF;\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "")
        self.buttonProcess.setObjectName("buttonProcess")
        self.buttonSave = QtWidgets.QPushButton(self.frame)
        self.buttonSave.setGeometry(QtCore.QRect(20, 70, 101, 31))
        self.buttonSave.setStyleSheet("QPushButton{\n"
                                      "border:solid;\n"
                                      "background-color:  #FFAEDF;\n"
                                      "border-radius:11px;\n"
                                      "font-family: \'Judson\';\n"
                                      "font-style: italic;\n"
                                      "font-weight: 400;\n"
                                      "font-size: 12px;\n"
                                      "color: #3B1A70;\n"
                                      "}\n"
                                      "QPushButton:hover:!pressed{\n"
                                      "background-color:#C19BFF;\n"
                                      "}\n"
                                      "")
        self.buttonSave.setObjectName("buttonSave")
        self.comboBox.raise_()
        self.img.raise_()
        self.importFile.raise_()
        self.makeUp.raise_()
        self.imgPostProcess.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.frame.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.importFile.setText(_translate("MainWindow", "download a file"))
        self.pickEyesColor.setText(_translate("MainWindow", "choose"))
        self.pickLipsColor.setText(_translate("MainWindow", "choose"))
        self.label_5.setText(_translate("MainWindow", "change eye color"))
        self.label_6.setText(_translate("MainWindow", "change lip color"))
        self.label.setText(_translate("MainWindow", "before"))
        self.label_2.setText(_translate("MainWindow", "after"))
        self.label_4.setText(_translate("MainWindow", "select a filter"))
        self.buttonProcess.setText(_translate("MainWindow", "prossess"))
        self.buttonSave.setText(_translate("MainWindow", "save"))


# import icons_rc


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
