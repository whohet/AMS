from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from addstudentgui import Ui_MainWindow
import sqlite3

class MainWindow(QMainWindow, Ui_MainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.addNew.clicked.connect(self.addStu)
        self.run()
    def addStu(self):
        id = self.id.toPlainText()
        password = self.password.toPlainText()
        confirmpass = self.confirmpass.toPlainText()
        fname = self.fname.toPlainText()
        lname = self.lname.toPlainText()
        t_id_1 = self.t_id_1.toPlainText()
        t_id_2 = self.t_id_2.toPlainText()
        t_id_3 = self.t_id_3.toPlainText()
        t_id_4 = self.t_id_4.toPlainText()
        t_id = [t_id_1, t_id_2, t_id_3, t_id_4]
        t_set = set(t_id)
        conn = sqlite3.connect('attendance.db')
        conn.execute('PRAGMA foreign_keys=on;')
        cursor = conn.execute("SELECT * FROM STUDENT WHERE roll_no=(?)", (id,))
        result = cursor.fetchall()
        conn.close()
        if len(result) != 0:
            self.errorDisplay.setText("Entered ID Already Exists! Enter a Unique ID to Register.")
        elif id == "":
            self.errorDisplay.setText("ID can't be NULL! Try Again by Entering a Valid ID.")
        elif password == "":
            self.errorDisplay.setText("Password Field Can't Be Empty! Try Again by Entering a Valid ID.")
        elif password != confirmpass:
            self.errorDisplay.setText("Password and Confirm Password field doesn't match. Try Again!")
        elif lname == "" or fname == "":
            self.errorDisplay.setText("Name Fields Can't Be Empty!")
        elif len(t_set) == 1 and t_id_1 == "":
            self.errorDisplay.setText("You Must Enroll in One Course!")
        else:
            flag = 1
            uniquel1 = list()
            uniquel2 = list()
            for i in range(len(t_id)):
                conn = sqlite3.connect('attendance.db')
                conn.execute('PRAGMA foreign_keys=on;')
                cursorx = conn.execute("SELECT course_id FROM TEACHER WHERE faculty_id=(?)", (t_id[i],))
                resultx = cursorx.fetchall()
                conn.close()
                if t_id[i] == "":
                    continue
                if len(resultx) == 0:
                    flag = 0
                    self.errorDisplay.setText("Enter a Valid Faculty ID!")
                    break
                if resultx[0][0] in uniquel1:
                    flag = 0
                    self.errorDisplay.setText("Enter Unique Subject's Faculty.")
                    break
                if t_id[i] in uniquel2:
                    flag = 0
                    self.errorDisplay.setText("Enter Unique Faculty IDs")
                uniquel1.append(resultx[0][0])
                uniquel2.append(t_id[i])
            if flag != 0:

                conn = sqlite3.connect('attendance.db')
                conn.execute('PRAGMA foreign_keys=on;')
                params1 = (id, fname, lname, password)
                cursorexe = conn.cursor()
                cursorexe.execute("INSERT INTO STUDENT VALUES (?, ?, ?, ?)", params1)
                conn.commit()
                conn.close()
                for i in range(len(uniquel1)):
                    conn = sqlite3.connect('attendance.db')
                    conn.execute('PRAGMA foreign_keys=on;')
                    cursor = conn.cursor()
                    params = (uniquel1[i], id, uniquel2[i])
                    cursor.execute("INSERT INTO STUDIES VALUES (?, ?, ?)", params)
                    conn.commit()
                    conn.close()
                self.errorDisplay.setText("Data Entered!")

    def run(self):
        self.show()