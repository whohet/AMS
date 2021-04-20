from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from popup import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.run()
    def run(self):
        self.show()