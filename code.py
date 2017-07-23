# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from toMachine import *
from Linker import *
from MACROProcessor import *
from Loader import *
import re, sys, os, time


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form, offset):
        ############ FEATURES OF PROCESSOR ############
        self.getIntVal = 0
        self.offset1 = offset
        self.byteLen = offset
        self.regs = {'A' : 0, 'B' : 0, 'C' : 0, 'D' : 0, 'E' : 0, 'F' : 0, 'H' : 0, 'L' : 0,}
        self.flags = [0 for i in range(5)]
        self.PC = 1
        self.macroTrigger = False
        self.WORDCount = 0
        self.mainPart ="START "+ str(offset) +"\n"
        self.dataPart = ""
        self.varsInt = {}
        self.varsChar = {}
        self.mapping = {}
        self.symbolTable = {}
        self.conditionCount = 0
        self.lastCondition = []
        self.lastloop = []
        self.loopCount = 0
        self.poolList = {}
        self.macroProcessed = ""
        self.stack = []
        self.firstPassMain = ""
        self.firstPassData = ""
        self.MNT=[]
        self.PNTAB = []
        self.APTAB = []
        self.MDT = []
        self.linked = ""
        self.loaded = ""
        self.calls = []
        self.EVTAB = []
        #########################################
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1003, 700)
        p = Form.palette()
        #p.setColor(Form.backgroundRole(), Qt.yellow)
        p.setColor(Form.backgroundRole(), QtGui.QColor(175, 155, 155))
        Form.setPalette(p)
        self.plainTextEdit = QtGui.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(50, 90, 271, 531))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(Form)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(340, 90, 271, 531))
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 10, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 70, 181, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(380, 70, 181, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(670, 120, 581, 301))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.tabWidget = QtGui.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 580, 301))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tableWidget = QtGui.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 281, 281))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tableWidget_2 = QtGui.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 0, 211, 261))
        self.tableWidget_2.setRowCount(5)
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(4, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(4, 1, item)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tableWidget_3 = QtGui.QTableWidget(self.tab_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 10, 256, 251))
        self.tableWidget_3.setRowCount(10)
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(3, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(4, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(4, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(5, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(5, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(6, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(6, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(7, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(7, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(8, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(8, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(9, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(9, 1, item)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))


        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.tableWidget_4 = QtGui.QTableWidget(self.tab_4)
        self.tableWidget_4.setGeometry(QtCore.QRect(10, 10, 256, 251))
        self.tableWidget_4.setRowCount(10)
        self.tableWidget_4.setColumnCount(2)
        self.tableWidget_4.setObjectName(_fromUtf8("tableWidget_4"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(3, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(4, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(4, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(5, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(5, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(6, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(6, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(7, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(7, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(8, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(8, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(9, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(9, 1, item)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))


        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.tableWidget_5 = QtGui.QTableWidget(self.tab_5)
        self.tableWidget_5.setGeometry(QtCore.QRect(10, 10, 256, 251))
        self.tableWidget_5.setRowCount(10)
        self.tableWidget_5.setColumnCount(2)
        self.tableWidget_5.setObjectName(_fromUtf8("tableWidget_5"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(3, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(4, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(4, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(5, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(5, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(6, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(6, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(7, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(7, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(8, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(8, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(9, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(9, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(10, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(10, 1, item)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))

        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.plainTextEdit_3 = QtGui.QPlainTextEdit(self.tab_6)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(0, 0, 571, 631))
        self.plainTextEdit_3.setObjectName(_fromUtf8("plainTextEdit_3"))
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))

        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.plainTextEdit_4 = QtGui.QPlainTextEdit(self.tab_7)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(0, 0, 571, 631))
        self.plainTextEdit_4.setObjectName(_fromUtf8("plainTextEdit_4"))
        self.tabWidget.addTab(self.tab_7, _fromUtf8(""))

        self.lcdNumber = QtGui.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(800, 70, 64, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setLineWidth(1)
        palette = self.lcdNumber.palette()
        palette.setColor(palette.Dark, QtGui.QColor(0, 0, 0))
        self.lcdNumber.setPalette(palette)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))

        self.lcdNumber_2 = QtGui.QLCDNumber(Form)
        self.lcdNumber_2.setGeometry(QtCore.QRect(990, 70, 64, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber_2.setFont(font)
        self.lcdNumber_2.setLineWidth(1)
        palette = self.lcdNumber_2.palette()
        palette.setColor(palette.Dark, QtGui.QColor(0, 0, 0))
        self.lcdNumber_2.setPalette(palette)
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))

        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(680, 70, 121, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(870, 70, 121, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(670, 450, 150, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 490, 99, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(840, 450, 99, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(840, 490, 99, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(720, 570, 221, 27))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(720, 530, 221, 27))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onestep)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.loader)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.linker)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.reset)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.machine)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.secPass)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Assembler Linker Loader Simulator", None))
        self.label_2.setText(_translate("Form", "User Defined Language", None))
        self.label_3.setText(_translate("Form", "Assembly Language", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "A", None))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Form", "B", None))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("Form", "C", None))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("Form", "D", None))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("Form", "E", None))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("Form", "F", None))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("Form", "H", None))
        item = self.tableWidget.item(6, 1)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("Form", "L", None))
        item = self.tableWidget.item(7, 1)
        item.setText(_translate("Form", "0", None))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Registers", None))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("Form", "GTFlag", None))
        item = self.tableWidget_2.item(0, 1)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget_2.item(1, 0)
        item.setText(_translate("Form", "LTFlag", None))
        item = self.tableWidget_2.item(1, 1)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget_2.item(2, 0)
        item.setText(_translate("Form", "EQFlag", None))
        item = self.tableWidget_2.item(2, 1)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget_2.item(3, 0)
        item.setText(_translate("Form", "ZFlag", None))
        item = self.tableWidget_2.item(3, 1)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget_2.item(4, 0)
        item.setText(_translate("Form", "NZFlag", None))
        item = self.tableWidget_2.item(4, 1)
        item.setText(_translate("Form", "0", None))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Flags", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Symbol Table", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Pool Table", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "Stack", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "1st Pass", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Form", "2nd Pass Obj File", None))
        self.label_4.setText(_translate("Form", "Program Counter", None))
        self.label_5.setText(_translate("Form", "Location Counter", None))
        self.pushButton.setText(_translate("Form", "One Step + 1st Pass ", None))
        self.pushButton_2.setText(_translate("Form", "Loader", None))
        self.pushButton_3.setText(_translate("Form", "Linker", None))
        self.pushButton_4.setText(_translate("Form", "Reset", None))
        self.pushButton_5.setText(_translate("Form", "Final Machine Code", None))
        self.pushButton_6.setText(_translate("Form", "2nd Pass Obj File", None))

    def showdialog(self, message):
        msg =QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)

        msg.setText(message)
        msg.setInformativeText("Info Box!")
        msg.setWindowTitle("Stop!")
        msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        retval = msg.exec_()

    def highlight(self, data):
        self.plainTextEdit.script_cursor = QtGui.QTextCursor(self.plainTextEdit.document())
        self.plainTextEdit.setTextCursor(self.plainTextEdit.script_cursor)
        self.plainTextEdit.script_cursor.movePosition(QtGui.QTextCursor.Start)
        for i in range(data):
            self.plainTextEdit.script_cursor.movePosition(QtGui.QTextCursor.Down)

        self.plainTextEdit.script_cursor.movePosition(QtGui.QTextCursor.EndOfLine)
        self.plainTextEdit.script_cursor.movePosition(QtGui.QTextCursor.StartOfLine, QtGui.QTextCursor.KeepAnchor)
        tmp = self.plainTextEdit.script_cursor.blockFormat()
        tmp.setBackground(QtGui.QBrush(QtCore.Qt.lightGray))
        self.plainTextEdit.script_cursor.setBlockFormat(tmp)

    def unhighlight(self, data):
        self.plainTextEdit.script_cursor = QtGui.QTextCursor(self.plainTextEdit.document())
        self.plainTextEdit.setTextCursor(self.plainTextEdit.script_cursor)
        self.plainTextEdit.script_cursor.movePosition(QtGui.QTextCursor.Start)
        for i in range(data):
            self.plainTextEdit.script_cursor.movePosition(QtGui.QTextCursor.Down)

        self.plainTextEdit.script_cursor.movePosition(QtGui.QTextCursor.EndOfLine)
        self.plainTextEdit.script_cursor.movePosition(QtGui.QTextCursor.StartOfLine, QtGui.QTextCursor.KeepAnchor)
        tmp = self.plainTextEdit.script_cursor.blockFormat()
        tmp.setBackground(QtGui.QBrush(QtCore.Qt.white))
        self.plainTextEdit.script_cursor.setBlockFormat(tmp)

    def updateRegsFlagsAndPC(self, reset = False):
        for i in range(5):
            item = self.tableWidget_2.item(i, 1)
            item.setText(_translate("Form", str(self.flags[i]), None))
        for j in range(8):
            regsName = ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'L']
            item = self.tableWidget.item(j, 1)
            if(type(self.regs[regsName[j]]) == str):
                item.setText(_translate("Form", self.regs[regsName[j]], None))
            else:
                item.setText(_translate("Form", str('{0:08b}'.format(self.regs[regsName[j]])), None))
        self.lcdNumber.display(self.PC)
        table = self.symbolTable.keys()
        if reset == False:
            for i in range(len(table)):
                item = self.tableWidget_3.item(i, 0)
                item.setText(_translate("Form", str(table[i]), None))
                item = self.tableWidget_3.item(i, 1)
                item.setText(_translate("Form", str(self.symbolTable[table[i]]), None))
            #table2 = self.varsInt.keys()
            table2 = self.poolList.keys()
            for i in range(len(table2)):
                item = self.tableWidget_4.item(i, 0)
                item.setText(_translate("Form", str(table2[i]), None))
                item = self.tableWidget_4.item(i, 1)
                item.setText(_translate("Form", str(self.poolList[table2[i]]), None))
            table3 = self.stack
            for i in range(len(table3)):
                item = self.tableWidget_5.item(i, 0)
                item.setText(_translate("Form", str('{0:08b}'.format(i)), None))
                item = self.tableWidget_5.item(i, 1)
                item.setText(_translate("Form", str(self.stack[-i-1]), None))
        else:
            for i in range(len(table)):
                item = self.tableWidget_3.item(i, 0)
                item.setText(_translate("Form", "", None))
                item = self.tableWidget_3.item(i, 1)
                item.setText(_translate("Form", "", None))
            table2 = self.poolList.keys()
            for i in range(len(table2)):
                item = self.tableWidget_4.item(i, 0)
                item.setText(_translate("Form", "", None))
                item = self.tableWidget_4.item(i, 1)
                item.setText(_translate("Form", "", None))
            table3 = self.stack
            for i in range(len(table3)):
                item = self.tableWidget_5.item(i, 0)
                item.setText(_translate("Form", str('{0:08b}'.format(i)), None))
                item = self.tableWidget_5.item(i, 1)
                item.setText(_translate("Form", "", None))

    def loader(self):
        minOff = 0
        try:
            pool = self.poolList.values()
            maxaddr1 = max(pool)
            symb = self.symbolTable.values()
            maxaddr2 = max(symb)
            minOff = max(maxaddr1, maxaddr2)
        except:
            pass
        self.getint("Loader Offset", "Enter Offset for loading (more than %d): " % minOff)
        self.loaded = load(self.linked, load_origin = self.getIntVal)
        filesInDir = os.listdir("./LoadFiles/")
        k=1
        string0 ="test"+str(k) + ".load"
        while string0 in filesInDir:
            k+=1
            string0 = "test"+str(k) + ".load"
        finalFile = open("./LoadFiles/"+string0,"w+")
        print "Loader file written in " + string0
        finalFile.write(self.loaded)

    def getint(self, title = "Integer Input Dialog", prompt = "enter a number"):
        num,ok = QtGui.QInputDialog.getInt(self.plainTextEdit_2 , title, prompt)
        if ok:
            self.getIntVal = int(num)

    def linker(self):
        minOff = 0
        try:
            pool = self.poolList.values()
            maxaddr1 = max(pool)
            symb = self.symbolTable.values()
            maxaddr2 = max(symb)
            minOff = max(maxaddr1, maxaddr2)
        except:
            pass
        self.getint("Linker Offset", "Enter Offset for linking (more than %d): " % minOff)
        self.linked = link(self.macroProcessed, link_origin = self.getIntVal)
        filesInDir = os.listdir("./LinkFiles/")
        k=1
        string0 ="test"+str(k) + ".link"
        while string0 in filesInDir:
            k+=1
            string0 = "test"+str(k) + ".link"
        finalFile = open("./LinkFiles/"+string0,"w+")
        print "Linker file written in " + string0
        finalFile.write(self.linked)

    def machine(self):
        #tb2 = str(self.plainTextEdit_2.toPlainText())
        machineCode = convertToMachine(self.loaded, self.symbolTable)
        filesInDir = os.listdir("./MachineFiles/")
        k=1
        string0 ="test"+str(k) + ".machine"
        while string0 in filesInDir:
            k+=1
            string0 = "test"+str(k) + ".machine"
        finalFile = open("./MachineFiles/"+string0,"w+")
        print "Machine File written to " + string0
        finalFile.write(machineCode)

    def secPass(self):
        tb2 = str(self.plainTextEdit_2.toPlainText())
        lines = tb2.split("\n")
        for lineNum in range(len(lines)):
            if "LTORG" in lines[lineNum]:
                self.processLiterals()
            if "ORIGIN" in lines[lineNum]:
                pos = int(lines[lineNum].split()[1])
                self.byteLen = pos
            if "JMP" in lines[lineNum] or "JNZ" in lines[lineNum] or "JZ" in lines[lineNum] or "JP" in lines[lineNum] or "JN" in lines[lineNum]:
                tag = lines[lineNum].split()[1].strip()
                lines[lineNum] = lines[lineNum].replace(tag, hex(int(self.symbolTable[tag])))
                #####
                operands = lines[lineNum].split()[1:]
                for operand in operands:
                    operand = operand.strip(',')
                    if operand in self.poolList.keys():
                        lines[lineNum] = lines[lineNum].replace(operand, str(hex(self.poolList[operand])))
                #####
        secPassCode = ""
        for line in lines:
            secPassCode+=(line+"\n")
        self.plainTextEdit_4.setPlainText(QtCore.QString(secPassCode))
        print "------------------------------Second Pass O/P------------------------------"
        print secPassCode
        self.macroProcessed = expandMacro(self)
        objectCode = convertToMachine(self.macroProcessed, self.symbolTable)
        self.plainTextEdit_4.setPlainText(QtCore.QString(objectCode))


    def reset(self):
        for i in range(self.PC-1):
            self.unhighlight(i)
        self.plainTextEdit_2.setPlainText(QtCore.QString(""))
        self.updateRegsFlagsAndPC(reset = True)
        self.byteLen = self.offset1
        self.regs = {'A' : 0, 'B' : 0, 'C' : 0, 'D' : 0, 'E' : 0, 'F' : 0, 'H' : 0, 'L' : 0,}
        self.flags = [0 for i in range(5)]
        self.PC = 1
        self.WORDCount = 0
        self.mainPart ="START:\n"
        self.dataPart = ""
        self.firstPassMain = ""
        self.firstPassData = ""
        self.varsInt = {}
        self.varsChar = {}
        self.mapping = {}
        self.symbolTable = {"START":self.offset1}
        self.conditionCount = 0
        self.lastCondition = []
        self.lastloop = []
        self.loopCount = 0
        self.poolList = {}
        self.plainTextEdit_3.setPlainText(QtCore.QString(""))
        self.plainTextEdit_4.setPlainText(QtCore.QString(""))
        self.showdialog("PC has been reset!")

    def onestep(self):
        self.unhighlight(self.PC-2)
        self.highlight(self.PC-1)
        tb1 = str(self.plainTextEdit.toPlainText())
        if(self.PC==1):
            filesInDir = os.listdir("./TestFiles/")
            k=1
            string0 ="test"+str(k) + ".c"
            while string0 in filesInDir:
                k+=1
                string0 = "test"+str(k) + ".c"
            finalFile = open("./TestFiles/"+string0,"w+")
            finalFile.write(tb1)
        lines = tb1.split("\n")
        try:
            self.call(lines[self.PC-1], self.varsInt, self.varsChar)
        except:
            self.dataPart+=("HLT\n")
            #self.symbolTable["END"] = self.byteLen
            self.processLiterals()
            self.updateRegsFlagsAndPC()
            self.plainTextEdit_2.setPlainText(QtCore.QString(self.mainPart + self.dataPart))
            self.firstPass()
            self.showdialog("PC reached End!")
            filesInDir = os.listdir("./AssemblerFiles/")
            k=1
            string1 ="File"+str(k) + ".asm"
            while string1 in filesInDir:
                k+=1
                string1 = "File"+str(k) + ".asm"
            finalFile = open("./AssemblerFiles/" + string1,"w+")
            finalFile.write(self.mainPart  + self.dataPart)
        self.PC += 1

    def firstPass(self):
        assembled = str(self.plainTextEdit_2.toPlainText())
        lines = assembled.split('\n')
        for line in lines:
            if line.startswith('ADDI'):
                self.firstPassMain+="(IS, 00)" + line.replace('ADDI', '(') + ")\n"
            if line.startswith('ANI'):
                self.firstPassMain+="(IS, 01)" + line.replace('ANI', '(') + ")\n"
            if line.startswith('JMP'):
                self.firstPassMain+="(IS, 02)" + line.replace('JMP', '(') + ")\n"
            if line.startswith('JNZ'):
                self.firstPassMain+="(IS, 03)" + line.replace('JNZ', '(') + ")\n"
            if line.startswith('JZ'):
                self.firstPassMain+="(IS, 04)" + line.replace('JZ', '(') + ")\n"
            if line.startswith('JP'):
                self.firstPassMain+="(IS, 05)" + line.replace('JP', '(') + ")\n"
            if line.startswith('HLT'):
                self.firstPassMain+="(IS, 06)\n"
            if line.startswith('SUI'):
                self.firstPassMain+="(IS, 07)" + line.replace('SUI', '(') + ")\n"
            if line.startswith('ADD'):
                self.firstPassMain+="(IS, 08)" + line.replace('ADD', '(') + ")\n"
            if line.startswith('ANA'):
                self.firstPassMain+="(IS, 09)" + line.replace('ANA', '(') + ")\n"
            if line.startswith('SUB'):
                self.firstPassMain+="(IS, 10)" + line.replace('SUB', '(') + ")\n"
            if line.startswith('POP'):
                self.firstPassMain+="(IS, 11)\n"
            if line.startswith('PUSH'):
                self.firstPassMain+="(IS, 12)" + line.replace('PUSH', '(') + ")\n"
            if line.startswith('MVI'):
                self.firstPassMain+="(IS, 13)" + line.replace('MVI', '(') + ")\n"
            if line.startswith('MOV'):
                self.firstPassMain+="(IS, 14)" + line.replace('MOV', '(') + ")\n"
            if line.startswith('ORA'):
                self.firstPassMain+="(IS, 15)" + line.replace('ORA', '(') + ")\n"
            if line.startswith('LDA'):
                self.firstPassMain+="(IS, 16)" + line.replace('LDA', '(') + ")\n"
            if line.startswith('LI'):
                self.firstPassMain+="(IS, 17)" + line.replace('LI', '(') + ")\n"
            if line.startswith('SYSCALL'):
                self.firstPassMain+="(AD, 06)\n"
            if line.startswith('START'):
                self.firstPassMain+="(AD, 01)\n"
            if line.startswith('LTORG'):
                self.firstPassMain+="(AD, 05)\n"
            if line.startswith('END'):
                self.firstPassMain+="(AD, 02)\n"
            if 'WORD' in line:
                self.firstPassData+="(DL, 01)\n"
            elif 'DB' in line:
                self.firstPassData+="(DL, 02)\n"
            elif 'DQ' in line:
                self.firstPassData+="(DL, 03)\n"
            elif 'DC ' in line:
                self.firstPassData+="(DL, 04)\n"
            elif 'LCL ' in line:
                self.firstPassData+="(DL, 05)\n"
        self.plainTextEdit_3.setPlainText(QtCore.QString(self.firstPassMain+self.firstPassData))

    def processLiterals(self):
        lines = self.dataPart.split("\n")
        self.lcdNumber_2.display(self.byteLen)
        for line in lines:
            if "DB" in line or "DQ" in line:
                if "WORD" in line:
                    entry = line.split()
                    entryName = entry[0].strip()
                    entryLen = entry[-1].strip()
                    self.poolList[entryName] = self.byteLen
                    self.byteLen += int(entryLen)
                else:
                    if "DB" in line:
                        entry = line.split()
                        entryName = entry[0].strip()
                        self.poolList[entryName] = self.byteLen
                        self.byteLen += 2
                    elif "DQ" in line:
                        entry = line.split()
                        entryName = entry[0].strip()
                        self.poolList[entryName] = self.byteLen
                        self.byteLen += 4
                    elif "DC " in line:
                        entry = line.split()
                        entryName = entry[0].strip()
                        self.poolList[entryName] = self.byteLen
                        self.byteLen += 1


    def call(self, i, varsInt, varsChar):
        #print self.poolList, self.varsInt
        self.flags = [0,0,0,0,0]
        if self.macroTrigger == True:
            #self.MDT[-1] += (i+"\n")
            if ("int " in i) and ("print" not in i):
                temp = (i.split("int"))[1]
                ar = (re.search('[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz][ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890]*(?=[ ;\=])', temp).group(0)).strip()
                br = (re.search('\=[1234567890 ]*(?=[; ])', temp).group(0)).strip()
                br = br.split("=")[1]
                self.mainPart += "LCL &" + ar+"\n"
                self.EVTAB.append("&" + ar)
                self.mainPart += "&" + ar + " SET " + str(br) + "\n"
                self.MDT[-1] += "LCL &" + ar+"\n"
                self.MDT[-1] += "&" + ar + " SET " + str(br) + "\n"
                # self.poolList[ar] = self.byteLen
                # self.byteLen+=2
                try:
                    varsInt["&" + ar] = int(br)
                except:
                    varsInt["&" + ar] = 0
            elif "+" in i and "=" in i and ";" in i:
                ar = i.split("=")
                v = ar[0]
                a = v.strip()
                b,c = ar[1].strip().split("+")
                c = c.split(";")[0]
                c = c.strip()
                b = b.strip()
                a = a.strip()
                if ("&" + b) in self.PNTAB[-1]:
                    b = "&" + b
                elif ("&" + b) in varsInt:
                    b = "&" + b
                if ("&" + c) in self.PNTAB[-1]:
                    c = "&" + c
                elif ("&" + c) in varsInt:
                    c = "&" + c
                a = "&" + a
                # if constantsNum==0:
                #     self.mainPart+=("MOV A, "+ b + "\n")
                #     self.byteLen+=1
                #     self.mainPart+=("MOV B, "+ c+ "\n")
                #     self.byteLen+=1
                #     self.mainPart+=("ADD A, B\n")
                #     self.byteLen+=1
                #     self.mainPart+=("MOV "+a + ", A\n")
                #     self.byteLen+=1
                # elif(constantsNum==1):
                #     if(markB):
                #         self.mainPart+=("MOV A, "+c+ "\n")
                #         self.byteLen+=1
                #         self.mainPart+=("ADD A, "+str(constants[0])+"\n")
                #         self.byteLen+=2
                #         self.mainPart+=("MOV "+a+ ", A\n")
                #         self.byteLen+=1
                #     else:
                #         self.mainPart+=("MOV A, "+b+ "\n")
                #         self.byteLen+=1
                #         self.mainPart+=("ADD A, "+str(constants[0])+"\n")
                #         self.byteLen+=2
                #         self.mainPart+=("MOV "+a + ", A\n")
                #         self.byteLen+=1
                # else:
                self.mainPart+=("MOV A, "+  b + "\n")
                self.MDT[-1] += ("MOV A, "+  b + "\n")
                self.byteLen+=1
                self.mainPart+=("MOV B, "+  c + "\n")
                self.MDT[-1] += ("MOV B, "+  c + "\n")
                self.byteLen+=1
                self.mainPart+=("ADD B\n")
                self.MDT[-1] += ("ADD B\n")
                self.byteLen+=1
                self.mainPart+=("MOV "+ a + ", A\n")
                self.MDT[-1] += ("MOV "+  a + ", A\n")
                self.byteLen+=1
            elif "-" in i and "=" in i and ";" in i:
                ar = i.split("=")
                v = ar[0]
                a = v.strip()
                b,c = ar[1].strip().split("+")
                c = c.split(";")[0]
                c = c.strip()
                b = b.strip()
                a = a.strip()
                if ("&" + b) in self.PNTAB[-1]:
                    b = "&" + b
                elif ("&" + b) in varsInt:
                    b = "&" + b
                if ("&" + c) in self.PNTAB[-1]:
                    c = "&" + c
                elif ("&" + c) in varsInt:
                    c = "&" + c
                a = "&" + a
                # if constantsNum==0:
                #     self.mainPart+=("MOV A, "+ b + "\n")
                #     self.byteLen+=1
                #     self.mainPart+=("MOV B, "+ c+ "\n")
                #     self.byteLen+=1
                #     self.mainPart+=("ADD A, B\n")
                #     self.byteLen+=1
                #     self.mainPart+=("MOV "+a + ", A\n")
                #     self.byteLen+=1
                # elif(constantsNum==1):
                #     if(markB):
                #         self.mainPart+=("MOV A, "+c+ "\n")
                #         self.byteLen+=1
                #         self.mainPart+=("ADD A, "+str(constants[0])+"\n")
                #         self.byteLen+=2
                #         self.mainPart+=("MOV "+a+ ", A\n")
                #         self.byteLen+=1
                #     else:
                #         self.mainPart+=("MOV A, "+b+ "\n")
                #         self.byteLen+=1
                #         self.mainPart+=("ADD A, "+str(constants[0])+"\n")
                #         self.byteLen+=2
                #         self.mainPart+=("MOV "+a + ", A\n")
                #         self.byteLen+=1
                # else:
                self.mainPart+=("MOV A, "+  b + "\n")
                self.MDT[-1] += ("MOV A, "+  b + "\n")
                self.byteLen+=1
                self.mainPart+=("MOV B, "+  c + "\n")
                self.MDT[-1] += ("MOV B, "+  c + "\n")
                self.byteLen+=1
                self.mainPart+=("SUB B\n")
                self.MDT[-1] += ("SUB B\n")
                self.byteLen+=1
                self.mainPart+=("MOV "+ a + ", A\n")
                self.MDT[-1] += ("MOV "+  a + ", A\n")
                self.byteLen+=1
            elif "print" in i:
                if '\"' not in i:
                    ar = (re.search('(?<=print) [ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz][ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890]*', i).group(0)).strip()
                    if(ar in varsInt.keys()):
                        self.mainPart+=("MOV A, " + ar + "\n")
                        self.byteLen+=1
                        self.regs['A'] = varsInt[ar]
                        lent = 0
                        toPrint = ""
                        lent = 2
                        self.mainPart+=("LI D, " + str(lent) + "\n")
                        self.byteLen+=2
                        self.mainPart+=("MOV C, " + ar + "\n")
                        self.byteLen+=1+lent
                        self.regs['D'] = lent
                        self.regs['E'] = self.regs['A']
                        self.mainPart+=("SYSCALL\n")
                        self.byteLen+=1
                    else:
                        self.mainPart+=("MOV A, " +ar + "\n")
                        self.byteLen+=1
                        self.regs['A'] = ord(varsChar[ar])
                        lent = 1
                        toPrint = ""
                        self.mainPart+=("LI D, " + str(lent) + "\n")
                        self.byteLen+=2
                        self.mainPart+=("MOV C, " + ar + "\n")
                        self.byteLen+=1+lent
                        self.regs['D'] = lent
                        self.regs['E'] = self.regs['A']
                        self.mainPart+=("SYSCALL\n")
                        self.byteLen+=1
                else:
                    ar = (re.search('(?<=print) \"[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 ]*\"*', i).group(0)).strip()
                    toPrint = ar.strip("\"")
                    lent = len(toPrint)
                    self.dataPart+=("WORD" + str(self.WORDCount+1) + " DB '"+toPrint+"' "+str(lent)+"\n")
                    # self.poolList["WORD" + str(self.WORDCount+1)] = self.byteLen
                    # self.byteLen+=lent
                    self.mainPart+=("LI D, " + str(hex(lent)) + "\n")
                    self.byteLen+=2
                    self.mainPart+=("MOV C, " + "WORD"+ str(self.WORDCount+1) + "\n")
                    self.byteLen+=1
                    self.regs['H'] = ord(toPrint[-2])
                    self.regs['L'] = ord(toPrint[-1])
                    self.regs['D'] = lent
                    self.regs['E'] = ord(toPrint[-1])
                    self.mainPart+=("SYSCALL\n")
                    self.byteLen+=1
                    self.WORDCount+=1
        elif "load" in i:
            self.mainPart+="LTORG\n"
            self.processLiterals()
            self.updateRegsFlagsAndPC()
        elif ("int " in i or "char " in i or "long " in i ) and ("print" not in i) and ("+" not in i) and ("-" not in i) and ("*" not in i) and ("/" not in i):
            if ("int " in i) and ("print" not in i):
                temp = (i.split("int"))[1]
                ar = (re.search('[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz][ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890]*(?=[ ;\=])', temp).group(0)).strip()
                br = (re.search('\=[1234567890 ]*(?=[; ])', temp).group(0)).strip()
                br = br.split("=")[1]
                self.dataPart += ar+ " DB " + br+"\n"
                # self.poolList[ar] = self.byteLen
                # self.byteLen+=2
                try:
                    varsInt[ar] = int(br)
                except:
                    varsInt[ar] = 0
            if "long " in i:
                temp = (i.split("long"))[1]
                ar = (re.search('[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz][ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 ]*(?=[ ;\=])', temp).group(0)).strip()
                br = (re.search('\=[1234567890 ]*(?=[; ])', temp).group(0)).strip()
                br = br.split("=")[1]
                self.dataPart += ar+ " DQ " + br+"\n"
                # self.poolList[ar] = self.byteLen
                # self.byteLen+=2
                try:
                    varsInt[ar] = int(br)
                except:
                    varsInt[ar] = 0
            if "char " in i:
                temp = (i.split("char"))[1]
                ar = (re.search('[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz][ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 ]*(?=[ ;\=])', temp).group(0)).strip()
                br = (re.search('\= \'[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ]\'(?=[ ;])', temp).group(0)).strip()
                br = (br.split("=")[1]).strip().strip("'")
                # self.poolList[ar] = self.byteLen
                # self.byteLen+=1
                self.dataPart += ar+ " DC " + br+"\n"
                try:
                    varsChar[ar] = br
                except:
                    varsChar[ar] = ''
                #print varsChar
        elif "=" in i and "+" not in i and "-" not in i and ";" in i and "or" not in i and "and" not in i:
            ar, br = i.split("=")
            ar = ar. strip()
            br = br.strip(";").strip()
            varsInt[ar] = int(br)
            self.mainPart+=("LDA "+str(br) + "\n")
            self.byteLen+=1
            self.mainPart+=("MOV "+ar+", A\n")
            self.byteLen+=1
            self.regs['A'] = br
            self.regs['L'] = br
        elif "=" in i and '+' in i and ';' in i:
            ar = i.split("=")
            v = ar[0]
            a = v.strip()
            b,c = ar[1].strip().split("+")
            c = c.split(";")[0]
            c = c.strip()
            b = b.strip()
            a = a.strip()
            temp1 = 0
            temp2 = 0
            constantsNum = 0
            constants = []
            markB = False
            if b in varsInt.keys():
                temp1 = varsInt[b]
            else:
                constantsNum += 1
                constants.append(int(b.strip()))
                markB = True
            if c in varsInt.keys():
                temp2 = varsInt[c]
            else:
                constantsNum += 1
                constants.append(int(c.strip()))
            if constantsNum==0:
                varsInt[a] = temp1+temp2
                self.mainPart+=("MOV A, "+ b + "\n")
                self.byteLen+=1
                self.mainPart+=("MOV B, "+ c+ "\n")
                self.byteLen+=1
                self.mainPart+=("ADD B\n")
                self.byteLen+=1
                self.mainPart+=("MOV "+a + ", A\n")
                self.byteLen+=1
                self.regs['A'] = temp1+temp2
                if (temp1 + temp2) == 0:
                    self.flags[3] = 1
                else:
                    self.flags[4] = 1
                self.regs['B'] = temp2
                self.regs['L'] = self.regs['A']
            elif(constantsNum==1):
                if(markB):
                    varsInt[a] = constants[0] + temp2
                    self.mainPart+=("MOV A, "+c+ "\n")
                    self.byteLen+=1
                    self.mainPart+=("ADDI "+str(constants[0])+"\n")
                    self.byteLen+=2
                    self.mainPart+=("MOV "+a+ ", A\n")
                    self.byteLen+=1
                    self.regs['A'] = constants[0] + temp2
                    if (constants[0] + temp2) == 0:
                        self.flags[3] = 1
                    else:
                        self.flags[4] = 1
                    self.regs['L'] = self.regs['A']
                else:
                    varsInt[a] = constants[0] + temp1
                    self.mainPart+=("MOV A, "+b+ "\n")
                    self.byteLen+=1
                    self.mainPart+=("ADDI "+str(constants[0])+"\n")
                    self.byteLen+=2
                    self.mainPart+=("MOV "+a + ", A\n")
                    self.byteLen+=1
                    self.regs['A'] = constants[0] + temp2
                    if (constants[0] + temp2) == 0:
                        self.flags[3] = 1
                    else:
                        self.flags[4] = 1
                    self.regs['L'] = self.regs['A']
            else:
                varsInt[a] = constants[0] + constants[1]
                self.mainPart+=("LI A, "+  str(constants[0]) + "\n")
                self.byteLen+=2
                self.mainPart+=("ADDI " +str(constants[1])+"\n")
                self.byteLen+=2
                self.mainPart+=("MOV "+ a + ", A\n")
                self.byteLen+=1
                self.regs['A'] = constants[0] + constants[1]
                if (constants[0] + constants[1]) == 0:
                    self.flags[3] = 1
                else:
                    self.flags[4] = 1
                self.regs['L'] = self.regs['A']
        elif "=" in i and '-' in i and ';' in i:
            ar = i.split("=")
            v = ar[0]
            a = v.strip()
            b,c = ar[1].strip().split("-")
            c = c.split(";")[0]
            c = c.strip()
            b = b.strip()
            a = a.strip()
            temp1 = 0
            temp2 = 0
            constantsNum = 0
            constants = []
            markB = False
            if b in varsInt.keys():
                temp1 = varsInt[b]
            else:
                constantsNum += 1
                constants.append(int(b.strip()))
                markB = True
            if c in varsInt.keys():
                temp2 = varsInt[c]
            else:
                constantsNum += 1
                constants.append(int(c.strip()))
            if constantsNum==0:
                varsInt[a] = temp1-temp2
                self.mainPart+=("MOV A, "+ b + "\n")
                self.byteLen+=1
                self.mainPart+=("MOV B, "+ c + "\n")
                self.byteLen+=1
                self.mainPart+=("SUB B\n")
                self.byteLen+=1
                self.mainPart+=("MOV "+a + ", A\n")
                self.byteLen+=1
                self.regs['A'] = temp1-temp2
                if (temp1 - temp2) == 0:
                    self.flags[3] = 1
                else:
                    self.flags[4] = 1
                self.regs['B'] = temp2
                self.regs['L'] = self.regs['A']
            elif(constantsNum==1):
                if(markB):
                    varsInt[a] = constants[0] - temp2
                    self.mainPart+=("MOV A, "+c+ "\n")
                    self.byteLen+=1
                    self.mainPart+=("SUI "+str(constants[0])+"\n")
                    self.byteLen+=2
                    self.mainPart+=("MOV "+a + ", A\n")
                    self.byteLen+=1
                    self.regs['A'] = constants[0] - temp2
                    if (constants[0] - temp2) == 0:
                        self.flags[3] = 1
                    else:
                        self.flags[4] = 1
                    self.regs['L'] = self.regs['A']
                else:
                    varsInt[a] = temp1 - constants[0] 
                    self.mainPart+=("MOV A, "+b+ "\n")
                    self.byteLen+=1
                    self.mainPart+=("SUI "+str(constants[0])+"\n")
                    self.byteLen+=2
                    self.mainPart+=("MOV "+a + ", A\n")
                    self.byteLen+=1
                    self.regs['A'] = constants[0] - temp2
                    if (constants[0] - temp2) == 0:
                        self.flags[3] = 1
                    else:
                        self.flags[4] = 1
                    self.regs['L'] = self.regs['A']
            else:
                varsInt[a] = constants[0] - constants[1]
                self.mainPart+=("LI A, "+  str(constants[0]) + "\n")
                self.byteLen+=2
                self.mainPart+=("SUI " +str(constants[1])+"\n")
                self.byteLen+=2
                self.mainPart+=("MOV "+ a+ ", A\n")
                self.byteLen+=1
                self.regs['A'] = constants[0] - constants[1]
                if (constants[0] - constants[1]) == 0:
                    self.flags[3] = 1
                else:
                    self.flags[4] = 1
                self.regs['L'] = self.regs['A']
        elif "or " in i and ";" in i:
            ar = i.split("=")
            v = ar[0]
            a = v.strip()
            b,c = ar[1].strip().split("or")
            c = c.split(";")[0]
            c = c.strip()
            b = b.strip()
            a = a.strip()
            b = int(b)
            c = int(c)
            varsInt[a] = b or c
            self.mainPart+=("LI A, " + str(b) + "\n")
            self.byteLen+=2
            self.mainPart+=("LI B, " + str(c) + "\n")
            self.byteLen+=2
            self.regs['B'] = c
            self.mainPart+=("ORA B\n")
            self.byteLen+=1
            self.regs['A'] = b or c
            self.mainPart+=("MOV " + a + ", A\n")
            self.byteLen+=1
        elif "and " in i and ";" in i:
            ar = i.split("=")
            v = ar[0]
            a = v.strip()
            b,c = ar[1].strip().split("and")
            c = c.split(";")[0]
            c = c.strip()
            b = b.strip()
            a = a.strip()
            b = int(b)
            c = int(c)
            varsInt[a] = b and c
            self.mainPart+=("LI A, " + str(b) + "\n")
            self.byteLen+=2
            self.mainPart+=("LI B, " + str(c) + "\n")
            self.byteLen+=2
            self.regs['B'] = c
            self.mainPart+=("ANA B\n")
            self.byteLen+=1
            self.regs['A'] = b and c
            self.mainPart+=("MOV " + a + ", A\n")
            self.byteLen+=1
        elif "print " in i:
            if '\"' not in i:
                ar = (re.search('(?<=print) [ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz][ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890]*', i).group(0)).strip()
                if(ar in varsInt.keys()):
                    self.mainPart+=("MOV A, " + ar + "\n")
                    self.byteLen+=1
                    self.regs['A'] = varsInt[ar]
                    lent = 0
                    toPrint = ""
                    lent = 2
                    self.mainPart+=("LI D, " + str(lent) + "\n")
                    self.byteLen+=2
                    self.mainPart+=("MOV C, " + ar + "\n")
                    self.byteLen+=1+lent
                    self.regs['D'] = lent
                    self.regs['E'] = self.regs['A']
                    self.mainPart+=("SYSCALL\n")
                    self.byteLen+=1
                else:
                    self.mainPart+=("MOV A, " +ar + "\n")
                    self.byteLen+=1
                    self.regs['A'] = ord(varsChar[ar])
                    lent = 1
                    toPrint = ""
                    self.mainPart+=("LI D, " + str(lent) + "\n")
                    self.byteLen+=2
                    self.mainPart+=("MOV C, " + ar + "\n")
                    self.byteLen+=1+lent
                    self.regs['D'] = lent
                    self.regs['E'] = self.regs['A']
                    self.mainPart+=("SYSCALL\n")
                    self.byteLen+=1
            else:
                ar = (re.search('(?<=print) \"[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 ]*\"*', i).group(0)).strip()
                toPrint = ar.strip("\"")
                lent = len(toPrint)
                self.dataPart+=("WORD" + str(self.WORDCount+1) + " DB '"+toPrint+"' "+str(lent)+"\n")
                # self.poolList["WORD" + str(self.WORDCount+1)] = self.byteLen
                # self.byteLen+=lent
                self.mainPart+=("LI D, " + str(hex(lent)) + "\n")
                self.byteLen+=2
                self.mainPart+=("MOV C, " + "WORD"+ str(self.WORDCount+1) + "\n")
                self.byteLen+=1
                self.regs['H'] = ord(toPrint[-2])
                self.regs['L'] = ord(toPrint[-1])
                self.regs['D'] = lent
                self.regs['E'] = ord(toPrint[-1])
                self.mainPart+=("SYSCALL\n")
                self.byteLen+=1
                self.WORDCount+=1
        elif "import " in i:
            fexts = open("exported.extrn", "r+")
            varName = i.split()[1].strip()
            varVal = 0
            exportedVars = fexts.read().split("\n")
            for var in exportedVars:
                try:
                    name,val = var.strip().split()
                    if name == varName:
                        if ord(val[0]) > 57:
                            self.varsChar[name] = val
                        else:
                            self.varsInt[name] = int(val)
                        self.poolList[name] = val
                except:
                    pass
            self.mainPart += (i.replace("import", "EXTERN?") + "\n")
            self.byteLen += 1
        elif "export " in i:
            fexts = open("exported.extrn", "a+")
            varName = i.split()[1].strip()
            varVal = 0
            if varName in varsInt.keys():
                varVal = varsInt[varName]
            else:
                varVal = varsChar[varName]
            fexts.write(varName + " " + str(varVal) + "\n")
            self.mainPart += (i.replace("export", "PUBLIC") + "\n")
            self.byteLen+=1
        elif ("if " in i) and ("endif" not in i):
            condition = "".join(i.split()[1:])
            op1 = ""
            op2 = ""
            if ">" in condition:
                op1,op2 = condition.split(">")
            elif "<" in condition:
                op1,op2 = condition.split("<")
            elif "==" in condition:
                op1,op2 = condition.split("==")
            cons = False
            try:
                a = varsInt[op1]
                b = varsInt[op2]
            except:
                cons = True
                try:
                    a = varsInt[op1]
                    b = int(op2.strip())
                except:
                    a = varsInt[op2]
                    b = int(op1.strip())
            if(a>b):
                self.flags[0] = 1
                self.flags[1] = 0
                self.flags[2] = 0
            elif(a<b):
                self.flags[0] = 0
                self.flags[1] = 1
                self.flags[2] = 0
            else:
                self.flags[0] = 0
                self.flags[1] = 0
                self.flags[2] = 1
            elsecond = ""
            endcond = ""
            if(cons==False):
                self.mainPart+=("MOV A, " + op1+ "\n")
                self.byteLen+=1
                self.mainPart+=("MOV B, "+op2+ "\n")
                self.byteLen+=1
                self.mainPart+=("SUB B\n")
                self.byteLen+=1
                elsecond = "ELSECONDITON" + str(self.conditionCount+1)
                endcond = "ENDCONDITON" + str(self.conditionCount+1)
                self.conditionCount+=1
                self.lastCondition.append(elsecond)
                self.lastCondition.append(endcond)
            else:
                self.mainPart+=("MOV A, " +op1 + "\n")
                self.byteLen+=1
                self.mainPart+=("LI B, " + str(b) + "\n")
                self.byteLen+=2
                self.mainPart+=("SUB B\n")
                self.byteLen+=1
                elsecond = "ELSECONDITON" + str(self.conditionCount+1)
                endcond = "ENDCONDITON" + str(self.conditionCount+1)
                self.conditionCount+=1
                self.lastCondition.append(elsecond)
                self.lastCondition.append(endcond)
            if(">" in condition):
                self.mainPart+=("JN "+ elsecond + "\n")
                self.byteLen+=1
                self.mainPart+=("JZ "+ elsecond + "\n")
                self.byteLen+=1
            elif("<" in condition):
                self.mainPart+=("JP "+ elsecond + "\n")
                self.byteLen+=1
                self.mainPart+=("JZ "+ elsecond + "\n")
                self.byteLen+=1
            elif("==" in condition):
                self.mainPart+=("JN "+ elsecond + "\n")
                self.byteLen+=1
                self.mainPart+=("JP "+ elsecond + "\n")
                self.byteLen+=1
        elif("else" in i):
            r =  self.lastCondition.pop()
            self.mainPart+=("JMP " + r + "\n")
            self.byteLen+=1
            tag = self.lastCondition.pop()
            self.mainPart+=("POP\n")
            self.lastCondition.append(r)
            self.mainPart+=(tag + ":\n")
            self.symbolTable[tag] = self.byteLen
            string2 = self.mainPart
            lines = string2.split("\n")
            for lineNum in range(len(lines)):
                if tag in lines[lineNum]:
                    injection = "PUSH " + str(hex(self.byteLen)) + "\n"
                    lines = lines[:lineNum] + [injection] + lines[lineNum:]
                    break
            self.mainPart = ""
            for i in lines:
                self.mainPart+=(i + "\n")
        elif("endif" in i):
            try:
                a = self.lastCondition[-1]
                b = self.lastCondition[-2]
                a = self.lastCondition.pop()
                b = self.lastCondition.pop()
                if b.startswith("ELSE"):
                    pass
                else:
                    self.lastCondition.append(b)
                self.mainPart+=(a + ":\n")
                self.mainPart+=("POP\n")
                self.symbolTable[a] = self.byteLen
                string2 = self.mainPart
                lines = string2.split("\n")
                for lineNum in range(len(lines)):
                    if a in lines[lineNum]:
                        injection = "PUSH " + str(hex(self.byteLen)) + "\n"
                        lines = lines[:lineNum] + [injection] + lines[lineNum:]
                        break
                self.mainPart = ""
                for i in lines:
                    self.mainPart+=(i + "\n")
            except:
                a = self.lastCondition.pop()
                self.mainPart+=(a + ":\n")
                self.symbolTable[a] = self.byteLen
                string2 = self.mainPart
                lines = string2.split("\n")
                for lineNum in range(len(lines)):
                    if a in lines[lineNum]:
                        injection = "PUSH " + str(hex(self.byteLen)) + "\n"
                        self.stack.append(a)
                        lines = lines[:lineNum] + [injection] + lines[lineNum:]
                        break
                self.mainPart = ""
                for i in lines:
                    self.mainPart+=(i + "\n")
        elif("loop" in i and "end" not in i):
            self.loopCount+=1
            num = int((i.split()[1]).strip())
            loopTag = "LOOP" + str(self.loopCount)
            self.mainPart+=("MVI C, " + str(num) + "\n")
            self.regs['C'] = num
            self.byteLen+=2
            self.mainPart+=(loopTag + ":\n")
            self.stack.append(loopTag)
            self.mainPart+=("PUSH " + str(hex(self.byteLen)) + "\n")
            self.symbolTable[loopTag] = self.byteLen
            self.lastloop.append(loopTag)
        elif("endloop" in i):
            self.mainPart+=("DCR C\n")
            self.flags[4] = 1
            self.byteLen+=1
            self.mainPart+=("JNZ " + self.lastloop.pop() + "\n")
            self.mainPart+=("POP\n")
            self.stack.pop()
            self.byteLen+=1
        if("func" in i and "end" not in i):
            self.macroTrigger = True
            funcVal = i.strip().split()[1:]
            self.MDT.append("")
            funcName = funcVal[0]
            funcArgs = funcVal[1:]
            self.mainPart+=("MACRO\n"+funcName + " &"+funcArgs[0] +", &"+ funcArgs[1] + ", &" + funcArgs[2] + "\n")
            self.MNT.append(funcName)
            self.PNTAB.append(["&" + funcArgs[0], "&" + funcArgs[1], "&" + funcArgs[2]])
        if "endfunc" in i:
            self.mainPart+=("MEND\n")
            self.macroTrigger = False
        if "call" in i:
            funcName, arg0, arg1, arg2 = i.split()[1:]
            self.APTAB.append([arg0, arg1, arg2])
            self.calls.append(funcName)
            self.mainPart += (funcName + " "+arg0 + ", " + arg1 + ", " + arg2 + "\n")

        self.updateRegsFlagsAndPC()
        self.plainTextEdit_2.setPlainText(QtCore.QString(self.mainPart + self.dataPart))