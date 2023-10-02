# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enreclient.ui'
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

        def enrecli(self):
                cin=self.lineEdit.text()
                if c_cin(cin)==False:
                        self.showDialog("CIN Invalide !",False)
                        self.lineEdit.setText("")
                        return
                if cin_existe(cin,self.Agence.ListeClient.liste)==True:
                        self.showDialog("CIN Existe Deja !",False)
                        self.lineEdit.setText("")
                        return
                nom=self.lineEdit_2.text()
                if c_nom(nom)==False:
                        self.showDialog("Nom Invalide !",False)
                        self.lineEdit_2.setText("")
                        return
                
                prenom=self.lineEdit_3.text()
                if c_nom(prenom)==False:
                        self.showDialog("Prenom Invalide !",False)
                        self.lineEdit_3.setText("")
                        return
                
                age=self.lineEdit_4.text()
                if age.isdigit()==False or int(age)<18:
                        self.showDialog("Age Invalide !",False)
                        self.lineEdit_4.setText("")
                        return
                
                adresse=self.lineEdit_5.text()
                if adresse.isdigit() or len(adresse)<4:
                        self.showDialog("Adresse Invalide !",False)
                        self.lineEdit_5.setText("")
                        return
                
                mail=self.lineEdit_6.text()
                if c_mail(mail)==False:
                        self.showDialog("Email Invalide !",False)
                        self.lineEdit_6.setText("")
                        return
                
                tlf=self.lineEdit_7.text()
                if c_tlf(tlf)==False:
                        self.showDialog("Téléphone Invalide !",False)
                        self.lineEdit_7.setText("")
                        return
                
                self.Agence.ListeClient.ajout_client(cin,nom,prenom,age,adresse,mail,tlf)
                self.showDialog("Enregistrement Terminée !",True)
                self.lineEdit.setText("");self.lineEdit_2.setText("");self.lineEdit_3.setText("");self.lineEdit_4.setText("")
                self.lineEdit_5.setText("");self.lineEdit_6.setText("");self.lineEdit_7.setText("")
                return


        def setupUi(self, Dialog):
                Dialog.setObjectName("Dialog")
                Dialog.resize(1392, 834)
                Dialog.setStyleSheet("background-color:DodgerBlue")
                self.label = QtWidgets.QLabel(Dialog)
                self.label.setGeometry(QtCore.QRect(-20, -10, 1431, 851))
                self.label.setText("")
                self.label.setPixmap(QtGui.QPixmap(":/pic/b2.jpg"))
                self.label.setScaledContents(True)
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(Dialog)
                self.label_2.setGeometry(QtCore.QRect(570, 40, 261, 81))
                font = QtGui.QFont()
                font.setFamily("Bernard MT Condensed")
                font.setPointSize(26)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("background-color:none;\n"
        "color:white")
                self.label_2.setObjectName("label_2")
                self.lineEdit = QtWidgets.QLineEdit(Dialog)
                self.lineEdit.setGeometry(QtCore.QRect(550, 140, 291, 31))
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
                self.lineEdit_2.setGeometry(QtCore.QRect(550, 210, 291, 31))
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
                self.lineEdit_3.setGeometry(QtCore.QRect(550, 280, 291, 31))
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
                self.lineEdit_4.setGeometry(QtCore.QRect(550, 350, 291, 31))
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
                self.lineEdit_5.setGeometry(QtCore.QRect(550, 420, 291, 31))
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
                self.lineEdit_6.setGeometry(QtCore.QRect(550, 490, 291, 31))
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
                self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
                self.lineEdit_7.setGeometry(QtCore.QRect(600, 560, 241, 31))
                font = QtGui.QFont()
                font.setFamily("Modern No. 20")
                font.setPointSize(14)
                self.lineEdit_7.setFont(font)
                self.lineEdit_7.setStyleSheet("QLineEdit{\n"
        "border-style: outset;\n"
        "background-color:white;\n"
        "    border-radius: 10px;\n"
        "}\n"
        "QLineEdit:focus{\n"
        "border:1.5px solid\n"
        "}")
                self.lineEdit_7.setObjectName("lineEdit_7")
                self.label_3 = QtWidgets.QLabel(Dialog)
                self.label_3.setGeometry(QtCore.QRect(540, 560, 51, 31))
                font = QtGui.QFont()
                font.setFamily("Segoe UI Variable Text Semibold")
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("background-color:none;\n"
        "color:white")
                self.label_3.setObjectName("label_3")
                self.pushButton = QtWidgets.QPushButton(Dialog)
                self.pushButton.setGeometry(QtCore.QRect(540, 680, 311, 41))
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.pushButton.setFont(font)
                self.pushButton.setStyleSheet("QPushButton{\n"
        "border-style: outset;\n"
        "background-color:Aquamarine;\n"
        "    border-radius: 10px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color:Aqua\n"
        "}")
                self.pushButton.setObjectName("pushButton")

                self.retranslateUi(Dialog)
                QtCore.QMetaObject.connectSlotsByName(Dialog)
                self.pushButton.clicked.connect(self.enrecli)

        def retranslateUi(self, Dialog):
                _translate = QtCore.QCoreApplication.translate
                Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
                self.label_2.setText(_translate("Dialog", "Enregistrement"))
                self.lineEdit.setPlaceholderText(_translate("Dialog", "C.I.N"))
                self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Nom"))
                self.lineEdit_3.setPlaceholderText(_translate("Dialog", "Prenom"))
                self.lineEdit_4.setPlaceholderText(_translate("Dialog", "Age"))
                self.lineEdit_5.setPlaceholderText(_translate("Dialog", "Adresse"))
                self.lineEdit_6.setPlaceholderText(_translate("Dialog", "Adresse@Mail"))
                self.lineEdit_7.setPlaceholderText(_translate("Dialog", "00 000 000"))
                self.label_3.setText(_translate("Dialog", "+216"))
                self.pushButton.setText(_translate("Dialog", "Save"))
import affc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
