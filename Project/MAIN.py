# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MAIN.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import mbg1

from LOGIN import *
from REGISTER import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 450)
        MainWindow.setStyleSheet("QWidget{\n"
"    background-image: url(:/newPrefix/mbg1.jpg);\n"
"}\n"
"QPushButton{\n"
"background:none;\n"
"}\n"
"\n"
"QLabel{\n"
"background:none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color:lightpink;\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 80, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(190, 170, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.login.setFont(font)
        self.login.setObjectName("login")
        self.reg = QtWidgets.QPushButton(self.centralwidget)
        self.reg.setGeometry(QtCore.QRect(190, 310, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.reg.setFont(font)
        self.reg.setObjectName("reg")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 250, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.login.clicked.connect(self.openlogin)
        self.reg.clicked.connect(self.openregister)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "OMR Exam Scanner"))
        self.login.setText(_translate("MainWindow", "Login"))
        self.reg.setText(_translate("MainWindow", "Register"))
        self.label_2.setText(_translate("MainWindow", "OR"))
#Importing Login Dialog and opening it when Login button is clicked
    def openlogin(self):
        from LOGIN import Ui_Login
        Login = QtWidgets.QDialog()
        ui = Ui_Login()
        ui.setupUi(Login)
        ret=Login.exec()

#Importing Register Dialog and opening it when Register button is clicked        
    def openregister(self):
        from REGISTER import Ui_Dialog
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        ret=Dialog.exec()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
