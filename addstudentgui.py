# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addstudentgui.ui'
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
        self.id.setGeometry(QtCore.QRect(220, 150, 391, 31))
        self.id.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.id.setObjectName("id")
        self.fname = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.fname.setGeometry(QtCore.QRect(800, 170, 391, 31))
        self.fname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fname.setObjectName("fname")
        self.t_id_1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.t_id_1.setGeometry(QtCore.QRect(220, 350, 391, 31))
        self.t_id_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t_id_1.setObjectName("t_id_1")
        self.password = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(220, 200, 391, 31))
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 150, 31, 31))
        self.label.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(670, 170, 121, 31))
        self.label_2.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(670, 230, 111, 31))
        self.label_3.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 200, 101, 31))
        self.label_4.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 350, 151, 31))
        self.label_5.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_5.setObjectName("label_5")
        self.lname = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.lname.setGeometry(QtCore.QRect(800, 230, 391, 31))
        self.lname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lname.setObjectName("lname")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 191, 31))
        self.label_6.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_6.setObjectName("label_6")
        self.confirmpass = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.confirmpass.setGeometry(QtCore.QRect(220, 250, 391, 31))
        self.confirmpass.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.confirmpass.setObjectName("confirmpass")
        self.errorDisplay = QtWidgets.QLabel(self.centralwidget)
        self.errorDisplay.setGeometry(QtCore.QRect(0, 580, 1281, 61))
        self.errorDisplay.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: AlignCenter;\n"
"color: rgb(217, 48, 37);")
        self.errorDisplay.setObjectName("errorDisplay")
        self.addNew = QtWidgets.QPushButton(self.centralwidget)
        self.addNew.setGeometry(QtCore.QRect(550, 520, 201, 41))
        self.addNew.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(52, 168, 83);")
        self.addNew.setObjectName("addNew")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 400, 141, 31))
        self.label_7.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(650, 350, 141, 31))
        self.label_8.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(650, 400, 141, 31))
        self.label_9.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_9.setObjectName("label_9")
        self.t_id_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.t_id_2.setGeometry(QtCore.QRect(220, 400, 391, 31))
        self.t_id_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t_id_2.setObjectName("t_id_2")
        self.t_id_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.t_id_3.setGeometry(QtCore.QRect(800, 350, 391, 31))
        self.t_id_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t_id_3.setObjectName("t_id_3")
        self.t_id_4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.t_id_4.setGeometry(QtCore.QRect(800, 400, 391, 31))
        self.t_id_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t_id_4.setObjectName("t_id_4")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(0, 30, 1281, 81))
        self.label_10.setStyleSheet("color: rgb(60, 25, 255);\n"
"font: 16pt \"Nirmala UI\";")
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Student"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">ID</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">First Name</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Last Name</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Password</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Faculty 1\'s ID</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Confirm Password</span></p></body></html>"))
        self.errorDisplay.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.addNew.setText(_translate("MainWindow", "Add New Student!"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Faculty 2\'s ID</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Faculty 3\'s ID</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Faculty 4\'s ID</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Enroll a New Student</span></p></body></html>"))

