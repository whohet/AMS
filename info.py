from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from infogui import Ui_MainWindow
import sqlite3


class MainWindow(QMainWindow, Ui_MainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.infoDisplay()
        self.run()
    def infoDisplay(self):
        conn = sqlite3.connect('attendance.db')
        cursor = conn.execute("SELECT course_id, course_name FROM COURSE")
        stringOut = "{}{}".format("Course ID".ljust(20), "Course Name".ljust(20))
        for row in cursor:
            s = "{}{}".format(row[0].ljust(20), row[1].ljust(20))
            stringOut = stringOut + '\n' + s
        self.course_details.setText(stringOut)
        conn.close()
        conn = sqlite3.connect('attendance.db')
        cursor = conn.execute("SELECT ffname, flname, course_id FROM TEACHER")
        stringOut = "{}{}{}".format("First Name".ljust(20), "Last Name".ljust(20), "Course ID".ljust(20))
        for row in cursor:
            s = "{}{}{}".format(row[0].ljust(20), row[1].ljust(20), row[2].ljust(20))
            stringOut = stringOut + '\n' + s
        self.teacher_details.setText(stringOut)
        conn.close()
    def run(self):
        self.show()


