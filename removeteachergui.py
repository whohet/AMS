# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'removeteachergui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet("background-color: rgb(219, 221, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.id = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(240, 260, 391, 31))
        self.id.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.id.setObjectName("id")
        self.fname = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.fname.setGeometry(QtCore.QRect(800, 280, 391, 31))
        self.fname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fname.setObjectName("fname")
        self.password = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(240, 310, 391, 31))
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password.setObjectName("password")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(130, 260, 91, 31))
        self.label_1.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(650, 280, 131, 31))
        self.label_2.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(650, 330, 131, 31))
        self.label_3.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 310, 111, 31))
        self.label_4.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_4.setObjectName("label_4")
        self.lname = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.lname.setGeometry(QtCore.QRect(800, 330, 391, 31))
        self.lname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lname.setObjectName("lname")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 360, 211, 31))
        self.label_5.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_5.setObjectName("label_5")
        self.confirmpass = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.confirmpass.setGeometry(QtCore.QRect(240, 360, 391, 31))
        self.confirmpass.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.confirmpass.setObjectName("confirmpass")
        self.errorDisplay = QtWidgets.QLabel(self.centralwidget)
        self.errorDisplay.setGeometry(QtCore.QRect(0, 500, 1281, 61))
        self.errorDisplay.setStyleSheet("qproperty-alignment: AlignCenter;\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(217, 48, 37);")
        self.errorDisplay.setText("")
        self.errorDisplay.setObjectName("errorDisplay")
        self.addNew = QtWidgets.QPushButton(self.centralwidget)
        self.addNew.setGeometry(QtCore.QRect(570, 440, 141, 31))
        self.addNew.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(52, 168, 83);")
        self.addNew.setObjectName("addNew")
        self.old_id = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.old_id.setGeometry(QtCore.QRect(450, 100, 391, 31))
        self.old_id.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.old_id.setObjectName("old_id")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 100, 81, 31))
        self.label.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label.setObjectName("label")
        self.remove = QtWidgets.QPushButton(self.centralwidget)
        self.remove.setGeometry(QtCore.QRect(590, 140, 111, 31))
        self.remove.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(217, 48, 37);")
        self.remove.setObjectName("remove")
        self.errorDisplay_2 = QtWidgets.QLabel(self.centralwidget)
        self.errorDisplay_2.setGeometry(QtCore.QRect(0, 180, 1281, 61))
        self.errorDisplay_2.setStyleSheet("color: rgb(60, 25, 255);\n"
"font: 16pt \"Nirmala UI\";")
        self.errorDisplay_2.setObjectName("errorDisplay_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 20, 1281, 51))
        self.label_6.setStyleSheet("color: rgb(60, 25, 255);\n"
"font: 16pt \"Nirmala UI\";")
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Delete Faculty"))
        self.label_1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">New ID</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">First Name</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Last Name</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Password</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Confirm Password</span></p></body></html>"))
        self.addNew.setText(_translate("MainWindow", "Add New!"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Old ID</span></p></body></html>"))
        self.remove.setText(_translate("MainWindow", "Remove"))
        self.errorDisplay_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">As There is Only One Faculty, You Need To Enter A New Faculty to Take Over This Course</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Remove an Existing Faculty</span></p></body></html>"))

