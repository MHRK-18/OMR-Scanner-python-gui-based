# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VE1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import bg3

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
"    ")
        self.ee2 = QtWidgets.QPushButton(Dialog)
        self.ee2.setGeometry(QtCore.QRect(330, 160, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ee2.setFont(font)
        self.ee2.setObjectName("ee2")
        self.ve = QtWidgets.QLineEdit(Dialog)
        self.ve.setGeometry(QtCore.QRect(250, 100, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ve.setFont(font)
        self.ve.setObjectName("ve")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 30, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.es = QtWidgets.QPushButton(Dialog)
        self.es.setGeometry(QtCore.QRect(110, 160, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.es.setFont(font)
        self.es.setObjectName("es")
        self.t4 = QtWidgets.QTableWidget(Dialog)
        self.t4.setGeometry(QtCore.QRect(20, 220, 511, 221))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.t4.setFont(font)
        self.t4.setRowCount(200)
        self.t4.setColumnCount(5)
        self.t4.setObjectName("t4")
        item = QtWidgets.QTableWidgetItem()
        self.t4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.t4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.t4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.t4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.t4.setHorizontalHeaderItem(4, item)

        conn=sqlite3.connect('EXAMOMR.db')
        sql="Select * from OMRDETAILS ORDER BY Edate DESC;"
        result=conn.execute(sql)
        self.t4.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.t4.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.t4.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(560, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.d2 = QtWidgets.QPushButton(Dialog)
        self.d2.setGeometry(QtCore.QRect(730, 370, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.d2.setFont(font)
        self.d2.setObjectName("d2")
        self.ve3 = QtWidgets.QLineEdit(Dialog)
        self.ve3.setGeometry(QtCore.QRect(700, 200, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ve3.setFont(font)
        self.ve3.setObjectName("ve3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(560, 300, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.ve5 = QtWidgets.QLineEdit(Dialog)
        self.ve5.setGeometry(QtCore.QRect(700, 300, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ve5.setFont(font)
        self.ve5.setObjectName("ve5")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(560, 250, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(610, 40, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.ve1 = QtWidgets.QLineEdit(Dialog)
        self.ve1.setEnabled(False)
        self.ve1.setGeometry(QtCore.QRect(700, 100, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ve1.setFont(font)
        self.ve1.setObjectName("ve1")
        self.ve4 = QtWidgets.QLineEdit(Dialog)
        self.ve4.setGeometry(QtCore.QRect(700, 250, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ve4.setFont(font)
        self.ve4.setObjectName("ve4")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(560, 200, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.ve2 = QtWidgets.QLineEdit(Dialog)
        self.ve2.setGeometry(QtCore.QRect(700, 150, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ve2.setFont(font)
        self.ve2.setObjectName("ve2")
        self.u2 = QtWidgets.QPushButton(Dialog)
        self.u2.setGeometry(QtCore.QRect(600, 370, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.u2.setFont(font)
        self.u2.setObjectName("u2")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(560, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.es.clicked.connect(self.get)
        self.u2.clicked.connect(self.update)
        self.d2.clicked.connect(self.delete)
        self.ee2.clicked.connect(Dialog.accept)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ee2.setText(_translate("Dialog", "Exit"))
        self.label.setText(_translate("Dialog", "View OMR Sheet Details"))
        self.label_2.setText(_translate("Dialog", "Enter Exam Code"))
        self.es.setText(_translate("Dialog", "Search"))
        item = self.t4.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Exam Code"))
        item = self.t4.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Exam Date"))
        item = self.t4.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "No.of Questions"))
        item = self.t4.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "No.of Options"))
        item = self.t4.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Q\\A Key"))
        self.label_3.setText(_translate("Dialog", "Exam Date"))
        self.d2.setText(_translate("Dialog", "Delete"))
        self.label_4.setText(_translate("Dialog", "Enter the Q/A Key"))
        self.label_5.setText(_translate("Dialog", "No.of Options"))
        self.label_6.setText(_translate("Dialog", "Edit OMR Sheet Details"))
        self.label_7.setText(_translate("Dialog", "No.of Questions"))
        self.u2.setText(_translate("Dialog", "Update"))
        self.label_8.setText(_translate("Dialog", "Exam Code"))
    
    def get(self):
        ecode=self.ve.text()
        Dialog=QtWidgets.QMessageBox()

        conn=sqlite3.connect('EXAMOMR.db')
        ec=""
        sql="Select * from OMRDETAILS where Examcode='"+str(ecode)+"';"
        cur=conn.execute(sql)
        result=cur.fetchone()
        if result is not None:
            ec=result[0]
            ed=result[1]
            q=result[2]
            
            o=result[3]
            
            qa=result[4]
            
            self.ve1.setText(ec)
            self.ve2.setText(str(ed))
            self.ve3.setText(str(q))
            self.ve4.setText(str(o))
            self.ve5.setText(qa)
            
        else:
            Dialog.setWindowTitle("Invalid")
            Dialog.setIcon(QtWidgets.QMessageBox.Warning)
            Dialog.setText("Invalid Exam code")
            ret=Dialog.exec()
            self.clear()


    def update(self):
        Dialog=QtWidgets.QMessageBox()
        d=self.ve1.text()
        if d=="":
            Dialog.setWindowTitle("Invalid")
            Dialog.setIcon(QtWidgets.QMessageBox.Warning)
            Dialog.setText("Please Enter Exam code")
            ret=Dialog.exec()
        else:    
            conn=sqlite3.connect('EXAMOMR.db')
            ecode=self.ve.text()
            ed1=self.ve2.text()
            q1=self.ve3.text()
            o1=self.ve4.text()
            qa1=self.ve5.text()
            if ed1!="" and q1!="" and o1!="" and qa1!="":
                cur=conn.execute("UPDATE OMRDETAILS SET Edate='"+ed1+"',Questions='"+q1+"',Options='"+o1+"',QAkey='"+qa1+"' where Examcode='"+ecode+"';")
                conn.commit()
                Dialog.setIcon(QtWidgets.QMessageBox.Information)
                Dialog.setWindowTitle("Saved")
                
                Dialog.setText("Updated Successfully")
                ret=Dialog.exec()
                self.t4.clearContents()
                self.clear()
                conn=sqlite3.connect('EXAMOMR.db')
                sql="Select * from OMRDETAILS;"
                result=conn.execute(sql)
                self.t4.setRowCount(0)
                for row_number,row_data in enumerate(result):
                    self.t4.insertRow(row_number)
                    for column_number,data in enumerate(row_data):
                        self.t4.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))
                conn.close()
            else:
                Dialog.setWindowTitle("Invalid")
                Dialog.setIcon(QtWidgets.QMessageBox.Warning)
                Dialog.setText("Enter all details")
                ret=Dialog.exec()
                

    def delete(self):
        Dialog=QtWidgets.QMessageBox()
        d=self.ve1.text()
        if d=="":
            Dialog.setWindowTitle("Invalid")
            Dialog.setIcon(QtWidgets.QMessageBox.Warning)
            Dialog.setText("Please Enter Examcode")
            ret=Dialog.exec()
        else:    
            conn=sqlite3.connect('EXAMOMR.db')
            ecode=self.ve.text()
            cur=conn.execute("DELETE from OMRDETAILS where Examcode='"+ecode+"';")
            conn.commit()
            Dialog.setIcon(QtWidgets.QMessageBox.Information)
            Dialog.setWindowTitle("Saved")
            Dialog.setText("Deleted Successfully")
            ret=Dialog.exec()
            self.t4.clearContents()
            self.clear()
            conn=sqlite3.connect('EXAMOMR.db')
            sql="Select * from OMRDETAILS;"
            result=conn.execute(sql)
            self.t4.setRowCount(0)
            for row_number,row_data in enumerate(result):
                self.t4.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.t4.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))
            conn.close()

    def clear(self):
        self.ve.setText("")
        self.ve1.setText("")
        self.ve2.setText("")
        self.ve3.setText("")
        self.ve4.setText("")
        self.ve5.setText("")
        
        

if __name__ == "__main__":
    
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
