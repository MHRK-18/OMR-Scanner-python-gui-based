# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ER.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 450)
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setStyleSheet("QDialog{\n"
"background-image: url(:/newPrefix/result.jpg);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#8cb3d9;\n"
"color:black;\n"
"}\n"
"")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(250, 20, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 80, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ec3 = QtWidgets.QLineEdit(Dialog)
        self.ec3.setGeometry(QtCore.QRect(290, 80, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ec3.setFont(font)
        self.ec3.setObjectName("ec3")
        self.t1 = QtWidgets.QTableWidget(Dialog)
        self.t1.setEnabled(True)
        self.t1.setGeometry(QtCore.QRect(10, 220, 631, 201))
        self.t1.setGridStyle(QtCore.Qt.NoPen)
        
        self.t1.setRowCount(100)
        self.t1.setColumnCount(6)
        self.t1.setObjectName("t1")
        item = QtWidgets.QTableWidgetItem()
        self.t1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.t1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.t1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.t1.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.t1.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.t1.setHorizontalHeaderItem(5, item)
        self.s5 = QtWidgets.QPushButton(Dialog)
        self.s5.setGeometry(QtCore.QRect(150, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.s5.setFont(font)
        self.s5.setObjectName("s5")
        self.e5 = QtWidgets.QPushButton(Dialog)
        self.e5.setGeometry(QtCore.QRect(380, 150, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.e5.setFont(font)
        self.e5.setObjectName("e5")

        self.s5.clicked.connect(self.get)
        self.e5.clicked.connect(Dialog.accept)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Exam Results"))
        self.label_2.setText(_translate("Dialog", "Enter Exam Code"))
        item = self.t1.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Student Id"))
        item = self.t1.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Name"))
        item = self.t1.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Branch"))
        item = self.t1.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Year"))
        item = self.t1.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Percentage"))
        item = self.t1.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Results"))
        self.s5.setText(_translate("Dialog", "Submit"))
        self.e5.setText(_translate("Dialog", "Exit"))

    def get(self):
        Dialog=QtWidgets.QMessageBox()
        ecode=self.ec3.text()
        conn=sqlite3.connect('EXAMOMR.db')
        sql="Select STUDENT.*,RESULT.Percentage,RESULT.Result from STUDENT,RESULT WHERE RESULT.Studentid=STUDENT.Studentid and RESULT.Examcode='"+ecode+"';"
        sql1="Select * from RESULT where Examcode='"+ecode+"';"
        cur=conn.execute(sql1)
        row=cur.fetchone()
        sql2="Select * from OMRDETAILS where Examcode='"+ecode+"';"
        conn=sqlite3.connect('EXAMOMR.db')
        cur1=conn.execute(sql2)
        row1=cur1.fetchone()

        if row is not None:
            ec=row[0]
            if ecode==ec:
                result=conn.execute(sql)
                if result is not None:
                    self.t1.setRowCount(0)
                    for row_number,row_data in enumerate(result):
                        self.t1.insertRow(row_number)
                        for column_number,data in enumerate(row_data):
                            self.t1.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))
                    conn.close()
        elif (row1 is not None):
            Dialog.setWindowTitle("No Result")
            Dialog.setIcon(QtWidgets.QMessageBox.Warning)
            Dialog.setText("No Results to be displayed")
            ret=Dialog.exec()
            self.clear()
        

                    
        else:
            Dialog.setWindowTitle("Invalid")
            Dialog.setIcon(QtWidgets.QMessageBox.Warning)
            Dialog.setText("Invalid Exam code")
            ret=Dialog.exec()
            self.clear()
            
    def clear(self):
        self.ec3.setText("")
        self.t1.clearContents()



import result


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
