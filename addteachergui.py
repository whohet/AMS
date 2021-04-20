# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addteachergui.ui'
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
        self.id.setGeometry(QtCore.QRect(230, 180, 391, 31))
        self.id.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.id.setObjectName("id")
        self.fname = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.fname.setGeometry(QtCore.QRect(780, 180, 391, 31))
        self.fname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fname.setObjectName("fname")
        self.course_id = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.course_id.setGeometry(QtCore.QRect(780, 280, 391, 31))
        self.course_id.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.course_id.setObjectName("course_id")
        self.password = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(230, 230, 391, 31))
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 180, 61, 31))
        self.label.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(650, 180, 111, 31))
        self.label_2.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(650, 230, 111, 31))
        self.label_3.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 230, 211, 31))
        self.label_4.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(630, 280, 121, 31))
        self.label_5.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_5.setObjectName("label_5")
        self.lname = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.lname.setGeometry(QtCore.QRect(780, 230, 391, 31))
        self.lname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lname.setObjectName("lname")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 280, 211, 31))
        self.label_6.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_6.setObjectName("label_6")
        self.confirmpass = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.confirmpass.setGeometry(QtCore.QRect(230, 280, 391, 31))
        self.confirmpass.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.confirmpass.setObjectName("confirmpass")
        self.errorDisplay = QtWidgets.QLabel(self.centralwidget)
        self.errorDisplay.setGeometry(QtCore.QRect(0, 460, 1281, 61))
        self.errorDisplay.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(217, 48, 37);\n"
"qproperty-alignment: AlignCenter;")
        self.errorDisplay.setText("")
        self.errorDisplay.setObjectName("errorDisplay")
        self.addNew = QtWidgets.QPushButton(self.centralwidget)
        self.addNew.setGeometry(QtCore.QRect(530, 400, 221, 41))
        self.addNew.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(52, 168, 83);")
        self.addNew.setObjectName("addNew")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 10, 1281, 121))
        self.label_7.setStyleSheet("color: rgb(60, 25, 255);\n"
"font: 16pt \"Nirmala UI\";")
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Teacher"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; font-weight:600;\">ID</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; font-weight:600;\">First Name</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; font-weight:600;\">Last Name</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; font-weight:600;\">Password</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; font-weight:600;\">Course ID</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; font-weight:600;\">Confirm Password</span></p></body></html>"))
        self.addNew.setText(_translate("MainWindow", "Add New Teacher!"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Assign a New Faculty</span></p></body></html>"))

