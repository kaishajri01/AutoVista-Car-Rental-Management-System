from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from app import Ui_MainWindow
from Agence import *
import sys

class MainWindow:

    
    def __init__(self,Agence):
        self.Agence=Agence
        self.window=QMainWindow()
        self.ui=Ui_MainWindow(Agence)
        self.ui.setupUi(self.window)
        self.window.show()
        

a=Agence()
app=QtWidgets.QApplication(sys.argv)
window=MainWindow(a)
app.exec_()

#st202210