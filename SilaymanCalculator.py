# -*- coding: cp1252 -*-
import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from math import *
import threading
form_class = uic.loadUiType("SilaymanCalculator.ui")[0]
class MyWindowClass(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.pushButton_7.clicked.connect(self.clear_button)
        self.pushButton_21.clicked.connect(self.zero_button)
        self.pushButton_19.clicked.connect(self.one_button)
        self.pushButton_4.clicked.connect(self.multiply_button)
        self.pushButton_10.clicked.connect(self.equals_button)
        self.pushButton_20.clicked.connect(self.two_button)
        self.pushButton_18.clicked.connect(self.three_button)
        self.pushButton_17.clicked.connect(self.four_button)
        self.pushButton_16.clicked.connect(self.five_button)
        self.pushButton_15.clicked.connect(self.six_button)
        self.pushButton_14.clicked.connect(self.seven_button)
        self.pushButton_13.clicked.connect(self.eight_button)
        self.pushButton_12.clicked.connect(self.nine_button)
        self.pushButton_5.clicked.connect(self.addition_button)
        self.pushButton_11.clicked.connect(self.decimal_button)
        self.pushButton_6.clicked.connect(self.subtraction_button)
        self.pushButton_3.clicked.connect(self.division_button)
        self.pushButton_9.clicked.connect(self.percentage_button)
        self.pushButton_8.clicked.connect(self.negative_button)
        self.pushButton_22.clicked.connect(self.delete_button)
    def clear_button(self):
        self.lineEdit.clear()
    def zero_button(self):
        self.lineEdit.insert("0")
    def one_button(self):
        self.lineEdit.insert("1")
    def two_button(self):
        self.lineEdit.insert("2")
    def three_button(self):
        self.lineEdit.insert("3")
    def four_button(self):
        self.lineEdit.insert("4")
    def five_button(self):
        self.lineEdit.insert("5")
    def six_button(self):
        self.lineEdit.insert("6")
    def seven_button(self):
        self.lineEdit.insert("7")
    def eight_button(self):
        self.lineEdit.insert("8")
    def nine_button(self):
        self.lineEdit.insert("9")
    def decimal_button(self):
        self.lineEdit.insert(".")
    def multiply_button(self):
        self.lineEdit.insert("x")
    def addition_button(self):
        self.lineEdit.insert("+")
    def subtraction_button(self):
        self.lineEdit.insert("(-)")
    def division_button(self):
        self.lineEdit.insert("÷")
    def percentage_button(self):
        input_text1 = self.lineEdit.text()
        self.lineEdit.clear()
        answer = float(input_text1) / float(100)
        self.lineEdit.insert(str(answer))
    def negative_button(self):
        self.lineEdit.insert("-")
    def delete_button(self):
        self.lineEdit.backspace()
    def equals_button(self):
        input_text1 = self.lineEdit.text()
        if "x" in input_text1:
            input_text = input_text1.split("x")
            numerouno = (input_text[0])
            numerodos = (input_text[1])
            answer1 = float(numerouno) * float(numerodos)
            self.lineEdit.clear()
            self.lineEdit.insert(str(answer1))
        if "+" in input_text1:
            input_text = input_text1.split("+")
            numerouno = (input_text[0])
            numerodos = (input_text[1])
            answer1 = float(numerouno) + float(numerodos)
            self.lineEdit.clear()
            self.lineEdit.insert(str(answer1))
        if "(-)" in input_text1:
            input_text = input_text1.split("(-)")
            numerouno = (input_text[0])
            numerodos = (input_text[1])
            answer1 = float(numerouno) - float(numerodos)
            self.lineEdit.clear()
            self.lineEdit.insert(str(answer1))
        if "÷" in input_text1:
            input_text = input_text1.split("÷")
            numerouno = (input_text[0])
            numerodos = (input_text[1])
            answer1 = float(numerouno) / float(numerodos)
            self.lineEdit.clear()
            self.lineEdit.insert(str(answer1))

app = QtWidgets.QApplication(sys.argv)
myWindow = MyWindowClass()
myWindow.show()
app.exec_()
