from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from teacherlogingui import Ui_MainWindow
import sqlite3
from datetime import date


class MainWindow(QMainWindow, Ui_MainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, faculty_id, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        conn = sqlite3.connect('attendance.db')
        conn.execute('PRAGMA foreign_keys=on;')
        course_id = list(conn.execute("SELECT course_id FROM teacher WHERE faculty_id=(?)", (faculty_id,)))
        coursename = list(conn.execute("SELECT course_name FROM course WHERE course_id=(?)", (course_id[0][0],)))
        self.course_id = course_id[0][0]
        self.coursename = coursename[0][0]
        self.faculty_id = faculty_id
        conn.close()
        self.title.setText("Attendance Sheet of " + self.course_id + " " + self.coursename)
        self.i = 0
        self.curr_roll_no = '0'
        self.showhide(True)
        self.start.clicked.connect(self.attendance)
        self.run()

    def attendance(self):
        self.i = 0
        self.showhide(False)
        self.start.setDisabled(True)
        self.start.setHidden(True)
        conn = sqlite3.connect('attendance.db')
        conn.execute('PRAGMA foreign_keys=on;')
        cursorx = conn.execute("SELECT * FROM STUDIES WHERE faculty_id=(?)", (self.faculty_id,))
        result = cursorx.fetchall()
        if len(result) == 0:
            self.errorDisplay.setText("Looks Like No Student Has Enrolled In Your Class Yet!")
            self.showhide(True)
            conn.close()
        else:
            cursor = list(conn.execute("SELECT * FROM studies INNER JOIN student ON studies.roll_no=student.roll_no WHERE "
                                   "faculty_id=(?)", (self.faculty_id,)))
            conn.close()
            self.curr_roll_no = cursor[self.i][1]
            fname = cursor[self.i][4]
            lname = cursor[self.i][5]
            self.id.setText(self.curr_roll_no)
            self.name.setText(fname + " " + lname)
            self.next.clicked.connect(self.take)

    def take(self):
        if self.absent.isChecked() and self.present.isChecked():
            self.errorDisplay.setText("Select either of Absent or Present!")
        elif not (self.absent.isChecked() or self.present.isChecked()):
            self.errorDisplay.setText("Select one of either Absent or Present!")
        else:
            status = 'A'
            if self.present.isChecked():
                status = 'P'
            params = (self.curr_roll_no, date.today(), status, self.course_id, self.faculty_id)
            conn = sqlite3.connect('attendance.db')
            conn.execute('PRAGMA foreign_keys=on;')
            conn.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?)", params)
            cursor = list(
                conn.execute("SELECT * FROM studies INNER JOIN student ON studies.roll_no=student.roll_no WHERE "
                             "faculty_id=(?)", (self.faculty_id,)))
            conn.commit()
            conn.close()
            self.errorDisplay.setText("")
            self.i += 1
            if self.i < len(cursor):
                fname = cursor[self.i][4]
                lname = cursor[self.i][5]
                self.curr_roll_no = cursor[self.i][1]
                self.id.setText(self.curr_roll_no)
                self.name.setText(fname + " " + lname)
            else:
                self.errorDisplay.setText("Done Taking Attendance!")
                self.showhide(True)
            self.absent.setChecked(False)
            self.present.setChecked(False)

    def showhide(self, ok):

        self.label.setHidden(ok)
        self.label_2.setHidden(ok)
        self.label_3.setHidden(ok)
        self.id.setHidden(ok)
        self.name.setHidden(ok)
        self.absent.setDisabled(ok)
        self.absent.setHidden(ok)
        self.present.setHidden(ok)
        self.present.setDisabled(ok)
        self.next.setDisabled(ok)
        self.next.setHidden(ok)

    def run(self):
        self.show()
