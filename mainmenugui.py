from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.id = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(920, 440, 181, 31))
        self.id.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.id.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.id.setObjectName("id")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(790, 440, 111, 41))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label.setObjectName("label")
        self.head = QtWidgets.QPushButton(self.centralwidget)
        self.head.setGeometry(QtCore.QRect(630, 570, 171, 31))
        self.head.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(83, 83, 255);\n"
"background-color: rgb(255,255,255);")
        self.head.setObjectName("head")
        self.teacher = QtWidgets.QPushButton(self.centralwidget)
        self.teacher.setGeometry(QtCore.QRect(840, 570, 171, 31))
        self.teacher.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(83, 83, 255);\n"
"background-color: rgb(255,255,255);")
        self.teacher.setObjectName("teacher")
        self.student = QtWidgets.QPushButton(self.centralwidget)
        self.student.setGeometry(QtCore.QRect(1050, 570, 171, 31))
        self.student.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(83, 83, 255);\n"
"background-color: rgb(255,255,255);")
        self.student.setObjectName("student")
        self.password = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(920, 480, 181, 31))
        self.password.setMaximumSize(QtCore.QSize(16777215, 31))
        self.password.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password.setObjectName("password")
        self.errorDisplay = QtWidgets.QLabel(self.centralwidget)
        self.errorDisplay.setGeometry(QtCore.QRect(630, 620, 591, 41))
        self.errorDisplay.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color:  rgb(217, 48, 37);\n"
"qproperty-alignment: AlignCenter;")
        self.errorDisplay.setObjectName("errorDisplay")
        self.info = QtWidgets.QPushButton(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(130, 640, 271, 41))
        self.info.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(52, 168, 83);")
        self.info.setObjectName("info")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(840, 530, 171, 41))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 480, 641, 28))
        self.label_2.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("bg.jpeg"))
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()
        self.id.raise_()
        self.label.raise_()
        self.head.raise_()
        self.teacher.raise_()
        self.student.raise_()
        self.password.raise_()
        self.errorDisplay.raise_()
        self.info.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600; color:#ffffff;\">Enter ID</span></p></body></html>"))
        self.head.setText(_translate("MainWindow", "Head of Institute"))
        self.teacher.setText(_translate("MainWindow", "Teacher"))
        self.student.setText(_translate("MainWindow", "Student"))
        self.errorDisplay.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\"><br/></span></p></body></html>"))
        self.info.setText(_translate("MainWindow", "Information Related to Database"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Login As</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600; color:#ffffff;\">Enter Password</span></p></body></html>"))

