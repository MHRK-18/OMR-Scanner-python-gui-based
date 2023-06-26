# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MAIN2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from SDETAILS import *
from OMRDETAILS import *
from SCANOMR import *
from ERESULTS import *
from SRESULTS import *
from VIEWSTU import *
from VIEWOMR import *
from CHANGE import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(501, 450)
        Dialog.setStyleSheet("QDialog{\n"
"background-image: url(:/newPrefix/mbg1.jpg);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:lightgrey;\n"
"color:black;\n"
"}")
        self.p2 = QtWidgets.QPushButton(Dialog)
        self.p2.setGeometry(QtCore.QRect(20, 160, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p2.setFont(font)
        self.p2.setObjectName("p2")
        self.p4 = QtWidgets.QPushButton(Dialog)
        self.p4.setGeometry(QtCore.QRect(20, 220, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p4.setFont(font)
        self.p4.setObjectName("p4")
        self.p5 = QtWidgets.QPushButton(Dialog)
        self.p5.setGeometry(QtCore.QRect(250, 220, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p5.setFont(font)
        self.p5.setObjectName("p5")
        self.p6 = QtWidgets.QPushButton(Dialog)
        self.p6.setGeometry(QtCore.QRect(250, 100, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p6.setFont(font)
        self.p6.setObjectName("p6")
        self.p3 = QtWidgets.QPushButton(Dialog)
        self.p3.setGeometry(QtCore.QRect(130, 290, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p3.setFont(font)
        self.p3.setStyleSheet("\n"
"QPushButton{\n"
"background-color:lightgray;\n"
"color:black;\n"
"\n"
"border-style:solid;\n"
"border-color:brown;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:crimson;\n"
"\n"
"}")
        self.p3.setObjectName("p3")
        self.p1 = QtWidgets.QPushButton(Dialog)
        self.p1.setGeometry(QtCore.QRect(20, 100, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p1.setFont(font)
        self.p1.setObjectName("p1")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 30, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color:black;")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.p7 = QtWidgets.QPushButton(Dialog)
        self.p7.setGeometry(QtCore.QRect(250, 160, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p7.setFont(font)
        self.p7.setObjectName("p7")
        self.p8 = QtWidgets.QPushButton(Dialog)
        self.p8.setGeometry(QtCore.QRect(10, 390, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.p8.setFont(font)
        self.p8.setStyleSheet("QPushButton{\n"
"color:black;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:lightgrey;\n"
"color:black;\n"
"}")
        self.p8.setObjectName("p8")
        self.p9 = QtWidgets.QPushButton(Dialog)
        self.p9.setGeometry(QtCore.QRect(250, 390, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p9.setFont(font)
        self.p9.setStyleSheet("\n"
"QPushButton{\n"
"color:black;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:red;\n"
"color:black;\n"
"}")
        self.p9.setObjectName("p9")

        
        self.p1.clicked.connect(self.student)
        self.p2.clicked.connect(self.eomr)
        self.p3.clicked.connect(self.SCANOMR)
        self.p4.clicked.connect(self.eresult)
        self.p5.clicked.connect(self.sresult)
        self.p6.clicked.connect(self.sview)
        self.p7.clicked.connect(self.eview)
        self.p8.clicked.connect(self.change)
        self.p9.clicked.connect(Dialog.accept)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.p2.setText(_translate("Dialog", "Enter OMR Sheet Details"))
        self.p4.setText(_translate("Dialog", "Fetch Exam Results"))
        self.p5.setText(_translate("Dialog", "Fetch Student Results"))
        self.p6.setText(_translate("Dialog", "View Student Details"))
        self.p3.setText(_translate("Dialog", "Scan OMR Sheets"))
        self.p1.setText(_translate("Dialog", "Enter Student Details"))
        self.label.setText(_translate("Dialog", "Welcome"))
        self.p7.setText(_translate("Dialog", "View OMR Sheet Details"))
        self.p8.setText(_translate("Dialog", "Change Password"))
        self.p9.setText(_translate("Dialog", "Logout"))
        
    def student(self):
        from SDETAILS import Ui_Dialog
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        ret=Dialog.exec()

    def eomr(self):
        from OMRDETAILS import Ui_Dialog
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        ret=Dialog.exec()

    def SCANOMR(self):
        from SCANOMR import Ui_Dialog
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        ret=Dialog.exec()

    def eresult(self):
        from ERESULTS import Ui_Dialog
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        ret=Dialog.exec()

    def sresult(self):
        from SRESULTS import Ui_Dialog
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        ret=Dialog.exec()

    def sview(self):
        from VIEWSTU import Ui_Dialog
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        ret=Dialog.exec()

    def eview(self):
        from VIEWOMR import Ui_Dialog
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        ret=Dialog.exec()

    def change(self):
        from CHANGE import Ui_cp
        cp = QtWidgets.QDialog()
        ui = Ui_cp()
        ui.setupUi(cp)
        ret=cp.exec()

    

import mbg1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
