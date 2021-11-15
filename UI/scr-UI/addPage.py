# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from MainPage import *


class Ui_addPage(object):
    def setupUi(self, addPage):
        addPage.setObjectName("addPage")
        addPage.resize(870, 342)
        addPage.setStyleSheet("background-color: rgb(50, 31, 40);")
        self.hourTxt = QtWidgets.QLineEdit(addPage)
        self.hourTxt.setGeometry(QtCore.QRect(525, 114, 114, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.hourTxt.setFont(font)
        self.hourTxt.setStyleSheet("color: rgb(231, 158, 79);")
        self.hourTxt.setObjectName("hourTxt")
        self.label_6 = QtWidgets.QLabel(addPage)
        self.label_6.setGeometry(QtCore.QRect(645, 118, 38, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(addPage)
        self.label_2.setGeometry(QtCore.QRect(9, 114, 48, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
        self.label_2.setObjectName("label_2")
        self.yearTxt = QtWidgets.QLineEdit(addPage)
        self.yearTxt.setGeometry(QtCore.QRect(135, 114, 74, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.yearTxt.setFont(font)
        self.yearTxt.setStyleSheet("color: rgb(231, 158, 79);")
        self.yearTxt.setObjectName("yearTxt")
        self.comboBox = QtWidgets.QComboBox(addPage)
        self.comboBox.setGeometry(QtCore.QRect(215, 115, 123, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.dayTxt = QtWidgets.QLineEdit(addPage)
        self.dayTxt.setGeometry(QtCore.QRect(371, 114, 115, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dayTxt.setFont(font)
        self.dayTxt.setStyleSheet("color: rgb(231, 158, 79);")
        self.dayTxt.setObjectName("dayTxt")
        self.label_5 = QtWidgets.QLabel(addPage)
        self.label_5.setGeometry(QtCore.QRect(492, 118, 27, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.minTxt = QtWidgets.QLineEdit(addPage)
        self.minTxt.setGeometry(QtCore.QRect(689, 114, 115, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.minTxt.setFont(font)
        self.minTxt.setStyleSheet("color: rgb(231, 158, 79);")
        self.minTxt.setObjectName("minTxt")
        self.label_9 = QtWidgets.QLabel(addPage)
        self.label_9.setGeometry(QtCore.QRect(344, 118, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(addPage)
        self.label.setGeometry(QtCore.QRect(9, 44, 73, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(addPage)
        self.label_3.setGeometry(QtCore.QRect(9, 184, 82, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(addPage)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(103, 118, 26, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
        self.label_4.setObjectName("label_4")
        self.address = QtWidgets.QLineEdit(addPage)
        self.address.setGeometry(QtCore.QRect(135, 44, 671, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.address.setFont(font)
        self.address.setStyleSheet("color: rgb(231, 158, 79);")
        self.address.setObjectName("address")
        self.radioButton = QtWidgets.QRadioButton(addPage)
        self.radioButton.setGeometry(QtCore.QRect(215, 184, 52, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
        self.radioButton.setObjectName("radioButton")
        self.noRadio = QtWidgets.QRadioButton(addPage)
        self.noRadio.setGeometry(QtCore.QRect(280, 184, 46, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.noRadio.setFont(font)
        self.noRadio.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
        self.noRadio.setObjectName("noRadio")
        self.label_8 = QtWidgets.QLabel(addPage)
        self.label_8.setGeometry(QtCore.QRect(10, 220, 691, 81))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 243, 228);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(addPage)
        self.pushButton.setGeometry(QtCore.QRect(710, 240, 151, 43))
        self.pushButton.setStyleSheet("color: rgb(50, 31, 40);\n"
"background-color: #E79E4F;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/add01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(28, 35))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.goToMainPage)


        self.retranslateUi(addPage)
        QtCore.QMetaObject.connectSlotsByName(addPage)



    def retranslateUi(self, addPage):
        _translate = QtCore.QCoreApplication.translate
        addPage.setWindowTitle(_translate("addPage", "Adding Page"))
        self.label_6.setText(_translate("addPage", "Minute"))
        self.label_2.setText(_translate("addPage", "Time:"))
        self.comboBox.setItemText(0, _translate("addPage", "January"))
        self.comboBox.setItemText(1, _translate("addPage", "February"))
        self.comboBox.setItemText(2, _translate("addPage", "March"))
        self.comboBox.setItemText(3, _translate("addPage", "April"))
        self.comboBox.setItemText(4, _translate("addPage", "May"))
        self.comboBox.setItemText(5, _translate("addPage", "June"))
        self.comboBox.setItemText(6, _translate("addPage", "July"))
        self.comboBox.setItemText(7, _translate("addPage", "August"))
        self.comboBox.setItemText(8, _translate("addPage", "September"))
        self.comboBox.setItemText(9, _translate("addPage", "October"))
        self.comboBox.setItemText(10, _translate("addPage", "November"))
        self.comboBox.setItemText(11, _translate("addPage", "December"))
        self.label_5.setText(_translate("addPage", "Hour"))
        self.label_9.setText(_translate("addPage", "Day"))
        self.label.setText(_translate("addPage", "Address:"))
        self.label_3.setText(_translate("addPage", "Evidence:"))
        self.label_4.setText(_translate("addPage", "Year"))
        self.radioButton.setText(_translate("addPage", "Yes"))
        self.noRadio.setText(_translate("addPage", "No"))
        self.label_8.setText(_translate("addPage", "Please insert the exact address of yourpicture( your jpg or png must be included in the address) and the time it was taken.\n"
"If the picture can be used as an evidence, please check yes and no if it\'s otherwised.\n"
"And then, please push \"Add\" button."))
        self.pushButton.setText(_translate("addPage", "Add"))

    def goToMainPage(self):
        self.a = self.address.text()
        self.y = self.yearTxt.text()
        self.mo= self.comboBox.currentText()
        self.d= self.dayTxt.text()
        self.h= self.hourTxt.text()
        self.mn= self.minTxt.text()
        if self.radioButton.isChecked():
            self.ev = True
        elif self.noRadio.isChecked:
            self.ev = False
        addPage.close()
        self.openMain( self.a, self.y, self.mo, self.d, self.h, self.mn, self.ev)


    def openMain(self, a, y, mo, d, h, mn, ev):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_mainPage()
        self.ui.setupUi(self.window, self.a, self.y, self.mo, self.d, self.h, self.mn, self.ev)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addPage = QtWidgets.QWidget()
    ui = Ui_addPage()
    ui.setupUi(addPage)
    addPage.show()
    sys.exit(app.exec_())
