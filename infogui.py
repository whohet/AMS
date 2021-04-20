from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(656, 648)
        MainWindow.setStyleSheet("background-color: rgb(219, 221, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("color: rgb(60, 25, 255);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.teacher_details = QtWidgets.QTextBrowser(self.centralwidget)
        self.teacher_details.setStyleSheet("font: 12pt \"Consolas\";\n"
"background-color: rgb(255, 255, 255);")
        self.teacher_details.setObjectName("teacher_details")
        self.verticalLayout.addWidget(self.teacher_details)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color: rgb(60, 25, 255);\n"
"font: 14pt \"Nirmala UI\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.course_details = QtWidgets.QTextBrowser(self.centralwidget)
        self.course_details.setStyleSheet("font: 12pt \"Consolas\";\n"
"background-color: rgb(255, 255, 255);")
        self.course_details.setObjectName("course_details")
        self.verticalLayout.addWidget(self.course_details)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Information about Database"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Teacher Details</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Course Details</span></p></body></html>"))

