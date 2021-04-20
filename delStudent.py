from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from removestudentgui import Ui_MainWindow
import sqlite3

class MainWindow(QMainWindow, Ui_MainWindow):
    switch_window = QtCore.pyqtSignal()
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.remove.clicked.connect(self.delete)
        self.run()
    def delete(self):
        id=self.id.toPlainText()
        conn = sqlite3.connect('attendance.db')
        conn.execute('PRAGMA foreign_keys=on;')
        if id=="":
            self.errorDisplay.setText("ID can't be Empty!")
        else:
            cursor = conn.execute("SELECT * FROM STUDENT WHERE roll_no=(?)", (id,))
            result = cursor.fetchall()
            if len(result)==0:
                self.errorDisplay.setText("No Such ID Found! Enter a Valid ID")
            else:
                conn.execute("DELETE FROM STUDENT WHERE roll_no=(?)", (id,))
                conn.commit()
                self.errorDisplay.setText("Data Removed!")
        conn.close()
    def run(self):
        self.show()



