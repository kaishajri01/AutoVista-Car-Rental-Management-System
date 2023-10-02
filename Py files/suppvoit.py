# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'suppvoit.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Controle import *

class Ui_Dialog(object):

    def __init__(self,Agence):
        self.Agence=Agence

    def showDialog(self,str,bool):
        msgBox = QMessageBox()
        if bool==False:
            msgBox.setIcon(QMessageBox.Warning)
        else:
            msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(str)
        msgBox.setWindowTitle("Advertissement")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()


    def radio1(self):
        self.lineEdit.setReadOnly(False)
        self.lineEdit_3.setReadOnly(False)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setText("")   

    def radio2(self):
        self.lineEdit.setReadOnly(True)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit.setText("")
        self.lineEdit_3.setText("")

    def radio3(self):
        self.lineEdit.setReadOnly(True)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit.setText("")
        self.lineEdit_3.setText("")


    def supprimer(self): 
            if self.radioButton.isChecked():
                p1matr=self.lineEdit.text()
                p2matr=self.lineEdit_3.text()
                matr=p1matr+" TUN "+p2matr
                if c_matricule(matr)==False:
                    self.showDialog("Matricule Invalide !",False)
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    return
                if  mat_existe(matr,self.Agence.Parc.parc)==False:
                    self.showDialog("Matricule N'existe pas !",False)
                    return
                self.Agence.Parc.supprimer_mat(matr)
                self.showDialog("Supression Terminé !",True)
                self.lineEdit.setText("")
                self.lineEdit_3.setText("")
                return

            elif self.radioButton_2.isChecked():
                marq=self.lineEdit_2.text()
                if c_marque(marq)==False:
                    self.showDialog("Marque Invalide !",False)
                    self.lineEdit_2.setText("")
                    return
                self.Agence.Parc.supprimer_marq(marq)   
                self.showDialog("Supression Terminé !",True) 
                self.lineEdit_2.setText("")

            elif self.radioButton_3.isChecked():
                self.Agence.Parc.supprimer_agee()
                self.showDialog("Supression Terminé !",True)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1392, 834)
        Dialog.setStyleSheet("background-color:DarkSlateGrey")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-80, -10, 1471, 851))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/pics/b1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(570, 40, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Bernard MT Condensed")
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:none;\n"
"color:white")
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(120, 260, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("background-color:none;\n"
"color:white")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(120, 360, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("background-color:none;\n"
"color:white")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(120, 460, 551, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("background-color:none;\n"
"color:white")
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(540, 620, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"border-style: outset;\n"
"background-color:DarkCyan;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:MediumSeaGreen\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(800, 270, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"border-style: outset;\n"
"background-color:white;\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus{\n"
"border:1.5px solid\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(800, 370, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"border-style: outset;\n"
"background-color:white;\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus{\n"
"border:1.5px solid\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(910, 270, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:none;\n"
"color:white\n"
"")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(960, 270, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"border-style: outset;\n"
"background-color:white;\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus{\n"
"border:1.5px solid\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.supprimer)
        self.radioButton.toggled.connect(self.radio1)
        self.radioButton_2.toggled.connect(self.radio2)
        self.radioButton_3.toggled.connect(self.radio3)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Suppression"))
        self.radioButton.setText(_translate("Dialog", "Supprimer  Matricule"))
        self.radioButton_2.setText(_translate("Dialog", "Supprimer  Marque"))
        self.radioButton_3.setText(_translate("Dialog", "Supprimer  voitures agées (>10 ans)"))
        self.pushButton.setText(_translate("Dialog", "Supprimer"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "000"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Marque"))
        self.label_3.setText(_translate("Dialog", "TUN"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "0000"))
import mothak3


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
