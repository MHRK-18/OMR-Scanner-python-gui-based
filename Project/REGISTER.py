# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'REGISTER.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import mbg2

from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 450)
        Dialog.setStyleSheet("QDialog{\n"
"background-image: url(:/newPrefix/mbg2.jpg);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:darkgrey;\n"
"color:white;\n"
"}\n"
"")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 30, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:lightpink;\n"
"")
        self.label.setObjectName("label")
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setGeometry(QtCore.QRect(220, 100, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.mail = QtWidgets.QLineEdit(Dialog)
        self.mail.setGeometry(QtCore.QRect(220, 150, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mail.setFont(font)
        self.mail.setObjectName("mail")
        self.phone = QtWidgets.QLineEdit(Dialog)
        self.phone.setGeometry(QtCore.QRect(220, 200, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.phone.setFont(font)
        self.phone.setObjectName("phone")
        self.uid1 = QtWidgets.QLineEdit(Dialog)
        self.uid1.setGeometry(QtCore.QRect(220, 250, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.uid1.setFont(font)
        self.uid1.setObjectName("uid1")
        self.pwd1 = QtWidgets.QLineEdit(Dialog)
        self.pwd1.setGeometry(QtCore.QRect(220, 300, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pwd1.setFont(font)
        self.pwd1.setObjectName("pwd1")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 200, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 250, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(60, 300, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.reg2 = QtWidgets.QPushButton(Dialog)
        self.reg2.setGeometry(QtCore.QRect(70, 360, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.reg2.setFont(font)
        self.reg2.setObjectName("reg2")
        self.exit2 = QtWidgets.QPushButton(Dialog)
        self.exit2.setGeometry(QtCore.QRect(310, 360, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exit2.setFont(font)
        self.exit2.setObjectName("exit2")
        
        self.reg2.clicked.connect(self.register)

        
        self.exit2.clicked.connect(Dialog.accept)
        self.hide=Dialog.accept
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "     Register"))
        self.label_2.setText(_translate("Dialog", "Name"))
        self.label_3.setText(_translate("Dialog", "Email Id"))
        self.label_4.setText(_translate("Dialog", "Phone Number"))
        self.label_5.setText(_translate("Dialog", "Username"))
        self.label_6.setText(_translate("Dialog", "Password"))
        self.reg2.setText(_translate("Dialog", "Register"))
        self.exit2.setText(_translate("Dialog", "Exit"))

    def register(self):
        Dialog=QtWidgets.QMessageBox()
        Name=self.name.text()
        Email=self.mail.text()
        Phone=self.phone.text()
        Username=self.uid1.text()
        Password=self.pwd1.text()
        conn = sqlite3.connect('EXAMOMR.db')
        try:
            if(Name!="" and Email!="" and Phone!="" and Username!="" and Password!=""):
                cur=conn.execute("INSERT INTO REGISTER (Name,Email,Phone,Username,Password) VALUES ('"+str(Name)+"','"+str(Email)+"','"+Phone+"','"+str(Username)+"','"+str(Password)+"');")
                conn.commit()
                Dialog.setWindowTitle("Saved")
                Dialog.setIcon(QtWidgets.QMessageBox.Information)
                Dialog.setText("Registration Successful")
                ret=Dialog.exec()
                self.hide()
                self.clear()
              
            else:
                conn.rollback()
                Dialog.setWindowTitle("Invalid")
                Dialog.setIcon(QtWidgets.QMessageBox.Warning)
                Dialog.setText("Enter all the Details")
                ret=Dialog.exec()
                self.clear()
        except:
                Dialog.setWindowTitle("Invalid")
                Dialog.setIcon(QtWidgets.QMessageBox.Critical)
                Dialog.setText("Username already exists")
                ret=Dialog.exec()
            

    def clear(self):
        self.name.setText("")
        self.mail.setText("")
        self.phone.setText("")
        self.uid1.setText("")
        self.pwd1.setText("")

if __name__ == "__main__":
    import sys
    
    conn = sqlite3.connect('EXAMOMR.db')
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
