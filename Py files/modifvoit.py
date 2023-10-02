# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modifvoit.ui'
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
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_5.setReadOnly(False)

        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_3.setText("")   
        self.lineEdit_4.setText("") 
        self.lineEdit_6.setText("") 

    def radio2(self):
        self.lineEdit_3.setReadOnly(False)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_6.setReadOnly(False)

        self.lineEdit.setReadOnly(True)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit.setText("")   
        self.lineEdit_2.setText("") 
        self.lineEdit_5.setText("")  

    def modifier(self):
        if self.radioButton.isChecked():
                p1matr=self.lineEdit.text()
                p2matr=self.lineEdit_2.text()
                matr=p1matr+" TUN "+p2matr
                coul=self.lineEdit_5.text()
                if c_matricule(matr)==False:
                    self.showDialog("Matricule Invalide !",False)
                    self.lineEdit.setText("")
                    self.lineEdit_2.setText("")
                    self.lineEdit_5.setText("")
                    return
                if  mat_existe(matr,self.Agence.Parc.parc)==False:
                    self.showDialog("Matricule N'existe pas !",False)
                    self.lineEdit.setText("")
                    self.lineEdit_2.setText("")
                    self.lineEdit_5.setText("")
                    return
                if c_couleur(coul)==False:
                    self.showDialog("Couleur Invalide !",False)
                    self.lineEdit.setText("")
                    self.lineEdit_2.setText("")
                    self.lineEdit_5.setText("")
                    return

                self.Agence.Parc.modif_couleur_voit(matr,coul)
                self.showDialog("Modification Terminé !",True)
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_5.setText("")
                return

        if self.radioButton_2.isChecked():
                p1matr=self.lineEdit_3.text()
                p2matr=self.lineEdit_4.text()
                matr=p1matr+" TUN "+p2matr
                pri=self.lineEdit_6.text()
                if c_matricule(matr)==False:
                    self.showDialog("Matricule Invalide !",False)
                    self.lineEdit_3.setText("")
                    self.lineEdit_4.setText("")
                    self.lineEdit_6.setText("")
                    return
                if  mat_existe(matr,self.Agence.Parc.parc)==False:
                    self.showDialog("Matricule N'existe pas !",False)
                    self.lineEdit_3.setText("")
                    self.lineEdit_4.setText("")
                    self.lineEdit_6.setText("")
                    return
                if c_prix(pri)==False:
                    self.showDialog("Prix Invalide !",False)
                    self.lineEdit_3.setText("")
                    self.lineEdit_4.setText("")
                    self.lineEdit_6.setText("")
                    return

                self.Agence.Parc.modif_prix_voit(matr,pri)
                self.showDialog("Modification Terminé !",True)
                self.lineEdit_3.setText("")
                self.lineEdit_4.setText("")
                self.lineEdit_6.setText("")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1392, 835)
        Dialog.setStyleSheet("background-color:DarkSlateGrey")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, -30, 1401, 861))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/pics/b1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(580, 60, 371, 61))
        font = QtGui.QFont()
        font.setFamily("Bernard MT Condensed")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:none;\n"
"color:white")
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(140, 280, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("background-color:none;\n"
"color:white")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(140, 430, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("background-color:none;\n"
"color:white")
        self.radioButton_2.setObjectName("radioButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(540, 280, 81, 31))
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
        self.lineEdit_2.setGeometry(QtCore.QRect(690, 280, 151, 31))
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
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(540, 430, 81, 31))
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
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(690, 430, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(14)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"border-style: outset;\n"
"background-color:white;\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus{\n"
"border:1.5px solid\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(1030, 280, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(14)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
"border-style: outset;\n"
"background-color:white;\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus{\n"
"border:1.5px solid\n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(1030, 430, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(14)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("QLineEdit{\n"
"border-style: outset;\n"
"background-color:white;\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus{\n"
"border:1.5px solid\n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(560, 640, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
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
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(634, 280, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:none;\n"
"color:white")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(630, 430, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:none;\n"
"color:white")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.modifier)
        self.radioButton.toggled.connect(self.radio1)
        self.radioButton_2.toggled.connect(self.radio2)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Modification"))
        self.radioButton.setText(_translate("Dialog", "Modifier Couleur"))
        self.radioButton_2.setText(_translate("Dialog", "Modifier Prix"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "000"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "0000"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "000"))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "0000"))
        self.lineEdit_5.setPlaceholderText(_translate("Dialog", "Nouvelle Couleur"))
        self.lineEdit_6.setPlaceholderText(_translate("Dialog", "Nouveau Prix"))
        self.pushButton.setText(_translate("Dialog", "Modify"))
        self.label_3.setText(_translate("Dialog", "TUN"))
        self.label_4.setText(_translate("Dialog", "TUN"))
import mothak4
import mothak5


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())