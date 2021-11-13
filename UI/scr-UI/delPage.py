# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_delPage(object):
    def setupUi(self, delPage):
        delPage.setObjectName("delPage")
        delPage.resize(800, 250)
        delPage.setStyleSheet("background-color: rgb(50, 31, 40);")
        self.pushButton = QtWidgets.QPushButton(delPage)
        self.pushButton.setGeometry(QtCore.QRect(560, 180, 191, 31))
        self.pushButton.setStyleSheet("color: rgb(50, 31, 40);\n"
"background-color: #E79E4F;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/3669134_find_in_page_ic_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(28, 35))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(delPage)
        self.comboBox.setGeometry(QtCore.QRect(224, 104, 141, 27))
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
        self.label_4 = QtWidgets.QLabel(delPage)
        self.label_4.setGeometry(QtCore.QRect(150, 40, 451, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(delPage)
        self.label_6.setGeometry(QtCore.QRect(615, 108, 38, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(delPage)
        self.label_2.setGeometry(QtCore.QRect(5, 104, 48, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
        self.label_2.setObjectName("label_2")
        self.hourTxt = QtWidgets.QLineEdit(delPage)
        self.hourTxt.setGeometry(QtCore.QRect(523, 104, 86, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.hourTxt.setFont(font)
        self.hourTxt.setStyleSheet("color: rgb(231, 158, 79);")
        self.hourTxt.setObjectName("hourTxt")
        self.minTxt = QtWidgets.QLineEdit(delPage)
        self.minTxt.setGeometry(QtCore.QRect(659, 104, 87, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.minTxt.setFont(font)
        self.minTxt.setStyleSheet("color: rgb(231, 158, 79);")
        self.minTxt.setObjectName("minTxt")
        self.label_8 = QtWidgets.QLabel(delPage)
        self.label_8.setGeometry(QtCore.QRect(371, 108, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(delPage)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(65, 108, 26, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
        self.label_5.setObjectName("label_5")
        self.dayTxt = QtWidgets.QLineEdit(delPage)
        self.dayTxt.setGeometry(QtCore.QRect(398, 104, 86, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dayTxt.setFont(font)
        self.dayTxt.setStyleSheet("color: rgb(231, 158, 79);")
        self.dayTxt.setObjectName("dayTxt")
        self.label_9 = QtWidgets.QLabel(delPage)
        self.label_9.setGeometry(QtCore.QRect(490, 108, 27, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.yearTxt = QtWidgets.QLineEdit(delPage)
        self.yearTxt.setGeometry(QtCore.QRect(105, 104, 101, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.yearTxt.setFont(font)
        self.yearTxt.setStyleSheet("color: rgb(231, 158, 79);")
        self.yearTxt.setObjectName("yearTxt")

        self.retranslateUi(delPage)
        QtCore.QMetaObject.connectSlotsByName(delPage)

    def retranslateUi(self, delPage):
        _translate = QtCore.QCoreApplication.translate
        delPage.setWindowTitle(_translate("delPage", "Deleting Page"))
        self.pushButton.setText(_translate("delPage", "Find"))
        self.comboBox.setItemText(0, _translate("delPage", "January"))
        self.comboBox.setItemText(1, _translate("delPage", "February"))
        self.comboBox.setItemText(2, _translate("delPage", "March"))
        self.comboBox.setItemText(3, _translate("delPage", "April"))
        self.comboBox.setItemText(4, _translate("delPage", "May"))
        self.comboBox.setItemText(5, _translate("delPage", "June"))
        self.comboBox.setItemText(6, _translate("delPage", "July"))
        self.comboBox.setItemText(7, _translate("delPage", "August"))
        self.comboBox.setItemText(8, _translate("delPage", "September"))
        self.comboBox.setItemText(9, _translate("delPage", "October"))
        self.comboBox.setItemText(10, _translate("delPage", "November"))
        self.comboBox.setItemText(11, _translate("delPage", "December"))
        self.label_4.setText(_translate("delPage", "Search for a picture by its time for deleting"))
        self.label_6.setText(_translate("delPage", "Minute"))
        self.label_2.setText(_translate("delPage", "Time:"))
        self.label_8.setText(_translate("delPage", "Day"))
        self.label_5.setText(_translate("delPage", "Year"))
        self.label_9.setText(_translate("delPage", "Hour"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    delPage = QtWidgets.QWidget()
    ui = Ui_delPage()
    ui.setupUi(delPage)
    delPage.show()
    sys.exit(app.exec_())
