# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SD.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


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
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 30, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 260, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.branch = QtWidgets.QComboBox(Dialog)
        self.branch.setGeometry(QtCore.QRect(210, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.branch.setFont(font)
        self.branch.setObjectName("branch")
        self.branch.addItem("")
        self.branch.addItem("")
        self.branch.addItem("")
        self.branch.addItem("")
        self.branch.addItem("")
        self.sid = QtWidgets.QLineEdit(Dialog)
        self.sid.setGeometry(QtCore.QRect(210, 110, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sid.setFont(font)
        self.sid.setObjectName("sid")
        self.n1 = QtWidgets.QLineEdit(Dialog)
        self.n1.setGeometry(QtCore.QRect(210, 160, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.n1.setFont(font)
        self.n1.setObjectName("n1")
        self.year = QtWidgets.QComboBox(Dialog)
        self.year.setGeometry(QtCore.QRect(210, 260, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.year.setFont(font)
        self.year.setObjectName("year")
        self.year.addItem("")
        self.year.addItem("")
        self.year.addItem("")
        self.year.addItem("")
        self.s1 = QtWidgets.QPushButton(Dialog)
        self.s1.setGeometry(QtCore.QRect(80, 340, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.s1.setFont(font)
        self.s1.setObjectName("s1")
        self.e1 = QtWidgets.QPushButton(Dialog)
        self.e1.setGeometry(QtCore.QRect(280, 340, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.e1.setFont(font)
        self.e1.setObjectName("e1")

        self.s1.clicked.connect(self.enter)
        self.e1.clicked.connect(Dialog.accept)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter Student Details"))
        self.label_2.setText(_translate("Dialog", "Student Id"))
        self.label_3.setText(_translate("Dialog", "Name"))
        self.label_4.setText(_translate("Dialog", "Branch"))
        self.label_5.setText(_translate("Dialog", "Year"))
        self.branch.setItemText(0, _translate("Dialog", "CSE"))
        self.branch.setItemText(1, _translate("Dialog", "IT"))
        self.branch.setItemText(2, _translate("Dialog", "ECE"))
        self.branch.setItemText(3, _translate("Dialog", "CE"))
        self.branch.setItemText(4, _translate("Dialog", "ME"))
        self.year.setItemText(0, _translate("Dialog", "I"))
        self.year.setItemText(1, _translate("Dialog", "II"))
        self.year.setItemText(2, _translate("Dialog", "III"))
        self.year.setItemText(3, _translate("Dialog", "IV"))
        self.s1.setText(_translate("Dialog", "Save"))
        self.e1.setText(_translate("Dialog", "Exit"))

    def enter(self):
        Dialog=QtWidgets.QMessageBox()
        conn = sqlite3.connect('EXAMOMR.db')
        Id=self.sid.text()
        Name=self.n1.text()
        Branch=self.branch.currentText()
        Year=self.year.currentText()
        try:
            if Id!="" and Name!="" and Branch!="" and Year!="":
                cur=conn.execute("INSERT INTO STUDENT (Studentid,Name,Branch,Year) VALUES ('"+str(Id)+"','"+str(Name)+"','"+str(Branch)+"','"+str(Year)+"');")
                Dialog.setIcon(QtWidgets.QMessageBox.Information)
                Dialog.setText("Saved Successfully")
                ret=Dialog.exec()
                self.clear()
                conn.commit()

            else:
                Dialog.setWindowTitle("Invalid")
                Dialog.setIcon(QtWidgets.QMessageBox.Warning)
                Dialog.setText("Please Enter all Details")
                ret=Dialog.exec()
                
        except:
            Dialog.setWindowTitle("Invalid")
            Dialog.setIcon(QtWidgets.QMessageBox.Warning)
            Dialog.setText("StudentId already exists")
            ret=Dialog.exec()
            self.clear()

    def clear(self):
        self.sid.setText("")
        self.n1.setText("")
        self.branch.setCurrentIndex(0)
        self.year.setCurrentIndex(0)

                
import bg1

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
