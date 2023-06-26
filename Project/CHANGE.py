# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CHANGE.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import mbg2

class Ui_cp(object):
    def setupUi(self, cp):
        cp.setObjectName("cp")
        cp.resize(500, 450)
        cp.setStyleSheet("QDialog{\n"
"background-image: url(:/newPrefix/mbg2.jpg);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:darkgrey;\n"
"color:white;\n"
"}\n"
"")
        self.cuid = QtWidgets.QLineEdit(cp)
        self.cuid.setGeometry(QtCore.QRect(230, 130, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cuid.setFont(font)
        self.cuid.setObjectName("cuid")
        self.label_2 = QtWidgets.QLabel(cp)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.copwd = QtWidgets.QLineEdit(cp)
        self.copwd.setGeometry(QtCore.QRect(230, 190, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.copwd.setFont(font)
        self.copwd.setMaxLength(32764)
        self.copwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.copwd.setObjectName("copwd")
        self.cs = QtWidgets.QPushButton(cp)
        self.cs.setGeometry(QtCore.QRect(60, 340, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cs.setFont(font)
        self.cs.setObjectName("cs")
        self.label_3 = QtWidgets.QLabel(cp)
        self.label_3.setGeometry(QtCore.QRect(60, 190, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(cp)
        self.label.setGeometry(QtCore.QRect(80, 50, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: lightpink;")
        self.label.setObjectName("label")
        self.ce = QtWidgets.QPushButton(cp)
        self.ce.setGeometry(QtCore.QRect(300, 340, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ce.setFont(font)
        self.ce.setObjectName("ce")
        self.label_4 = QtWidgets.QLabel(cp)
        self.label_4.setGeometry(QtCore.QRect(60, 250, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.cnpwd = QtWidgets.QLineEdit(cp)
        self.cnpwd.setGeometry(QtCore.QRect(230, 250, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cnpwd.setFont(font)
        self.cnpwd.setObjectName("cnpwd")

        self.cs.clicked.connect(self.change)
        self.ce.clicked.connect(cp.accept)

        self.hide=cp.accept
        self.retranslateUi(cp)
        QtCore.QMetaObject.connectSlotsByName(cp)

    def retranslateUi(self, cp):
        _translate = QtCore.QCoreApplication.translate
        cp.setWindowTitle(_translate("cp", "Dialog"))
        self.label_2.setText(_translate("cp", "Username"))
        self.cs.setText(_translate("cp", "Change Password"))
        self.label_3.setText(_translate("cp", "Old Password"))
        self.label.setText(_translate("cp", "       Change Password"))
        self.ce.setText(_translate("cp", "Cancel"))
        self.label_4.setText(_translate("cp", "New Password"))

    def change(self):
        import sqlite3
        Dialog=QtWidgets.QMessageBox()
        usern=self.cuid.text()
        oldp=self.copwd.text()
        newp=self.cnpwd.text()

        conn = sqlite3.connect('EXAMOMR.db')
        sql="Select * from REGISTER where Username='"+usern+"';"
        cur=conn.execute(sql)
        row=cur.fetchone()
        if row is not None:
            uid1=row[3]
            pwd1=row[4]
            if uid1==usern and oldp==pwd1 and newp!="":
                cur=conn.execute("UPDATE REGISTER SET Password='"+newp+"' where Username='"+usern+"';")
                conn.commit()
                Dialog.setWindowTitle("Saved")
                Dialog.setIcon(QtWidgets.QMessageBox.Information)
                Dialog.setText("Password changed Successfully")
                ret=Dialog.exec()
                self.hide()
                self.clear()
            if uid1==usern and oldp!=pwd1:
                Dialog.setWindowTitle("Invalid")
                Dialog.setIcon(QtWidgets.QMessageBox.Warning)
                Dialog.setText("Enter valid Username and Password")
                ret=Dialog.exec()
                self.clear()
            if uid1==usern and oldp==pwd1 and newp=="":
                Dialog.setWindowTitle("Invalid")
                Dialog.setIcon(QtWidgets.QMessageBox.Warning)
                Dialog.setText("Enter all the Details")
                ret=Dialog.exec()
                
        else:
            Dialog.setWindowTitle("Invalid")
            Dialog.setIcon(QtWidgets.QMessageBox.Warning)
            Dialog.setText("Enter valid Username and Password")
            ret=Dialog.exec()
            self.clear()




    def clear(self):
        self.cuid.setText("")
        self.copwd.setText("")
        self.cnpwd.setText("")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cp = QtWidgets.QDialog()
    ui = Ui_cp()
    ui.setupUi(cp)
    cp.show()
    sys.exit(app.exec_())
