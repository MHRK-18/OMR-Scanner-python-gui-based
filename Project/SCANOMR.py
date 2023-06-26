# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SOMR.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import bg2

from PyQt5 import QtCore, QtGui, QtWidgets

# import the necessary packages

import sqlite3

from datetime import datetime
from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2

import tkinter as tk
from tkinter import filedialog


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 450)
        Dialog.setStyleSheet("QDialog{\n"
"background-image: url(:/newPrefix/bg2.jpg);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:lightpink;\n"
"}\n"
"    ")
        self.ec2 = QtWidgets.QLineEdit(Dialog)
        self.ec2.setGeometry(QtCore.QRect(230, 130, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ec2.setFont(font)
        self.ec2.setObjectName("ec2")
        self.s34 = QtWidgets.QPushButton(Dialog)
        self.s34.setGeometry(QtCore.QRect(20, 300, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.s34.setFont(font)
        self.s34.setObjectName("s34")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 190, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.e34 = QtWidgets.QPushButton(Dialog)
        self.e34.setGeometry(QtCore.QRect(340, 300, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.e34.setFont(font)
        self.e34.setObjectName("e34")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 40, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.sid1 = QtWidgets.QLineEdit(Dialog)
        self.sid1.setGeometry(QtCore.QRect(230, 190, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sid1.setFont(font)
        self.sid1.setObjectName("sid1")
        self.s34.clicked.connect(self.proceed)
        self.e34.clicked.connect(Dialog.accept)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.s34.setText(_translate("Dialog", " Scan OMR Sheet"))
        self.label_2.setText(_translate("Dialog", "Enter Student Id"))
        self.e34.setText(_translate("Dialog", "Exit"))
        self.label.setText(_translate("Dialog", "Scan Exam OMR Sheets"))
        self.label_3.setText(_translate("Dialog", "Enter Exam Code"))

    def proceed(self):
        import sqlite3
        from datetime import datetime
        Dialog=QtWidgets.QMessageBox()
        combo=""
        ri=""
        
        ec=self.ec2.text()
        sid=self.sid1.text()
        combo=ec+sid
        conn = sqlite3.connect('EXAMOMR.db')
        
        sql="Select OMRDETAILS.*,STUDENT.Studentid from OMRDETAILS,STUDENT where OMRDETAILS.Examcode='"+ec+"' and STUDENT.Studentid='"+sid+"';"
        cur=conn.execute(sql)
        row=cur.fetchone()
        
        sql1="Select * from RESULT where Resultid='"+combo+"';"
        cur1=conn.execute(sql1)
        result=cur1.fetchone()
        if result is not None:
            ri=result[7]
    
        if row is not None:
            examcode=row[0]
            edate=row[1]
            q1=row[2]
            nq=int(q1)
            o1=row[3]
            op=int(o1)
            qakey=row[4]
            studid=row[5]
            
            if examcode==ec and studid==sid:
                try:
                    ak=dict(item.split(":") for item in qakey.split(","))
                    
                    # Answer key maps the question number to the correct answer

                    ANSWER_KEY= {int(k):int(v) for k,v in ak.items()}
                                                     
                    now = datetime.now()
                    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

                    root = tk.Tk()
                    root.withdraw()

                    file_path = filedialog.askopenfilename()

                    # load the image
                    image = cv2.imread(r""+file_path+"")
                    # Convert the image into grayscale, 
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    # Slightly blur the gray scale image
                    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
                    # Find edges in the blurred image
                    edged = cv2.Canny(blurred, 75, 200)

                    # Find contours in the edged image
                    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)

                    # Initialize the contour that corresponds to the document
                    cnts = imutils.grab_contours(cnts)
                    docCnt = None

                    # Check that atleast one contour was found
                    if len(cnts) > 0:
                    # Sort the contours according to their size in descending order
                        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

                    # loop over the sorted contours
                        for c in cnts:
                            # approximate the contour
                                peri = cv2.arcLength(c, True)
                                approx = cv2.approxPolyDP(c, 0.02 * peri, True)

                            # If the contour has four points, then we consider it to be our OMR Sheet
                                if len(approx) == 4:
                                        docCnt = approx
                                        break

                    # Apply a four point perspective transform to both the original image, grayscale image to obtain a top-down
                    # birds eye view of the paper
                    paper = four_point_transform(image, docCnt.reshape(4, 2))
                    warped = four_point_transform(gray, docCnt.reshape(4, 2))

                    epaper = four_point_transform(image, docCnt.reshape(4, 2))

                    # apply Otsu's thresholding method to binarize the warped
                    # piece of paper
                    thresh = cv2.threshold(warped, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

                    # find contours in the thresholded image, then initialize
                    # the list of contours that correspond to questions
                    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
                    cnts = imutils.grab_contours(cnts)
                    questionCnts = []

                    # loop over the contours
                    for c in cnts:
                    # compute the bounding box of the contour, then use the
                    # bounding box to derive the aspect ratio
                            (x, y, w, h) = cv2.boundingRect(c)
                            ar = w / float(h)

                    # in order to label the contour as a question, region
                    # should be sufficiently wide, sufficiently tall, and
                    # have an aspect ratio approximately equal to 1
                            if w >= 20 and h >= 20 and ar >= 0.9 and ar <= 1.1:
                                    questionCnts.append(c)

                    #Check if the no.of bubbles in the OMR Sheet is equal to the no.of Contours (questionCnts)
                    #nq stands for no.of questions
                    #op stands for no.of options                

                    total_bubbles=nq*op

                    l=len(questionCnts)

                    if l==total_bubbles:

                        # sort the question contours top-to-bottom, then initialize
                        # the total number of correct answers
                        questionCnts = contours.sort_contours(questionCnts,method="top-to-bottom")[0]
                        correct = 0

                        # each question has possible options
                        # To loop over the question in batches of the no.of options
                        for (q, i) in enumerate(np.arange(0, len(questionCnts), op)):
                            
                        # sort the contours for the current question from
                        # left to right, then initialize the index of the
                        # bubbled answer
                        
                            cnts = contours.sort_contours(questionCnts[i:i + op])[0]
                            bubbled = None

                        # loop over the sorted contours
                            for (j, c) in enumerate(cnts):
                                # construct a mask that reveals only the current
                                # "bubble" for the question
                                    mask = np.zeros(thresh.shape, dtype="uint8")
                                    cv2.drawContours(mask, [c], -1, 255, -1)

                                # apply the mask to the thresholded image, then
                                # count the number of non-zero pixels in the
                                # bubble area
                                    mask = cv2.bitwise_and(thresh, thresh, mask=mask)
                                    total = cv2.countNonZero(mask)

                                # if the current total has a larger number of total
                                # non-zero pixels, then we are examining the currently
                                # bubbled-in answer
                                    if bubbled is None or total > bubbled[0]:
                                            bubbled = (total, j)

                        # initialize the contour color and the index of the
                        # *correct* answer
                            color = (0, 0, 255)
                            k = ANSWER_KEY[q]

                        # check to see if the bubbled answer is correct
                            if k == bubbled[1]:
                                    color = (0, 255, 0)
                                    correct += 1

                        # draw the outline of the correct answer on the test
                            cv2.drawContours(paper, [cnts[k]], -1, color, 3)

                        # Calculate the Persentage and Result.
                        #Result can be Pass or Fail.
                        #Percentage of 36 and above is considerd to be Pass.
                        score = (correct / nq) * 100
                        p=score
                        perc=round(p,2)
                        print(perc)
                        res=""
                        if score>=36:
                            res="Pass"
                        else:
                            res="Fail"
                        print("[INFO] score: {:.2f}%".format(score))
                        cv2.putText(paper, "{:.2f}%".format(score), (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

                        scale = 85 # percent of original size

                        # Resize the Result image 
                        wi = int(paper.shape[1] * scale / 100)
                        he = int(paper.shape[0] * scale / 100)
                        dim1 = (wi, he)
                        exam = cv2.resize(paper, dim1, interpolation = cv2.INTER_AREA)

                        # Resize the Original image 
                        width = int(epaper.shape[1] * scale / 100)
                        height = int(epaper.shape[0] * scale / 100)
                        dim2 = (width, height)
                        original = cv2.resize(epaper, dim2, interpolation = cv2.INTER_AREA)
                        cv2.imshow("Exam", original)

                        cv2.imshow("Result", exam)
                        
                        cv2.waitKey(0)
                        self.sid1.setText("")

                        #Update the Result if the Result is already existing in the database
                        if ri==combo:
                            cur2=conn.execute("UPDATE RESULT SET Percentage='"+str(perc)+"',Result='"+str(res)+"',Omrsheet='"+str(file_path)+"',Evadate='"+str(dt_string)+"' where Resultid='"+combo+"';")
                            cur2=conn.execute(sql)
                            conn.commit()
                            Dialog.setWindowTitle("Updated")
                            Dialog.setIcon(QtWidgets.QMessageBox.Information)
                            Dialog.setText("OMR Sheet Updated Successfully")
                            ret=Dialog.exec()
                            
                        #Save the Result into the Database    
                        else:
                            cur3=conn.execute("INSERT INTO RESULT (Examcode,Studentid,Edate,Percentage,Result,Omrsheet,Evadate,Resultid) VALUES ('"+str(examcode)+"','"+str(sid)+"','"+str(edate)+"','"+str(perc)+"','"+str(res)+"','"+str(file_path)+"','"+str(dt_string)+"','"+str(combo)+"');")
                            cur3=conn.execute(sql)
                            conn.commit()
                            Dialog.setWindowTitle("Inserted")
                            Dialog.setIcon(QtWidgets.QMessageBox.Information)
                            Dialog.setText("OMR Sheet Scanned Successfully")
                            ret=Dialog.exec()
                    else:
                        Dialog.setWindowTitle("Invalid")
                        Dialog.setIcon(QtWidgets.QMessageBox.Warning)
                        Dialog.setText("Invalid Image.Rescan OMR Sheet.")
                        ret=Dialog.exec()

                except AttributeError:
                    Dialog.setWindowTitle("Invalid")
                    Dialog.setIcon(QtWidgets.QMessageBox.Warning)
                    Dialog.setText("Invalid Image.Rescan OMR Sheet.")
                    ret=Dialog.exec()

                except KeyError:
                    Dialog.setWindowTitle("Invalid")
                    Dialog.setIcon(QtWidgets.QMessageBox.Warning)
                    Dialog.setText("Rescan OMR sheet")
                    ret=Dialog.exec()

                except ValueError:
                    Dialog.setWindowTitle("Invalid")
                    Dialog.setIcon(QtWidgets.QMessageBox.Warning)
                    Dialog.setText("Rescan OMR sheet")
                    ret=Dialog.exec()

                except IndexError:
                    Dialog.setWindowTitle("Invalid")
                    Dialog.setIcon(QtWidgets.QMessageBox.Warning)
                    Dialog.setText("Rescan OMR sheet")
                    ret=Dialog.exec()

                except TypeError:
                    Dialog.setWindowTitle("Invalid")
                    Dialog.setIcon(QtWidgets.QMessageBox.Warning)
                    Dialog.setText("Please check Question-Answer key")
                    ret=Dialog.exec()


                except sqlite3.Error:
                    Dialog.setWindowTitle("Invalid")
                    Dialog.setIcon(QtWidgets.QMessageBox.Warning)
                    Dialog.setText("Database Error")
                    ret=Dialog.exec()

                except BaseException:
                    Dialog.setWindowTitle("Invalid")
                    Dialog.setIcon(QtWidgets.QMessageBox.Warning)
                    Dialog.setText("Invalid Image. Rescan OMR Sheet.")
                    ret=Dialog.exec()

        else:
            Dialog.setWindowTitle("Invalid")
            Dialog.setIcon(QtWidgets.QMessageBox.Warning)
            Dialog.setText("Invalid Examcode or Studentid")
            ret=Dialog.exec()
            self.clear()


            
    def clear(self):
        self.ec2.setText("")
        self.sid1.setText("")




if __name__ == "__main__":
    import sys
    import sqlite3
    import datetime
    conn = sqlite3.connect('EXAMOMR.db')
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
