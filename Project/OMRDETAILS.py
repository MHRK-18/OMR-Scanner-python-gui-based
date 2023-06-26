# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ED.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import bg1
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 450)
        Dialog.setStyleSheet("QDialog{\n"
"background-image: url(:/newPrefix/bg1.jpg);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:lightgrey;\n"
"color:black;\n"
"}\n"
"")
        self.ec1 = QtWidgets.QLineEdit(Dialog)
        self.ec1.setGeometry(QtCore.QRect(190, 80, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ec1.setFont(font)
        self.ec1.setObjectName("ec1")
        self.ed = QtWidgets.QLineEdit(Dialog)
        self.ed.setGeometry(QtCore.QRect(190, 130, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ed.setFont(font)
        self.ed.setObjectName("ed")
        self.op = QtWidgets.QLineEdit(Dialog)
        self.op.setGeometry(QtCore.QRect(190, 230, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.op.setFont(font)
        self.op.setObjectName("op")
        self.qa = QtWidgets.QLineEdit(Dialog)
        self.qa.setGeometry(QtCore.QRect(190, 280, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.qa.setFont(font)
        self.qa.setObjectName("qa")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 80, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 230, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 280, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.e0 = QtWidgets.QPushButton(Dialog)
        self.e0.setGeometry(QtCore.QRect(430, 280, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.e0.setFont(font)
        self.e0.setStyleSheet("\n"
"QPushButton{\n"
"color:black;\n"
"background-color:lightpink;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:crimson;\n"
"color:white;\n"
"}")
        self.e0.setObjectName("e0")
        self.s2 = QtWidgets.QPushButton(Dialog)
        self.s2.setGeometry(QtCore.QRect(90, 350, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.s2.setFont(font)
        self.s2.setObjectName("s2")
        self.e2 = QtWidgets.QPushButton(Dialog)
        self.e2.setGeometry(QtCore.QRect(260, 350, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.e2.setFont(font)
        self.e2.setObjectName("e2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(70, 20, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 180, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.q = QtWidgets.QLineEdit(Dialog)
        self.q.setGeometry(QtCore.QRect(190, 180, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.q.setFont(font)
        self.q.setObjectName("q")

        self.s2.clicked.connect(self.enter)
        self.e2.clicked.connect(Dialog.accept)
        self.e0.clicked.connect(self.help)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter Exam Code"))
        self.label_2.setText(_translate("Dialog", "Enter Exam Date"))
        self.label_3.setText(_translate("Dialog", "No.of Options"))
        self.label_4.setText(_translate("Dialog", "Enter the Q/A Key"))
        self.e0.setText(_translate("Dialog", "Help"))
        self.s2.setText(_translate("Dialog", "Save"))
        self.e2.setText(_translate("Dialog", "Exit"))
        self.label_5.setText(_translate("Dialog", "Exam and OMR Sheet Details"))
        self.label_6.setText(_translate("Dialog", "No.of Questions"))

    def enter(self):
        import datetime
        conn = sqlite3.connect('EXAMOMR.db')
        Dialog=QtWidgets.QMessageBox()
        ec=self.ec1.text()
        date=self.ed.text()
        nq=self.q.text()
        np=self.op.text()
        qak=self.qa.text()
        try:
            if (ec!="" and date!="" and nq!="" and np!="" and qak!=""):
                cur=conn.execute("INSERT INTO OMRDETAILS (Examcode,Edate,Questions,Options,QAkey) VALUES ('"+str(ec)+"','"+date+"','"+nq+"','"+np+"','"+str(qak)+"');")
                conn.commit()
                Dialog.setWindowTitle("Saved")
                Dialog.setIcon(QtWidgets.QMessageBox.Information)
                Dialog.setText("Saved Successfully")
                ret=Dialog.exec()
                self.clear()
            else:
                conn.rollback()
                Dialog.setWindowTitle("Invalid")
                Dialog.setIcon(QtWidgets.QMessageBox.Warning)
                Dialog.setText("Add all the Details")
                ret=Dialog.exec()
                self.clear()
        except:
            Dialog.setWindowTitle("Invalid")
            Dialog.setIcon(QtWidgets.QMessageBox.Warning)
            Dialog.setText("Exam code already exists")
            ret=Dialog.exec()
            self.clear()

    def clear(self):
        self.ec1.setText("")
        self.ed.setText("")
        self.q.setText("")
        self.op.setText("")
        self.qa.setText("")

    def help(self):
        Dialog=QtWidgets.QMessageBox()
        Dialog.setWindowTitle("Help")
        Dialog.setIcon(QtWidgets.QMessageBox.Information)
        Dialog.setText("""Please Enter the Question Answer key starting from 0 format Q:A,Q:A, ...
Example:- 0:1,1:2 specifies 1st answer as B(1) and 2nd answer as C(2)
Seperate Q and A using ':' and Q/A key pair using ','.
                       """)
        ret=Dialog.exec()
        
        



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
