from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import addTeacher
import addStudent
import delStudent
import delTeacher
from headgui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    switch_window = QtCore.pyqtSignal()
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.addTeacher.clicked.connect(self.addTeach)
        self.addStudent.clicked.connect(self.addStu)
        self.delTeacher.clicked.connect(self.delTeach)
        self.delStudent.clicked.connect(self.delStu)
        self.run()

    def addTeach(self):
        self.addTeacherPanel = addTeacher.MainWindow()
    def delTeach(self):
        self.delTeacherPanel = delTeacher.MainWindow()
    def addStu(self):
        self.addStudentPanel = addStudent.MainWindow()
    def delStu(self):
        self.delStudentPanel = delStudent.MainWindow()
    def run(self):
        self.show()
