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
        self.present = QtWidgets.QRadioButton(self.centralwidget)
        self.present.setGeometry(QtCore.QRect(660, 390, 121, 31))
        self.present.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.present.setObjectName("present")
        self.absent = QtWidgets.QRadioButton(self.centralwidget)
        self.absent.setGeometry(QtCore.QRect(524, 390, 111, 31))
        self.absent.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.absent.setObjectName("absent")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 170, 171, 61))
        self.label.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label.setObjectName("label")
        self.id = QtWidgets.QLabel(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(650, 170, 631, 61))
        self.id.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.id.setObjectName("id")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 220, 191, 71))
        self.label_2.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_2.setObjectName("label_2")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(650, 230, 631, 51))
        self.name.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.name.setObjectName("name")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 20, 1281, 61))
        self.title.setStyleSheet("color: rgb(60, 25, 255);\n"
"qproperty-alignment: AlignCenter;\n"
"font: 95 16pt \"Nirmala UI\";")
        self.title.setObjectName("title")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(590, 450, 93, 28))
        self.next.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(52, 168, 83);")
        self.next.setObjectName("next")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 329, 1281, 51))
        self.label_3.setStyleSheet("color: rgb(60, 25, 255);\n"
"font: 16pt \"Nirmala UI\";")
        self.label_3.setObjectName("label_3")
        self.errorDisplay = QtWidgets.QLabel(self.centralwidget)
        self.errorDisplay.setGeometry(QtCore.QRect(0, 520, 1281, 61))
        self.errorDisplay.setStyleSheet("qproperty-alignment: AlignCenter;\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.errorDisplay.setObjectName("errorDisplay")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(510, 100, 261, 41))
        self.start.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(123, 123, 184);")
        self.start.setObjectName("start")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Attendance Sheet"))
        self.present.setText(_translate("MainWindow", "Present"))
        self.absent.setText(_translate("MainWindow", "Absent"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:14pt; font-weight:600;\">Student\'s ID</span></p></body></html>"))
        self.id.setText(_translate("MainWindow", "ID"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Student\'s Name</span></p></body></html>"))
        self.name.setText(_translate("MainWindow", "Name"))
        self.title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Attendence Sheet of Subject</span></p></body></html>"))
        self.next.setText(_translate("MainWindow", "Next"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Enter Status</span></p></body></html>"))
        self.errorDisplay.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.start.setText(_translate("MainWindow", "Start Taking Attendence"))

