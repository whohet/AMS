# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'headgui.ui'
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
        self.addTeacher = QtWidgets.QPushButton(self.centralwidget)
        self.addTeacher.setGeometry(QtCore.QRect(140, 310, 191, 41))
        self.addTeacher.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(123, 123, 184);")
        self.addTeacher.setObjectName("addTeacher")
        self.addStudent = QtWidgets.QPushButton(self.centralwidget)
        self.addStudent.setGeometry(QtCore.QRect(950, 310, 191, 41))
        self.addStudent.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(123, 123, 184);")
        self.addStudent.setObjectName("addStudent")
        self.delTeacher = QtWidgets.QPushButton(self.centralwidget)
        self.delTeacher.setGeometry(QtCore.QRect(80, 370, 301, 41))
        self.delTeacher.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(123, 123, 184);")
        self.delTeacher.setObjectName("delTeacher")
        self.delStudent = QtWidgets.QPushButton(self.centralwidget)
        self.delStudent.setGeometry(QtCore.QRect(900, 370, 301, 41))
        self.delStudent.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(123, 123, 184);")
        self.delStudent.setObjectName("delStudent")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(124, 240, 221, 41))
        self.label.setStyleSheet("color: rgb(123, 123, 184);\n"
"font: 16pt \"Nirmala UI\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(930, 240, 241, 41))
        self.label_2.setStyleSheet("color: rgb(123, 123, 184);\n"
"font: 16pt \"Nirmala UI\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 1281, 151))
        self.label_3.setStyleSheet("color: rgb(60, 25, 255);\n"
"font: 16pt \"Nirmala UI\";")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manage Students and Teachers"))
        self.addTeacher.setText(_translate("MainWindow", "Add a New Teacher"))
        self.addStudent.setText(_translate("MainWindow", "Add a New Student"))
        self.delTeacher.setText(_translate("MainWindow", "Delete Existing Teacher Records"))
        self.delStudent.setText(_translate("MainWindow", "Delete Existing Student Records"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Manage Teachers</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Manage Students</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Manage Students and Teachers</span></p></body></html>"))

