from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from node import *
from dataStructure import *
import sys


class Ui_all_in_one(object):
	def setupUi(self, all_in_one):
		self.counter= 0
		all_in_one.setObjectName("all_in_one")
		all_in_one.resize(920, 880)
		all_in_one.setStyleSheet("background-color: rgb(255, 243, 228);")
		self.toolBox = QtWidgets.QToolBox(all_in_one)
		self.toolBox.setGeometry(QtCore.QRect(20, 10, 880, 861))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.toolBox.setFont(font)
		self.toolBox.setStyleSheet("background-color: rgb(50, 31, 40);\n"
"color: rgb(255, 243, 228);")
		self.toolBox.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.toolBox.setObjectName("toolBox")
		self.page = QtWidgets.QWidget()
		self.page.setGeometry(QtCore.QRect(0, 0, 880, 747))
		self.page.setObjectName("page")
		self.noRadio = QtWidgets.QRadioButton(self.page)
		self.noRadio.setGeometry(QtCore.QRect(285, 136, 46, 27))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.noRadio.setFont(font)
		self.noRadio.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.noRadio.setObjectName("noRadio")
		self.label_3 = QtWidgets.QLabel(self.page)
		self.label_3.setGeometry(QtCore.QRect(14, 136, 82, 23))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_3.setFont(font)
		self.label_3.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.label_3.setObjectName("label_3")
		self.yesRadio = QtWidgets.QRadioButton(self.page)
		self.yesRadio.setGeometry(QtCore.QRect(220, 136, 52, 27))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.yesRadio.setFont(font)
		self.yesRadio.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.yesRadio.setObjectName("yesRadio")
		self.minTxt = QtWidgets.QLineEdit(self.page)
		self.minTxt.setGeometry(QtCore.QRect(694, 76, 115, 29))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.minTxt.setFont(font)
		self.minTxt.setStyleSheet("color: rgb(231, 158, 79);")
		self.minTxt.setObjectName("minTxt")
		self.label_9 = QtWidgets.QLabel(self.page)
		self.label_9.setGeometry(QtCore.QRect(349, 80, 21, 16))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_9.setFont(font)
		self.label_9.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.label_9.setAlignment(QtCore.Qt.AlignCenter)
		self.label_9.setObjectName("label_9")
		self.yearTxt = QtWidgets.QLineEdit(self.page)
		self.yearTxt.setGeometry(QtCore.QRect(140, 76, 74, 29))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.yearTxt.setFont(font)
		self.yearTxt.setStyleSheet("color: rgb(231, 158, 79);")
		self.yearTxt.setObjectName("yearTxt")
		self.label = QtWidgets.QLabel(self.page)
		self.label.setGeometry(QtCore.QRect(14, 6, 73, 23))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label.setFont(font)
		self.label.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.page)
		self.label_2.setGeometry(QtCore.QRect(14, 76, 48, 23))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_2.setFont(font)
		self.label_2.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.label_2.setObjectName("label_2")
		self.timeLabel = QtWidgets.QLabel(self.page)
		self.timeLabel.setGeometry(QtCore.QRect(210, 700, 231, 31))
		font = QtGui.QFont()
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.timeLabel.setFont(font)
		self.timeLabel.setStyleSheet("color: rgb(255, 243, 228);")
		self.timeLabel.setText("")
		self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.timeLabel.setObjectName("timeLabel")
		self.comboBox = QtWidgets.QComboBox(self.page)
		self.comboBox.setGeometry(QtCore.QRect(220, 77, 123, 27))
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
		self.label_8 = QtWidgets.QLabel(self.page)
		self.label_8.setGeometry(QtCore.QRect(15, 172, 691, 61))
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
		self.label_5 = QtWidgets.QLabel(self.page)
		self.label_5.setGeometry(QtCore.QRect(497, 80, 27, 16))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_5.setFont(font)
		self.label_5.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.label_5.setAlignment(QtCore.Qt.AlignCenter)
		self.label_5.setObjectName("label_5")
		self.dayTxt = QtWidgets.QLineEdit(self.page)
		self.dayTxt.setGeometry(QtCore.QRect(376, 76, 115, 29))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.dayTxt.setFont(font)
		self.dayTxt.setStyleSheet("color: rgb(231, 158, 79);")
		self.dayTxt.setObjectName("dayTxt")
		self.label_4 = QtWidgets.QLabel(self.page)
		self.label_4.setEnabled(True)
		self.label_4.setGeometry(QtCore.QRect(108, 80, 26, 16))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_4.setFont(font)
		self.label_4.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.label_4.setObjectName("label_4")
		self.addButton = QtWidgets.QPushButton(self.page)
		self.addButton.setGeometry(QtCore.QRect(730, 180, 130, 50))
		self.addButton.setStyleSheet("color: rgb(50, 31, 40);\n"
"background-color: #E79E4F;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("Icons/103590_image_add_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.addButton.setIcon(icon)
		self.addButton.setIconSize(QtCore.QSize(28, 35))
		self.addButton.setObjectName("addButton")
		self.address = QtWidgets.QLineEdit(self.page)
		self.address.setGeometry(QtCore.QRect(140, 6, 671, 29))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.address.setFont(font)
		self.address.setStyleSheet("color: rgb(231, 158, 79);")
		self.address.setObjectName("address")
		self.hourTxt = QtWidgets.QLineEdit(self.page)
		self.hourTxt.setGeometry(QtCore.QRect(530, 76, 114, 29))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.hourTxt.setFont(font)
		self.hourTxt.setStyleSheet("color: rgb(231, 158, 79);")
		self.hourTxt.setObjectName("hourTxt")
		self.checkLabel = QtWidgets.QLabel(self.page)
		self.checkLabel.setGeometry(QtCore.QRect(460, 700, 221, 31))
		font = QtGui.QFont()
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.checkLabel.setFont(font)
		self.checkLabel.setStyleSheet("color: rgb(255, 243, 228);")
		self.checkLabel.setText("")
		self.checkLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.checkLabel.setObjectName("checkLabel")
		self.label_6 = QtWidgets.QLabel(self.page)
		self.label_6.setGeometry(QtCore.QRect(650, 80, 38, 16))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_6.setFont(font)
		self.label_6.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.label_6.setObjectName("label_6")
		self.picturePlace = QtWidgets.QLabel(self.page)
		self.picturePlace.setGeometry(QtCore.QRect(202, 260, 480, 430))
		self.picturePlace.setText("")
		self.picturePlace.setObjectName("picturePlace")
		self.picturePlace.setAlignment(QtCore.Qt.AlignCenter)
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap("Icons/103476_cancel_image_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.toolBox.addItem(self.page, icon1, "")
		self.page_2 = QtWidgets.QWidget()
		self.page_2.setGeometry(QtCore.QRect(0, 0, 880, 747))
		self.page_2.setObjectName("page_2")
		self.label_7 = QtWidgets.QLabel(self.page_2)
		self.label_7.setGeometry(QtCore.QRect(300, 10, 259, 23))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_7.setFont(font)
		self.label_7.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.label_7.setAlignment(QtCore.Qt.AlignCenter)
		self.label_7.setObjectName("label_7")
		self.label_10 = QtWidgets.QLabel(self.page_2)
		self.label_10.setGeometry(QtCore.QRect(140, 50, 591, 23))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(False)
		font.setUnderline(True)
		font.setWeight(50)
		self.label_10.setFont(font)
		self.label_10.setStyleSheet("color: rgb(252, 134, 33);")
		self.label_10.setAlignment(QtCore.Qt.AlignCenter)
		self.label_10.setObjectName("label_10")
		self.searchHour = QtWidgets.QLineEdit(self.page_2)
		self.searchHour.setGeometry(QtCore.QRect(579, 100, 86, 29))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.searchHour.setFont(font)
		self.searchHour.setStyleSheet("color: rgb(231, 158, 79);")
		self.searchHour.setObjectName("searchHour")
		self.simpleSearch = QtWidgets.QPushButton(self.page_2)
		self.simpleSearch.setGeometry(QtCore.QRect(560, 170, 275, 33))
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(False)
		font.setWeight(50)
		self.simpleSearch.setFont(font)
		self.simpleSearch.setStyleSheet("color: rgb(50, 31, 40);\n"
"background-color: #E79E4F;")
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap("Icons/392504_find_in_magnifier_magnifying_research_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.simpleSearch.setIcon(icon2)
		self.simpleSearch.setIconSize(QtCore.QSize(28, 35))
		self.simpleSearch.setObjectName("simpleSearch")
		self.label_11 = QtWidgets.QLabel(self.page_2)
		self.label_11.setGeometry(QtCore.QRect(546, 104, 27, 16))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_11.setFont(font)
		self.label_11.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.label_11.setAlignment(QtCore.Qt.AlignCenter)
		self.label_11.setObjectName("label_11")
		self.searchYear = QtWidgets.QLineEdit(self.page_2)
		self.searchYear.setGeometry(QtCore.QRect(161, 100, 101, 29))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.searchYear.setFont(font)
		self.searchYear.setStyleSheet("color: rgb(231, 158, 79);")
		self.searchYear.setObjectName("searchYear")
		self.label_12 = QtWidgets.QLabel(self.page_2)
		self.label_12.setEnabled(True)
		self.label_12.setGeometry(QtCore.QRect(121, 104, 26, 16))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_12.setFont(font)
		self.label_12.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.label_12.setObjectName("label_12")
		self.evidenceButton = QtWidgets.QPushButton(self.page_2)
		self.evidenceButton.setGeometry(QtCore.QRect(59, 170, 275, 33))
		font = QtGui.QFont()
		font.setFamily("MS Shell Dlg 2")
		font.setPointSize(14)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		self.evidenceButton.setFont(font)
		self.evidenceButton.setStyleSheet("color: rgb(50, 31, 40);\n"
"background-color: #E79E4F;")
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap("Icons/8103345_office_search_business_technology_research_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.evidenceButton.setIcon(icon3)
		self.evidenceButton.setIconSize(QtCore.QSize(28, 28))
		self.evidenceButton.setObjectName("evidenceButton")
		self.label_13 = QtWidgets.QLabel(self.page_2)
		self.label_13.setGeometry(QtCore.QRect(427, 104, 21, 16))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_13.setFont(font)
		self.label_13.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.label_13.setAlignment(QtCore.Qt.AlignCenter)
		self.label_13.setObjectName("label_13")
		self.label_14 = QtWidgets.QLabel(self.page_2)
		self.label_14.setGeometry(QtCore.QRect(671, 104, 38, 16))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_14.setFont(font)
		self.label_14.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.label_14.setObjectName("label_14")
		self.searchMin = QtWidgets.QLineEdit(self.page_2)
		self.searchMin.setGeometry(QtCore.QRect(715, 100, 87, 29))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.searchMin.setFont(font)
		self.searchMin.setStyleSheet("color: rgb(231, 158, 79);")
		self.searchMin.setObjectName("searchMin")
		self.label_29 = QtWidgets.QLabel(self.page_2)
		self.label_29.setGeometry(QtCore.QRect(61, 100, 48, 23))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_29.setFont(font)
		self.label_29.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.label_29.setObjectName("label_29")
		self.searchDay = QtWidgets.QLineEdit(self.page_2)
		self.searchDay.setGeometry(QtCore.QRect(454, 100, 86, 29))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.searchDay.setFont(font)
		self.searchDay.setStyleSheet("color: rgb(231, 158, 79);")
		self.searchDay.setObjectName("searchDay")
		self.searchMonth = QtWidgets.QComboBox(self.page_2)
		self.searchMonth.setGeometry(QtCore.QRect(280, 100, 141, 27))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.searchMonth.setFont(font)
		self.searchMonth.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.searchMonth.setObjectName("searchMonth")
		self.searchMonth.addItem("")
		self.searchMonth.addItem("")
		self.searchMonth.addItem("")
		self.searchMonth.addItem("")
		self.searchMonth.addItem("")
		self.searchMonth.addItem("")
		self.searchMonth.addItem("")
		self.searchMonth.addItem("")
		self.searchMonth.addItem("")
		self.searchMonth.addItem("")
		self.searchMonth.addItem("")
		self.searchMonth.addItem("")
		self.searchCheckLabel = QtWidgets.QLabel(self.page_2)
		self.searchCheckLabel.setGeometry(QtCore.QRect(460, 670, 221, 31))
		font = QtGui.QFont()
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.searchCheckLabel.setFont(font)
		self.searchCheckLabel.setText("")
		self.searchCheckLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.searchCheckLabel.setObjectName("searchCheckLabel")
		self.searchPicturePlace = QtWidgets.QLabel(self.page_2)
		self.searchPicturePlace.setGeometry(QtCore.QRect(200, 230, 471, 421))
		self.searchPicturePlace.setText("")
		self.searchPicturePlace.setObjectName("searchPicturePlace")
		self.searchPicturePlace.setAlignment(QtCore.Qt.AlignCenter)
		self.searchTimeLabel = QtWidgets.QLabel(self.page_2)
		self.searchTimeLabel.setGeometry(QtCore.QRect(190, 670, 251, 31))
		font = QtGui.QFont()
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.searchTimeLabel.setFont(font)
		self.searchTimeLabel.setText("")
		self.searchTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.searchTimeLabel.setObjectName("searchTimeLabel")
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap("Icons/103797_viewer_image_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.toolBox.addItem(self.page_2, icon4, "")
		self.page_3 = QtWidgets.QWidget()
		self.page_3.setObjectName("page_3")
		self.delDay = QtWidgets.QLineEdit(self.page_3)
		self.delDay.setGeometry(QtCore.QRect(460, 80, 86, 29))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.delDay.setFont(font)
		self.delDay.setStyleSheet("color: rgb(231, 158, 79);")
		self.delDay.setObjectName("delDay")
		self.label_30 = QtWidgets.QLabel(self.page_3)
		self.label_30.setGeometry(QtCore.QRect(67, 80, 48, 23))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_30.setFont(font)
		self.label_30.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.label_30.setObjectName("label_30")
		self.delCombo = QtWidgets.QComboBox(self.page_3)
		self.delCombo.setGeometry(QtCore.QRect(286, 80, 141, 27))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.delCombo.setFont(font)
		self.delCombo.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.delCombo.setObjectName("delCombo")
		self.delCombo.addItem("")
		self.delCombo.addItem("")
		self.delCombo.addItem("")
		self.delCombo.addItem("")
		self.delCombo.addItem("")
		self.delCombo.addItem("")
		self.delCombo.addItem("")
		self.delCombo.addItem("")
		self.delCombo.addItem("")
		self.delCombo.addItem("")
		self.delCombo.addItem("")
		self.delCombo.addItem("")
		self.delHour = QtWidgets.QLineEdit(self.page_3)
		self.delHour.setGeometry(QtCore.QRect(585, 80, 86, 29))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.delHour.setFont(font)
		self.delHour.setStyleSheet("color: rgb(231, 158, 79);")
		self.delHour.setObjectName("delHour")
		self.delYear = QtWidgets.QLineEdit(self.page_3)
		self.delYear.setGeometry(QtCore.QRect(167, 80, 101, 29))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.delYear.setFont(font)
		self.delYear.setStyleSheet("color: rgb(231, 158, 79);")
		self.delYear.setObjectName("delYear")
		self.label_31 = QtWidgets.QLabel(self.page_3)
		self.label_31.setGeometry(QtCore.QRect(552, 84, 27, 16))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_31.setFont(font)
		self.label_31.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.label_31.setAlignment(QtCore.Qt.AlignCenter)
		self.label_31.setObjectName("label_31")
		self.label_32 = QtWidgets.QLabel(self.page_3)
		self.label_32.setGeometry(QtCore.QRect(677, 84, 38, 16))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_32.setFont(font)
		self.label_32.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.label_32.setObjectName("label_32")
		self.label_33 = QtWidgets.QLabel(self.page_3)
		self.label_33.setGeometry(QtCore.QRect(212, 16, 451, 23))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_33.setFont(font)
		self.label_33.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.label_33.setAlignment(QtCore.Qt.AlignCenter)
		self.label_33.setObjectName("label_33")
		self.delMin = QtWidgets.QLineEdit(self.page_3)
		self.delMin.setGeometry(QtCore.QRect(721, 80, 87, 29))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.delMin.setFont(font)
		self.delMin.setStyleSheet("color: rgb(231, 158, 79);")
		self.delMin.setObjectName("delMin")
		self.label_34 = QtWidgets.QLabel(self.page_3)
		self.label_34.setGeometry(QtCore.QRect(433, 84, 21, 16))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_34.setFont(font)
		self.label_34.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.label_34.setAlignment(QtCore.Qt.AlignCenter)
		self.label_34.setObjectName("label_34")
		self.label_35 = QtWidgets.QLabel(self.page_3)
		self.label_35.setEnabled(True)
		self.label_35.setGeometry(QtCore.QRect(127, 84, 26, 16))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_35.setFont(font)
		self.label_35.setStyleSheet("\n"
"color: rgb(231, 158, 79);")
		self.label_35.setObjectName("label_35")
		self.delFind = QtWidgets.QPushButton(self.page_3)
		self.delFind.setGeometry(QtCore.QRect(622, 156, 191, 31))
		self.delFind.setStyleSheet("color: rgb(50, 31, 40);\n"
"background-color: #E79E4F;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
		icon5 = QtGui.QIcon()
		icon5.addPixmap(QtGui.QPixmap("Icons/3669134_find_in_page_ic_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.delFind.setIcon(icon5)
		self.delFind.setIconSize(QtCore.QSize(28, 35))
		self.delFind.setObjectName("delFind")
		self.delButton = QtWidgets.QPushButton(self.page_3)
		self.delButton.setGeometry(QtCore.QRect(270, 660, 111, 51))
		self.delButton.setStyleSheet("color: rgb(50, 31, 40);\n"
"background-color: #E79E4F;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
		icon6 = QtGui.QIcon()
		icon6.addPixmap(QtGui.QPixmap("Icons/103594_image_remove_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.delButton.setIcon(icon6)
		self.delButton.setIconSize(QtCore.QSize(30, 30))
		self.delButton.setObjectName("delButton")
		self.delCheckLabel = QtWidgets.QLabel(self.page_3)
		self.delCheckLabel.setGeometry(QtCore.QRect(340, 600, 221, 31))
		font = QtGui.QFont()
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.delCheckLabel.setFont(font)
		self.delCheckLabel.setText("")
		self.delCheckLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.delCheckLabel.setObjectName("delCheckLabel")
		self.delTimeLabel = QtWidgets.QLabel(self.page_3)
		self.delTimeLabel.setGeometry(QtCore.QRect(80, 600, 251, 31))
		font = QtGui.QFont()
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.delTimeLabel.setFont(font)
		self.delTimeLabel.setText("")
		self.delTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.delTimeLabel.setObjectName("delTimeLabel")
		self.delPicturePlace = QtWidgets.QLabel(self.page_3)
		self.delPicturePlace.setGeometry(QtCore.QRect(80, 160, 471, 421))
		self.delPicturePlace.setText("")
		self.delPicturePlace.setObjectName("delPicturePlace")
		self.delPicturePlace.setAlignment(QtCore.Qt.AlignCenter)
		self.toolBox.addItem(self.page_3, icon1, "")

		self.retranslateUi(all_in_one)
		self.toolBox.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(all_in_one)

		self.addButton.clicked.connect(self.addingPic)
		self.simpleSearch.clicked.connect(self.searchInAll)
		self.delFind.clicked.connect(self.delete)
		self.evidenceButton.clicked.connect(self.evidenceTag)

	def retranslateUi(self, all_in_one):
		_translate = QtCore.QCoreApplication.translate
		all_in_one.setWindowTitle(_translate("all_in_one", "Form"))
		self.noRadio.setText(_translate("all_in_one", "No"))
		self.label_3.setText(_translate("all_in_one", "Evidence:"))
		self.yesRadio.setText(_translate("all_in_one", "Yes"))
		self.label_9.setText(_translate("all_in_one", "Day"))
		self.label.setText(_translate("all_in_one", "Address:"))
		self.label_2.setText(_translate("all_in_one", "Time:"))
		self.comboBox.setItemText(0, _translate("all_in_one", "January"))
		self.comboBox.setItemText(1, _translate("all_in_one", "February"))
		self.comboBox.setItemText(2, _translate("all_in_one", "March"))
		self.comboBox.setItemText(3, _translate("all_in_one", "April"))
		self.comboBox.setItemText(4, _translate("all_in_one", "May"))
		self.comboBox.setItemText(5, _translate("all_in_one", "June"))
		self.comboBox.setItemText(6, _translate("all_in_one", "July"))
		self.comboBox.setItemText(7, _translate("all_in_one", "August"))
		self.comboBox.setItemText(8, _translate("all_in_one", "September"))
		self.comboBox.setItemText(9, _translate("all_in_one", "October"))
		self.comboBox.setItemText(10, _translate("all_in_one", "November"))
		self.comboBox.setItemText(11, _translate("all_in_one", "December"))
		self.label_8.setText(_translate("all_in_one", "Please insert the exact address of yourpicture( your jpg or png must be included in the address) and the time it was taken.\n"
"If the picture can be used as an evidence, please check yes and no if it\'s otherwised.\n"
"And then, please push \"Add\" button."))
		self.label_5.setText(_translate("all_in_one", "Hour"))
		self.label_4.setText(_translate("all_in_one", "Year"))
		self.addButton.setText(_translate("all_in_one", "Add"))
		self.label_6.setText(_translate("all_in_one", "Minute"))
		self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("all_in_one", "Adding New Pictures Here"))
		self.label_7.setText(_translate("all_in_one", "Search for a picture by its time"))
		self.label_10.setText(_translate("all_in_one", "!Please make sure that you have already added some pictures before you do the searching!"))
		self.simpleSearch.setText(_translate("all_in_one", "Simple Search"))
		self.label_11.setText(_translate("all_in_one", "Hour"))
		self.label_12.setText(_translate("all_in_one", "Year"))
		self.evidenceButton.setText(_translate("all_in_one", "Search in the Evidences"))
		self.label_13.setText(_translate("all_in_one", "Day"))
		self.label_14.setText(_translate("all_in_one", "Minute"))
		self.label_29.setText(_translate("all_in_one", "Time:"))
		self.searchMonth.setItemText(0, _translate("all_in_one", "January"))
		self.searchMonth.setItemText(1, _translate("all_in_one", "February"))
		self.searchMonth.setItemText(2, _translate("all_in_one", "March"))
		self.searchMonth.setItemText(3, _translate("all_in_one", "April"))
		self.searchMonth.setItemText(4, _translate("all_in_one", "May"))
		self.searchMonth.setItemText(5, _translate("all_in_one", "June"))
		self.searchMonth.setItemText(6, _translate("all_in_one", "July"))
		self.searchMonth.setItemText(7, _translate("all_in_one", "August"))
		self.searchMonth.setItemText(8, _translate("all_in_one", "September"))
		self.searchMonth.setItemText(9, _translate("all_in_one", "October"))
		self.searchMonth.setItemText(10, _translate("all_in_one", "November"))
		self.searchMonth.setItemText(11, _translate("all_in_one", "December"))
		self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("all_in_one", "Searching for a Picture Here"))
		self.label_30.setText(_translate("all_in_one", "Time:"))
		self.delCombo.setItemText(0, _translate("all_in_one", "January"))
		self.delCombo.setItemText(1, _translate("all_in_one", "February"))
		self.delCombo.setItemText(2, _translate("all_in_one", "March"))
		self.delCombo.setItemText(3, _translate("all_in_one", "April"))
		self.delCombo.setItemText(4, _translate("all_in_one", "May"))
		self.delCombo.setItemText(5, _translate("all_in_one", "June"))
		self.delCombo.setItemText(6, _translate("all_in_one", "July"))
		self.delCombo.setItemText(7, _translate("all_in_one", "August"))
		self.delCombo.setItemText(8, _translate("all_in_one", "September"))
		self.delCombo.setItemText(9, _translate("all_in_one", "October"))
		self.delCombo.setItemText(10, _translate("all_in_one", "November"))
		self.delCombo.setItemText(11, _translate("all_in_one", "December"))
		self.label_31.setText(_translate("all_in_one", "Hour"))
		self.label_32.setText(_translate("all_in_one", "Minute"))
		self.label_33.setText(_translate("all_in_one", "Search for a picture by its time for deleting"))
		self.label_34.setText(_translate("all_in_one", "Day"))
		self.label_35.setText(_translate("all_in_one", "Year"))
		self.delFind.setText(_translate("all_in_one", "Find"))
		self.delButton.setText(_translate("all_in_one", "Delete"))
		self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("all_in_one", "Deleting a Picture"))

	def addingPic(self):
		address = self.address.text()
		pixmap = QtGui.QPixmap(address)
		pixmapSize = pixmap.scaled(480, 430)
		self.picturePlace.setPixmap(pixmap)
		year = self.yearTxt.text()
		month = self.comboBox.currentText()
		day = self.dayTxt.text()
		hour = self.hourTxt.text()
		minute = self.minTxt.text()
		if self.yesRadio.isChecked():
			evidence = True
		elif self.noRadio.isChecked:
			evidence = False
		self.timeLabel.setText(f"{day} {month} {year} {hour}:{minute}")
		self.checkLabel.setText(str(evidence))
		
		if self.counter == 0:

			pointer = Node(address, int(year), month, int(day), int(hour), int(minute), evidence)
			self.l1 = LinkedListPictures(pointer)
			self.counter += 1
		
		elif self.counter >= 1:
			pointer = Node(address, int(year), month, int(day), int(hour), int(minute), evidence)
			self.l1.addData(address, int(year), month, int(day), int(hour), int(minute), evidence)

	def searchInAll(self):
		year2 = self.searchYear.text()
		month2= self.searchMonth.currentText()
		day2= self.searchDay.text()
		hour2= self.searchHour.text()
		minute2= self.searchMin.text()
		searcher = Node("", int(year2), month2, int(day2), int(hour2), int(minute2))
		try:
			infoTuple = self.l1.searchNextNodeByTag(searcher).getInformation()
			pixmap = QtGui.QPixmap(infoTuple[0])
			pixmapSize = pixmap.scaled(480, 430)
			self.searchPicturePlace.setPixmap(pixmap)
			self.searchCheckLabel.setText(str(infoTuple[-1]))
			self.searchTimeLabel.setText(str(infoTuple[1]))
		except AttributeError:
			msg = QMessageBox()
			msg.setWindowTitle("Wrong Information")
			msg.setText("There is no information for this date!\nPlease enter another timing.")
			msg.setIcon(QMessageBox.Information)
			x = msg.exec_()

	def delete(self):
		year3 = self.delYear.text()
		month3= self.delCombo.currentText()
		day3= self.delDay.text()
		hour3= self.delHour.text()
		minute3= self.delMin.text()
		self.selectDel = Node("", int(year3), month3, int(day3), int(hour3), int(minute3))
		
		nodeInList = self.l1.searchNode(node=self.selectDel, equal=True)
		if nodeInList is not None:
			self.infoTuple = nodeInList.getInformation()
			pixmap = QtGui.QPixmap(self.infoTuple[0])
			pixmapSize = pixmap.scaled(480, 430)
			self.delPicturePlace.setPixmap(pixmap)
			self.delCheckLabel.setText(str(self.infoTuple[-1]))
			self.delTimeLabel.setText(str(self.infoTuple[1]))
			self.delButton.clicked.connect(self.finalDel)
			return

		msg = QMessageBox()
		msg.setWindowTitle("Wrong Information")
		msg.setText("There is no information for this date!\nPlease enter another timing.")
		msg.setIcon(QMessageBox.Information)
		x = msg.exec_()		
		
		
		# try:
		# 	self.infoTuple = self.l1.searchNode(self.selectDel, equal=True).getInformation()
		# 	pixmap = QtGui.QPixmap(self.infoTuple[0])
		# 	pixmapSize = pixmap.scaled(480, 430)
		# 	self.delPicturePlace.setPixmap(pixmap)
		# 	self.delCheckLabel.setText(str(self.infoTuple[-1]))
		# 	self.delTimeLabel.setText(str(self.infoTuple[1]))
		# 	self.delButton.clicked.connect(self.finalDel)

		# except AttributeError:
		# 	msg = QMessageBox()
		# 	msg.setWindowTitle("Wrong Information")
		# 	msg.setText("There is no information for this date!\nPlease enter another timing.")
		# 	msg.setIcon(QMessageBox.Information)
		# 	x = msg.exec_()

	def finalDel(self):
		newDel = Node(self.infoTuple[0],self.infoTuple[1].year, self.infoTuple[1].month, self.infoTuple[1].day, self.infoTuple[1].hour,self.infoTuple[1].minute, self.infoTuple[2])
		self.l1.deleteNode(newDel)
		msg = QMessageBox()
		msg.setWindowTitle("Deleted")
		msg.setText("The picture is successfully deleted.")
		msg.setIcon(QMessageBox.Information)
		x = msg.exec_()
	

	def evidenceTag(self):
		year2 = self.searchYear.text()
		month2= self.searchMonth.currentText()
		day2= self.searchDay.text()
		hour2= self.searchHour.text()
		minute2= self.searchMin.text()
		tagSearcher = Node("", int(year2), month2, int(day2), int(hour2), int(minute2))
		try:
			infoTuple = self.l1.searchNextNodeByTag(tagSearcher, tagIsImportant= True).getInformation()
			pixmap = QtGui.QPixmap(infoTuple[0])
			pixmapSize = pixmap.scaled(480, 430)
			self.searchPicturePlace.setPixmap(pixmap)
			self.searchCheckLabel.setText(str(infoTuple[-1]))
			self.searchTimeLabel.setText(str(infoTuple[1]))
			
		except AttributeError:
			msg = QMessageBox()
			msg.setWindowTitle("Wrong Information")
			msg.setText("There is no information for this date!\nPlease enter another timing.")
			msg.setIcon(QMessageBox.Information)
			x = msg.exec_()
		
	def __printLog(object, operation, logObject=''):
		operationDict = {
		'd': Fore.RED +'deleted',
		'a': Fore.LIGHTMAGENTA_EX + 'added',
		'l': Fore.CYAN + 'list',
		'nF': Fore.YELLOW + 'not found',
		'nFN': Fore.YELLOW + 'Not Found next node',
		'nFNT': Fore.YELLOW + 'not found next TRUE node',
		's': Fore.GREEN + 'search',
		'sN': Fore.GREEN + 'search next node',
		'sNT': Fore.GREEN + 'search next TRUE node',
		'ch': Fore.YELLOW + 'change node'}
		print(operationDict[operation] + ' ' + str(logObject) + ' ' + Fore.RESET + str(object))
		

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	all_in_one = QtWidgets.QWidget()
	ui = Ui_all_in_one()
	ui.setupUi(all_in_one)
	all_in_one.show()
	sys.exit(app.exec_())
