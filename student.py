from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from studentlogingui import Ui_MainWindow
import sqlite3
import popupcode


class MainWindow(QMainWindow, Ui_MainWindow):
    switch_window = QtCore.pyqtSignal()
    def __init__(self, roll_no, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.studentDisplay(roll_no)

    def studentDisplay(self, roll_no):
        conn = sqlite3.connect('attendance.db')
        conn.execute('PRAGMA foreign_keys=on;')
        name=list(conn.execute("SELECT SFNAME,SLNAME FROM STUDENT WHERE roll_no=(?)",(roll_no,)))
        self.rollno.setText(roll_no)
        self.name.setText(name[0][0]+" "+name[0][1])
        cursor = conn.execute("SELECT * FROM ATTENDANCE WHERE roll_no=(?)", (roll_no,))
        result = cursor.fetchall()
        if len(result)==0:
            self.popup=popupcode.MainWindow()
        else:
            self.run()
            course_id = set(conn.execute("SELECT course_id FROM ATTENDANCE WHERE roll_no=(?)", (roll_no,)))
            course_id = list(course_id)
            course_id.sort()
            row1=list()
            for subjects in course_id:
                total_classes = list(conn.execute("SELECT count(*) FROM ATTENDANCE WHERE roll_no=(?) AND course_id=(?)",
                                                  (roll_no, subjects[0],)))
                total_classes = total_classes[0][0]

                Attended_classes = list(
                    conn.execute("SELECT count(*) FROM ATTENDANCE WHERE roll_no=(?) AND course_id=(?) "
                                 "AND status=(?)", (roll_no, subjects[0], 'P')))
                Attended_classes = Attended_classes[0][0]
                percentage = Attended_classes * 100 / total_classes
                row = list(
                    conn.execute("SELECT * FROM (SELECT * FROM ATTENDANCE INNER JOIN COURSE ON "
                                 "ATTENDANCE.course_id=COURSE.course_id WHERE roll_no=(?)) WHERE course_id=(?)",
                                 (roll_no, subjects[0],)))
                # print(row)
                percentage = "{:.2f}%".format(percentage)
                #print("{}{}{}{}".format(subjects[0].ljust(19), row[0][6].ljust(20), row[0][4].ljust(17), percentage))
                row1.append([subjects[0], row[0][6], row[0][4], percentage])
                conn.commit()

            for row1x in row1:
                tableRowNumber = self.primary.rowCount()
                self.primary.setRowCount(tableRowNumber + 1)
                col = 0
                for item in row1x:
                    cell = QTableWidgetItem(str(item))
                    self.primary.setItem(tableRowNumber, col, cell)
                    col += 1
            rows = list(
                conn.execute("SELECT * FROM ATTENDANCE INNER JOIN COURSE ON "
                             "ATTENDANCE.course_id=COURSE.course_id WHERE roll_no=(?)", (roll_no,)))

            row1.clear()
            for row in rows:
                #print("{}{}{}{}{}".format(row[3].ljust(19), row[6].ljust(20), row[4].ljust(17), row[2].ljust(14), row[1]))
                row1.append([row[3], row[6],row[4], row[1], row[2]])
            row1.sort()

            for row1x in row1:
                tableRowNumber = self.secondary.rowCount()
                self.secondary.setRowCount(tableRowNumber + 1)
                col = 0
                for item in row1x:
                    cell = QTableWidgetItem(str(item))
                    self.secondary.setItem(tableRowNumber, col, cell)
                    col += 1
        conn.close()
    def run(self):
        self.show()


