from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import student
import teacher
from mainmenugui import Ui_MainWindow
import info
import database
import head
import sqlite3
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    switch_window = QtCore.pyqtSignal()
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.defaultid="admin"
        self.defaultpass="admin"
        self.info.clicked.connect(self.openInfoPanel)
        self.head.clicked.connect(self.openHeadPanel)
        self.student.clicked.connect(self.openStudentPanel)
        self.teacher.clicked.connect(self.openTeacherPanel)

    def openInfoPanel(self):
        self.infoWindow=info.MainWindow()
        self.id.clear()
        self.password.clear()

    def openHeadPanel(self):
        idinput=self.id.toPlainText()
        passinput=self.password.toPlainText()
        if idinput==self.defaultid and passinput==self.defaultpass:
            self.id.clear()
            self.password.clear()
            self.headWindow=head.MainWindow()
            self.errorDisplay.setText("")
        elif idinput!=self.defaultid:
            self.errorDisplay.setText("No Such ID Found! Please Check Your ID Again!")
        else :
            self.errorDisplay.setText("Incorrect Password! Please Check Your Password Again")
        

    def openStudentPanel(self):
        idinput = self.id.toPlainText()
        passinput = self.password.toPlainText()
        conn = sqlite3.connect('attendance.db')
        conn.execute('PRAGMA foreign_keys=on;')
        cursor = conn.execute("SELECT * FROM STUDENT WHERE roll_no=(?)", (idinput,))
        result=cursor.fetchall()
        conn.close()
        if len(result)==0:
            self.errorDisplay.setText("No Such ID Found! Please Check Your ID Again!")
        elif result[0][3]!=passinput:
            self.errorDisplay.setText("Incorrect Password! Please Check Your Password Again")
        else:
            self.errorDisplay.setText("")
            self.id.clear()
            self.password.clear()
            self.studentWindow=student.MainWindow(idinput)

    def openTeacherPanel(self):
        idinput = self.id.toPlainText()
        passinput = self.password.toPlainText()
        conn = sqlite3.connect('attendance.db')
        conn.execute('PRAGMA foreign_keys=on;')
        cursor = conn.execute("SELECT * FROM TEACHER WHERE faculty_id=(?)", (idinput,))
        result = cursor.fetchall()
        conn.close()
        if len(result) == 0:
            self.errorDisplay.setText("No Such ID Found! Please Check Your ID Again!")
        elif result[0][3] != passinput:
            self.errorDisplay.setText("Incorrect Password! Please Check Your Password Again")
        else:
            self.errorDisplay.setText("")
            self.id.clear()
            self.password.clear()
            self.teacherWindow = teacher.MainWindow(idinput)

database.Tables()
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
