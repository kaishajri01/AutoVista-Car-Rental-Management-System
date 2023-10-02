from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Controle import *
from Main import *

def __init__(self):
        self.window=QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()