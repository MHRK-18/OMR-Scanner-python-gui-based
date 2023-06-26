# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VS1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import bg3
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 500)
        Dialog.setStyleSheet("QDialog{\n"
"    background-image: url(:/newPrefix/bg3.jpg);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:lightgrey;\n"
"color:black;\n"
"}\n"
"")

        self.ee1 = QtWidgets.QPushButton(Dialog)
        self.ee1.setGeometry(QtCore.QRect(280, 140, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ee1.setFont(font)
        self.ee1.setObjectName("ee1")
        self.t3 = QtWidgets.QTableWidget(Dialog)
        self.t3.setGeometry(QtCore.QRect(30, 210, 441, 231))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.t3.setFont(font)
        self.t3.setRowCount(200)
        self.t3.setObjectName("t3")
        
        self.t3.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.t3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.t3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.t3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.t3.setHorizontalHeaderItem(3, item)

        conn = sqlite3.connect('EXAMOMR.db')
        sql="Select * from STUDENT ORDER BY Year,Branch ASC;"
        result=conn.execute(sql)
        self.t3.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.t3.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.t3.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 20, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.vs = QtWidgets.QLineEdit(Dialog)
        self.vs.setGeometry(QtCore.QRect(240, 80, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vs.setFont(font)
        self.vs.setObjectName("vs")
        self.ss = QtWidgets.QPushButton(Dialog)
        self.ss.setGeometry(QtCore.QRect(100, 140, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ss.setFont(font)
        self.ss.setObjectName("ss")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(530, 20, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.vs4 = QtWidgets.QComboBox(Dialog)
        self.vs4.setGeometry(QtCore.QRect(620, 230, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.vs4.setFont(font)
        self.vs4.setObjectName("vs4")
        self.vs4.addItem("")
        self.vs4.addItem("")
        self.vs4.addItem("")
        self.vs4.addItem("")
        self.vs2 = QtWidgets.QLineEdit(Dialog)
        self.vs2.setGeometry(QtCore.QRect(620, 130, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vs2.setFont(font)
        self.vs2.setObjectName("vs2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(530, 230, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.vs3 = QtWidgets.QComboBox(Dialog)
        self.vs3.setGeometry(QtCore.QRect(620, 180, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.vs3.setFont(font)
        self.vs3.setObjectName("vs3")
        self.vs3.addItem("")
        self.vs3.addItem("")
        self.vs3.addItem("")
        self.vs3.addItem("")
        self.vs3.addItem("")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(530, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.u1 = QtWidgets.QPushButton(Dialog)
        self.u1.setGeometry(QtCore.QRect(570, 300, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.u1.setFont(font)
        self.u1.setObjectName("u1")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(530, 130, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.d1 = QtWidgets.QPushButton(Dialog)
        self.d1.setGeometry(QtCore.QRect(710, 300, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.d1.setFont(font)
        self.d1.setObjectName("d1")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(530, 80, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.vs1 = QtWidgets.QLineEdit(Dialog)
        self.vs1.setEnabled(False)
        self.vs1.setGeometry(QtCore.QRect(620, 80, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vs1.setFont(font)
        self.vs1.setObjectName("vs1")

        self.u1.clicked.connect(self.update)
        self.d1.clicked.connect(self.delete)
        self.ss.clicked.connect(self.get)
        self.ee1.clicked.connect(Dialog.accept)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ee1.setText(_translate("Dialog", "Exit"))
        item = self.t3.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Student Id"))
        item = self.t3.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Name"))
        item = self.t3.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Branch"))
        item = self.t3.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Year"))
        self.label.setText(_translate("Dialog", "View Student Details"))
        self.label_2.setText(_translate("Dialog", "Enter Student Id"))
        self.ss.setText(_translate("Dialog", "Search"))
        self.label_3.setText(_translate("Dialog", "        Edit Student Details"))
        self.vs4.setItemText(0, _translate("Dialog", "I"))
        self.vs4.setItemText(1, _translate("Dialog", "II"))
        self.vs4.setItemText(2, _translate("Dialog", "III"))
        self.vs4.setItemText(3, _translate("Dialog", "IV"))
        self.label_5.setText(_translate("Dialog", "Year"))
        self.vs3.setItemText(0, _translate("Dialog", "CSE"))
        self.vs3.setItemText(1, _translate("Dialog", "IT"))
        self.vs3.setItemText(2, _translate("Dialog", "ECE"))
        self.vs3.setItemText(3, _translate("Dialog", "CE"))
        self.vs3.setItemText(4, _translate("Dialog", "ME"))
        self.label_6.setText(_translate("Dialog", "Branch"))
        self.u1.setText(_translate("Dialog", "Update"))
        self.label_7.setText(_translate("Dialog", "Name"))
        self.d1.setText(_translate("Dialog", "Delete"))
        self.label_4.setText(_translate("Dialog", "Student Id"))

    def get(self):
        sid4=self.vs.text()
        Dialog=QtWidgets.QMessageBox()
        conn=sqlite3.connect('EXAMOMR.db')
        sql="Select * from STUDENT where Studentid='"+sid4+"';"
        cur = conn.execute(sql)
        result = cur.fetchone()
        if result is not None:
            sid = result[0]
            name = result[1]
            branch = result[2]
            year = result[3]

            if sid==sid4:
                self.vs1.setText(sid)
                self.vs2.setText(name)
                b=self.vs3.findText(branch)
                self.vs3.setCurrentIndex(b)
                y=self.vs4.findText(year)
                self.vs4.setCurrentIndex(y)

        else:
            Dialog.setWindowTitle("Invalid")
            Dialog.setIcon(QtWidgets.QMessageBox.Warning)
            Dialog.setText("Invalid StudentId")
            ret=Dialog.exec()
            self.clear()

    def update(self):
        Dialog=QtWidgets.QMessageBox()
        d=self.vs1.text()
        if d=="":
            Dialog.setWindowTitle("Invalid")
            Dialog.setIcon(QtWidgets.QMessageBox.Warning)
            Dialog.setText("Please Enter Student Id")
            ret=Dialog.exec()
        else:
            conn=sqlite3.connect('EXAMOMR.db')
            sid=self.vs1.text()
            name=self.vs2.text()

            branch=self.vs3.currentText()
            year=self.vs4.currentText()
            if year!="" and sid!="" and name!="" and branch!="":
                cur=conn.execute("UPDATE STUDENT SET Name='"+name+"',Branch='"+branch+"',Year='"+year+"' where Studentid='"+sid+"';")
                conn.commit()
                Dialog.setWindowTitle("Saved")
                Dialog.setIcon(QtWidgets.QMessageBox.Information)
                Dialog.setText("Updated Successfully")
                ret=Dialog.exec()
                self.clear()
                self.t3.clearContents()
                conn = sqlite3.connect('EXAMOMR.db')
                sql="Select * from STUDENT;"
                result=conn.execute(sql)
                self.t3.setRowCount(0)
                for row_number,row_data in enumerate(result):
                    self.t3.insertRow(row_number)
                    for column_number,data in enumerate(row_data):
                        self.t3.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))
                conn.close()
            else:
                Dialog.setWindowTitle("Invalid")
                Dialog.setIcon(QtWidgets.QMessageBox.Warning)
                Dialog.setText("Enter all Details")
                ret=Dialog.exec()
                


    def delete(self):
        Dialog=QtWidgets.QMessageBox()
        conn=sqlite3.connect('EXAMOMR.db')
        Dialog=QtWidgets.QMessageBox()
        sid=self.vs1.text()
        if sid=="":
            Dialog.setWindowTitle("Invalid")
            Dialog.setIcon(QtWidgets.QMessageBox.Warning)
            Dialog.setText("Please Enter Student Id")
            ret=Dialog.exec()
        else:   
            cur=conn.execute("DELETE from STUDENT where Studentid='"+sid+"';")
            conn.commit()
            Dialog.setIcon(QtWidgets.QMessageBox.Information)
            Dialog.setWindowTitle("Saved")
            Dialog.setText("Deleted Successfully")
            ret=Dialog.exec()
            self.t3.clearContents()
            self.clear()
            self.t3.clearContents()
            conn = sqlite3.connect('EXAMOMR.db')
            sql="Select * from STUDENT;"
            result=conn.execute(sql)
            self.t3.setRowCount(0)
            for row_number,row_data in enumerate(result):
                self.t3.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.t3.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))
            conn.close()

    def clear(self):
        self.vs.setText("")
        self.vs1.setText("")
        self.vs2.setText("")
        self.vs3.setCurrentIndex(0)
        self.vs4.setCurrentIndex(0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
