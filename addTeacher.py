from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from addteachergui import Ui_MainWindow
import sqlite3


class MainWindow(QMainWindow, Ui_MainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.addNew.clicked.connect(self.addTeach)
        self.run()
    def addTeach(self):
        idinput = self.id.toPlainText()
        passinput = self.password.toPlainText()
        confirmpass = self.confirmpass.toPlainText()
        fname = self.fname.toPlainText()
        lname = self.lname.toPlainText()
        course_id = self.course_id.toPlainText()
        conn = sqlite3.connect('attendance.db')
        conn.execute('PRAGMA foreign_keys=on;')
        cursor = conn.execute("SELECT * FROM TEACHER WHERE faculty_id=(?)", (idinput,))
        result = cursor.fetchall()
        if len(result) != 0:
            self.errorDisplay.setText("Entered ID Already Exists! Enter a Unique ID to Register.")
        elif idinput == "":
            self.errorDisplay.setText("ID can't be NULL! Try Again by Entering a Valid ID.")
        elif passinput=="":
            self.errorDisplay.setText("Password Field Can't Be Empty! Try Again by Entering a Valid ID.")
        elif passinput != confirmpass:
            self.errorDisplay.setText("Password and Confirm Password field doesn't match. Try Again!")
        elif lname=="" or fname=="":
            self.errorDisplay.setText("Name Fields Can't Be Empty!")
        else:
            cursorx = conn.execute("SELECT * FROM COURSE WHERE course_id=(?)", (course_id,))
            resultx = cursorx.fetchall()
            if len(resultx) == 0:
                self.errorDisplay.setText("Enter a Valid Course ID!")
            else:
                params = (idinput, fname, lname, passinput, course_id)
                cursorexe = conn.cursor()
                cursorexe.execute("INSERT INTO teacher VALUES (?, ?, ?, ?, ?)", params)
                conn.commit()
                self.errorDisplay.setText("Data Entered!")
        conn.close()
    def run(self):
        self.show()