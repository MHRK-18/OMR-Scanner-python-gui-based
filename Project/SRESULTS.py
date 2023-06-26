# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SR.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import result
import sqlite3

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 450)
        Dialog.setStyleSheet("\n"
"QDialog{\n"
"background-image: url(:/newPrefix/result.jpg);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#8cb3d9;\n"
"color:black;\n"
"}\n"
"")
        self.s6 = QtWidgets.QPushButton(Dialog)
        self.s6.setGeometry(QtCore.QRect(160, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.s6.setFont(font)
        self.s6.setObjectName("s6")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(230, 0, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 50, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.e6 = QtWidgets.QPushButton(Dialog)
        self.e6.setGeometry(QtCore.QRect(340, 100, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.e6.setFont(font)
        self.e6.setObjectName("e6")
        self.sid2 = QtWidgets.QLineEdit(Dialog)
        self.sid2.setGeometry(QtCore.QRect(260, 50, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sid2.setFont(font)
        self.sid2.setObjectName("sid2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(380, 170, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.sn = QtWidgets.QLineEdit(Dialog)
        self.sn.setEnabled(False)
        self.sn.setGeometry(QtCore.QRect(160, 170, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sn.setFont(font)
        self.sn.setObjectName("sn")
        self.sb = QtWidgets.QLineEdit(Dialog)
        self.sb.setEnabled(False)
        self.sb.setGeometry(QtCore.QRect(450, 170, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sb.setFont(font)
        self.sb.setObjectName("sb")
        self.t2 = QtWidgets.QTableWidget(Dialog)
        self.t2.setEnabled(False)
        self.t2.setGeometry(QtCore.QRect(30, 230, 531, 201))
        self.t2.setRowCount(100)
        self.t2.setColumnCount(5)
        self.t2.setObjectName("t2")
        item = QtWidgets.QTableWidgetItem()
        self.t2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.t2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.t2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.t2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.t2.setHorizontalHeaderItem(4, item)
        self.s6.clicked.connect(self.get)
        self.e6.clicked.connect(Dialog.accept)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.s6.setText(_translate("Dialog", "Submit"))
        self.label.setText(_translate("Dialog", "Student  Results"))
        self.label_2.setText(_translate("Dialog", "Enter Student Id"))
        self.e6.setText(_translate("Dialog", "Exit"))
        self.label_3.setText(_translate("Dialog", "Student Name"))
        self.label_4.setText(_translate("Dialog", "Branch"))
        item = self.t2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Exam Code"))
        item = self.t2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Exam Date"))
        item = self.t2.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Year"))
        item = self.t2.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Percentage"))
        item = self.t2.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Results"))
    

    def get(self):
        Dialog=QtWidgets.QMessageBox()
        studid=self.sid2.text()
        conn=sqlite3.connect('EXAMOMR.db')
        sql="Select RESULT.Examcode,RESULT.Edate,STUDENT.Year,RESULT.Percentage,RESULT.Result from STUDENT,RESULT WHERE RESULT.Studentid=STUDENT.Studentid and STUDENT.Studentid='"+str(studid)+"';"
        sql1="Select * from STUDENT where Studentid='"+studid+"';"
        cur=conn.execute(sql1)
        row=cur.fetchone()
        
        if row is not None:
            stid=row[0]
            name=row[1]
            branch=row[2]
            if studid==stid:
                self.sn.setText(name)
                self.sb.setText(branch)
                result=conn.execute(sql)
                if result is not None:
                    self.t2.setRowCount(0)
                    for row_number,row_data in enumerate(result):
                        self.t2.insertRow(row_number)
                        for column_number,data in enumerate(row_data):
                            self.t2.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))

                    conn.close()
        else:
            Dialog.setWindowTitle("Invalid")
            Dialog.setIcon(QtWidgets.QMessageBox.Warning)
            Dialog.setText("Invalid Studentid")
            ret=Dialog.exec()
            self.clear()
            
    def clear(self):
        self.sid2.setText("")
        self.sn.setText("")
        self.sb.setText("")
        self.t2.clearContents()
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
