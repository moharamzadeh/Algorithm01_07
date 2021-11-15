# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from delPage import *
from addPage2 import *
from searchPage import *
import sys


class Ui_mainPage(object):
    def setupUi(self, mainPage, a, y, mo, d, h, mn, ev):
        self.address = a
        self.year = y
        self.month = mo
        self.day = d
        self.hour = h
        self.minute = mn
        self.ev = ev
        mainPage.setObjectName("mainPage")
        mainPage.resize(750, 600)
        mainPage.setStyleSheet("background-color: rgb(238, 214, 196);")
        self.picturePlace = QtWidgets.QLabel(mainPage)
        self.picturePlace.setGeometry(QtCore.QRect(140, 20, 471, 421))
        self.picturePlace.setText("")
        self.picturePlace.setObjectName("picturePlace")
        self.timeLabel = QtWidgets.QLabel(mainPage)
        self.timeLabel.setGeometry(QtCore.QRect(150, 460, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.timeLabel.setFont(font)
        self.timeLabel.setText("")
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.checkLabel = QtWidgets.QLabel(mainPage)
        self.checkLabel.setGeometry(QtCore.QRect(400, 460, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.checkLabel.setFont(font)
        self.checkLabel.setText("")
        self.checkLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.checkLabel.setObjectName("checkLabel")
        self.preButton = QtWidgets.QPushButton(mainPage)
        self.preButton.setGeometry(QtCore.QRect(10, 230, 111, 51))
        self.preButton.setStyleSheet("background-color: rgb(72, 52, 52);\n"
"color: rgb(255, 243, 228);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/623176_arrow_bold_dual_left_back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.preButton.setIcon(icon)
        self.preButton.setIconSize(QtCore.QSize(40, 40))
        self.preButton.setObjectName("preButton")
        self.nextButton = QtWidgets.QPushButton(mainPage)
        self.nextButton.setGeometry(QtCore.QRect(630, 230, 111, 51))
        self.nextButton.setStyleSheet("background-color: rgb(72, 52, 52);\n"
"color: rgb(255, 243, 228);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/623175_arrow_bold_dual_right_direction_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon1)
        self.nextButton.setIconSize(QtCore.QSize(40, 40))
        self.nextButton.setObjectName("nextButton")
        self.searchButton = QtWidgets.QPushButton(mainPage)
        self.searchButton.setGeometry(QtCore.QRect(150, 520, 111, 51))
        self.searchButton.setStyleSheet("background-color: rgb(72, 52, 52);\n"
"color: rgb(255, 243, 228);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/103797_viewer_image_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchButton.setIcon(icon2)
        self.searchButton.setIconSize(QtCore.QSize(40, 40))
        self.searchButton.setObjectName("searchButton")
        self.delButton = QtWidgets.QPushButton(mainPage)
        self.delButton.setGeometry(QtCore.QRect(330, 520, 111, 51))
        self.delButton.setStyleSheet("background-color: rgb(72, 52, 52);\n"
"color: rgb(255, 243, 228);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/103476_cancel_image_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delButton.setIcon(icon3)
        self.delButton.setIconSize(QtCore.QSize(30, 30))
        self.delButton.setObjectName("delButton")
        self.addButton = QtWidgets.QPushButton(mainPage)
        self.addButton.setGeometry(QtCore.QRect(510, 520, 111, 51))
        self.addButton.setStyleSheet("background-color: rgb(72, 52, 52);\n"
"color: rgb(255, 243, 228);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/add01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon4)
        self.addButton.setIconSize(QtCore.QSize(35, 35))
        self.addButton.setObjectName("addButton")

        self.retranslateUi(mainPage)
        QtCore.QMetaObject.connectSlotsByName(mainPage)
        self.timeLabel.setText(f"{self.day} {self.month} {self.year} {self.hour}:{self.minute}")
        self.checkLabel.setText(str(self.ev))
        pixmap = QtGui.QPixmap(str(self.address))
        self.picturePlace.setPixmap(pixmap)


        self.addButton.clicked.connect(self.openAdd)
        self.delButton.clicked.connect(self.openDel)
        self.searchButton.clicked.connect(self.openSearch)


    def retranslateUi(self, mainPage):
        _translate = QtCore.QCoreApplication.translate
        mainPage.setWindowTitle(_translate("mainPage", "Main Page"))
        self.preButton.setText(_translate("mainPage", "Previous"))
        self.nextButton.setText(_translate("mainPage", "Next"))
        self.searchButton.setText(_translate("mainPage", "Search"))
        self.delButton.setText(_translate("mainPage", "Delete"))
        self.addButton.setText(_translate("mainPage", "Add"))

    def openAdd(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_addPage2()
        self.ui.setupUi(self.window)
        self.window.show()

    def openDel(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_delPage()
        self.ui.setupUi(self.window)
        self.window.show()

    def openSearch(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_searchPage()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainPage = QtWidgets.QWidget()
    ui = Ui_mainPage()
    ui.setupUi(mainPage, 'None', 'None', 'None', 'None', 'None', 'None', 'None')
    mainPage.show()
    sys.exit(app.exec_())