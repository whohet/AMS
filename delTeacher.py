from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from removeteachergui import Ui_MainWindow
import sqlite3

class MainWindow(QMainWindow, Ui_MainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.id.setHidden(True)
        self.fname.setHidden(True)
        self.lname.setHidden(True)
        self.password.setHidden(True)
        self.confirmpass.setHidden(True)
        self.id.setDisabled(True)
        self.fname.setDisabled(True)
        self.lname.setDisabled(True)
        self.password.setDisabled(True)
        self.confirmpass.setDisabled(True)
        self.errorDisplay_2.setHidden(True)
        self.addNew.setDisabled(True)
        self.addNew.setHidden(True)
        self.remove.clicked.connect(self.delete)
        self.label_1.setHidden(True)
        self.label_2.setHidden(True)
        self.label_3.setHidden(True)
        self.label_4.setHidden(True)
        self.label_5.setHidden(True)
        self.run()
    def delete(self):

        old = self.old_id.toPlainText()
        conn = sqlite3.connect('attendance.db')
        conn.execute('PRAGMA foreign_keys=on;')
        cursor = conn.execute("SELECT course_id FROM teacher WHERE faculty_id=(?)", (old,))
        result = cursor.fetchall()
        conn.close()
        if old == "":
            self.errorDisplay.setText("ID Can't Be Empty!")
        elif len(result) == 0:
            self.errorDisplay.setText("No Such ID Found!")
        else:
            self.errorDisplay.setText("")
            conn = sqlite3.connect('attendance.db')
            conn.execute('PRAGMA foreign_keys=on;')
            cursor = conn.execute("SELECT course_id FROM teacher WHERE faculty_id=(?)", (old,))
            result = cursor.fetchall()
            course_id = result[0][0]

            val = list(conn.execute("SELECT faculty_id FROM teacher WHERE course_id=(?)", (course_id,)))
            conn.close()
            if len(val) == 1:
                self.id.setHidden(False)
                self.fname.setHidden(False)
                self.lname.setHidden(False)
                self.password.setHidden(False)
                self.confirmpass.setHidden(False)
                self.id.setDisabled(False)
                self.fname.setDisabled(False)
                self.lname.setDisabled(False)
                self.password.setDisabled(False)
                self.confirmpass.setDisabled(False)
                self.errorDisplay_2.setHidden(False)
                self.addNew.setDisabled(False)
                self.addNew.setHidden(False)
                self.label_1.setHidden(False)
                self.label_2.setHidden(False)
                self.label_3.setHidden(False)
                self.label_4.setHidden(False)
                self.label_5.setHidden(False)
                self.old_id.setReadOnly(True)
                self.remove.setDisabled(True)
                self.addNew.clicked.connect(self.delete2)
            else:
                conn = sqlite3.connect('attendance.db')
                conn.execute('PRAGMA foreign_keys=on;')
                val = list(conn.execute("SELECT faculty_id FROM teacher WHERE course_id=(?) AND faculty_id!=(?)",
                                        (course_id, old,)))
                val = val[0][0]
                cursor = list(conn.execute("SELECT roll_no FROM studies WHERE faculty_id=(?)", (old,)))
                for i in cursor:
                    cor = conn.cursor()
                    params = (course_id, i[0], val)
                    cor.execute("INSERT INTO studies VALUES (?, ?, ?)", params)
                    conn.commit()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM teacher WHERE faculty_id=(?)", (old,))
                self.errorDisplay.setText("Data Updated!")
                conn.commit()
                conn.close()

    def delete2(self):
        old_id = self.old_id.toPlainText()
        conn = sqlite3.connect('attendance.db')
        conn.execute('PRAGMA foreign_keys=on;')
        cursor = conn.execute("SELECT course_id FROM teacher WHERE faculty_id=(?)", (old_id,))
        result = cursor.fetchall()
        course_id = result[0][0]
        conn.close()
        idinput = self.id.toPlainText()
        passinput = self.password.toPlainText()
        confirmpass = self.confirmpass.toPlainText()
        fname = self.fname.toPlainText()
        lname = self.lname.toPlainText()
        conn = sqlite3.connect('attendance.db')
        conn.execute('PRAGMA foreign_keys=on;')
        cursor = conn.execute("SELECT * FROM TEACHER WHERE faculty_id=(?)", (idinput,))
        result = cursor.fetchall()
        if len(result) != 0:
            self.errorDisplay.setText("Entered ID Already Exists! Enter a Unique ID to Register.")
        elif idinput == "":
            self.errorDisplay.setText("ID can't be NULL! Try Again by Entering a Valid ID.")
        elif passinput == "":
            self.errorDisplay.setText("Password Field Can't Be Empty! Try Again by Entering a Valid ID.")
        elif passinput != confirmpass:
            self.errorDisplay.setText("Password and Confirm Password field doesn't match. Try Again!")
        elif lname == "" or fname == "":
            self.errorDisplay.setText("Name Fields Can't Be Empty!")
        else:
            params = (idinput, fname, lname, passinput, course_id)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO teacher VALUES (?, ?, ?, ?, ?)", params)
            conn.commit()
            cursor = list(conn.execute("SELECT roll_no FROM studies WHERE faculty_id=(?)", (old_id,)))
            for i in cursor:
                cor = conn.cursor()
                params = (course_id, i[0], idinput)
                cor.execute("INSERT INTO studies VALUES (?, ?, ?)", params)
                conn.commit()

            conn.execute("DELETE FROM teacher WHERE faculty_id=(?)", (old_id,))
            conn.commit()
            self.errorDisplay.setText("Data Updated!")
            self.addNew.setDisabled(True)
        conn.close()
    def run(self):
        self.show()