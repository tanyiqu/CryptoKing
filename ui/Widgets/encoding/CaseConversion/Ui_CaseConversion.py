# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'x:\Python\.Project\CryptoKing\ui\Widgets\encoding\CaseConversion\CaseConversion.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CaseConversion(object):
    def setupUi(self, CaseConversion):
        CaseConversion.setObjectName("CaseConversion")
        CaseConversion.resize(647, 527)
        CaseConversion.setMinimumSize(QtCore.QSize(90, 40))
        self.btn_upper = QtWidgets.QPushButton(CaseConversion)
        self.btn_upper.setGeometry(QtCore.QRect(20, 380, 90, 40))
        self.btn_upper.setMinimumSize(QtCore.QSize(90, 40))
        self.btn_upper.setMaximumSize(QtCore.QSize(90, 40))
        self.btn_upper.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_upper.setStyleSheet("QPushButton {\n"
"    border-radius: 4px;\n"
"    background-color: #66afe9;\n"
"    border: none;\n"
"    color: #FFFFFF;\n"
"    text-align: center;\n"
"    font: 11pt \"微软雅黑\";\n"
"    margin: 2px;\n"
"    vertical-align: middle;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    opacity: 1;\n"
"    right: 0;\n"
"    background-color: #1976d2;\n"
"}\n"
"")
        self.btn_upper.setObjectName("btn_upper")
        self.btn_lower = QtWidgets.QPushButton(CaseConversion)
        self.btn_lower.setGeometry(QtCore.QRect(120, 380, 90, 40))
        self.btn_lower.setMinimumSize(QtCore.QSize(90, 40))
        self.btn_lower.setMaximumSize(QtCore.QSize(90, 40))
        self.btn_lower.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_lower.setStyleSheet("QPushButton {\n"
"    border-radius: 4px;\n"
"    background-color: #66afe9;\n"
"    border: none;\n"
"    color: #FFFFFF;\n"
"    text-align: center;\n"
"    font: 11pt \"微软雅黑\";\n"
"    margin: 2px;\n"
"    vertical-align: middle;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    opacity: 1;\n"
"    right: 0;\n"
"    background-color: #1976d2;\n"
"}\n"
"")
        self.btn_lower.setObjectName("btn_lower")
        self.txt_left = QtWidgets.QPlainTextEdit(CaseConversion)
        self.txt_left.setGeometry(QtCore.QRect(20, 20, 591, 170))
        self.txt_left.setMinimumSize(QtCore.QSize(0, 170))
        self.txt_left.setMaximumSize(QtCore.QSize(16777215, 0))
        self.txt_left.setStyleSheet("QPlainTextEdit {\n"
"font-size: 14px;\n"
"color: #000;\n"
"font: 11pt \"微软雅黑\";\n"
"background-color: #ffffff;\n"
"border: 1px solid #cccccc;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"border-color: #66afe9;\n"
"outline: 0;\n"
"}")
        self.txt_left.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        self.txt_left.setObjectName("txt_left")
        self.txt_right = QtWidgets.QPlainTextEdit(CaseConversion)
        self.txt_right.setGeometry(QtCore.QRect(20, 200, 591, 170))
        self.txt_right.setMinimumSize(QtCore.QSize(0, 170))
        self.txt_right.setMaximumSize(QtCore.QSize(16777215, 250))
        self.txt_right.setStyleSheet("QPlainTextEdit {\n"
"font-size: 14px;\n"
"color: #000;\n"
"font: 11pt \"微软雅黑\";\n"
"background-color: #ffffff;\n"
"border: 1px solid #cccccc;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"border-color: #66afe9;\n"
"outline: 0;\n"
"}")
        self.txt_right.setReadOnly(True)
        self.txt_right.setObjectName("txt_right")

        self.retranslateUi(CaseConversion)
        QtCore.QMetaObject.connectSlotsByName(CaseConversion)
        CaseConversion.setTabOrder(self.btn_upper, self.btn_lower)

    def retranslateUi(self, CaseConversion):
        _translate = QtCore.QCoreApplication.translate
        CaseConversion.setWindowTitle(_translate("CaseConversion", "Form"))
        self.btn_upper.setText(_translate("CaseConversion", "全大写"))
        self.btn_lower.setText(_translate("CaseConversion", "全小写"))
        self.txt_left.setPlaceholderText(_translate("CaseConversion", "Input:"))
        self.txt_right.setPlaceholderText(_translate("CaseConversion", "Output:"))
