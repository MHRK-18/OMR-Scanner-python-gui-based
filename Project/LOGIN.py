# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LOGIN.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import bg2
from HOME import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(500, 450)
        Login.setStyleSheet("QDialog{\n"
"background-image: url(:/newPrefix/mbg2.jpg);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:darkgrey;\n"
"color:white;\n"
"}\n"
"")
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(150, 70, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: lightpink;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(90, 170, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Login)
        self.label_3.setGeometry(QtCore.QRect(90, 230, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.uid = QtWidgets.QLineEdit(Login)
        self.uid.setGeometry(QtCore.QRect(212, 169, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.uid.setFont(font)
        self.uid.setObjectName("uid")
        self.pwd = QtWidgets.QLineEdit(Login)
        self.pwd.setGeometry(QtCore.QRect(210, 230, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pwd.setFont(font)
        self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd.setObjectName("pwd")
        self.login1 = QtWidgets.QPushButton(Login)
        self.login1.setGeometry(QtCore.QRect(110, 300, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.login1.setFont(font)
        self.login1.setObjectName("login1")
        self.exit1 = QtWidgets.QPushButton(Login)
        self.exit1.setGeometry(QtCore.QRect(270, 300, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.exit1.setFont(font)
        self.exit1.setObjectName("exit1")

        self.hide=Login.accept
        
        self.login1.clicked.connect(self.login)

        self.exit1.clicked.connect(Login.accept)
        
        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Dialog"))
        self.label.setText(_translate("Login", "        Login"))
        self.label_2.setText(_translate("Login", "Username"))
        self.label_3.setText(_translate("Login", "Password"))
        self.login1.setText(_translate("Login", "Login"))
        self.exit1.setText(_translate("Login", "Exit"))

    def login(self):
        import sqlite3

        Dialog=QtWidgets.QMessageBox()
        uname=self.uid.text()
        passwd=self.pwd.text()
        conn = sqlite3.connect('EXAMOMR.db')
        sql="Select * from REGISTER where Username='"+uname+"';"
        cur=conn.execute(sql)
        row=cur.fetchone()
        if row is not None:
            uid1=row[3]
            pwd1=row[4]
            if uid1==uname and passwd==pwd1:
                self.hide()
                from HOME import Ui_Dialog
                Dialog = QtWidgets.QDialog()
                ui = Ui_Dialog()
                ui.setupUi(Dialog)
                ret=Dialog.exec()

                
            elif uid1==uname and passwd!=pwd1:
                conn.rollback()
                Dialog.setWindowTitle("Invalid")
                Dialog.setIcon(QtWidgets.QMessageBox.Warning)
                Dialog.setText("Invalid Username or Password")
                ret=Dialog.exec()
                self.clear()

        else:
            Dialog.setWindowTitle("Invalid")
            Dialog.setIcon(QtWidgets.QMessageBox.Warning)
            Dialog.setText("Invalid Username or Password")
            ret=Dialog.exec()
            self.clear()              


    def clear(self):
        self.uid.setText("")
        self.pwd.setText("")

        
import mbg2


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
