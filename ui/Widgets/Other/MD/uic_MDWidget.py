# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MDWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MDWidget(object):
    def setupUi(self, MDWidget):
        MDWidget.setObjectName("MDWidget")
        MDWidget.resize(758, 513)
        MDWidget.setMinimumSize(QtCore.QSize(90, 40))
        self.verticalLayout = QtWidgets.QVBoxLayout(MDWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(MDWidget)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 280))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_left = QtWidgets.QPlainTextEdit(self.widget)
        self.txt_left.setStyleSheet("QPlainTextEdit {\n"
"font-size: 14px;\n"
"color: #000;\n"
"font: 11pt \"微软雅黑\";\n"
"background-color: #ffffff;\n"
"border: 1px solid #cccccc;\n"
"border-radius: 4px;\n"
"-webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);\n"
"box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);\n"
"-webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;\n"
"transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"border-color: #66afe9;\n"
"outline: 0;\n"
"-webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);\n"
"box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);\n"
"}")
        self.txt_left.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        self.txt_left.setObjectName("txt_left")
        self.horizontalLayout.addWidget(self.txt_left)
        self.txt_right = QtWidgets.QPlainTextEdit(self.widget)
        self.txt_right.setMinimumSize(QtCore.QSize(0, 250))
        self.txt_right.setMaximumSize(QtCore.QSize(16777215, 250))
        self.txt_right.setStyleSheet("QPlainTextEdit {\n"
"font-size: 14px;\n"
"color: #000;\n"
"font: 11pt \"微软雅黑\";\n"
"background-color: #ffffff;\n"
"border: 1px solid #cccccc;\n"
"border-radius: 4px;\n"
"-webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);\n"
"box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);\n"
"-webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;\n"
"transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"border-color: #66afe9;\n"
"outline: 0;\n"
"-webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);\n"
"box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);\n"
"}")
        self.txt_right.setReadOnly(True)
        self.txt_right.setObjectName("txt_right")
        self.horizontalLayout.addWidget(self.txt_right)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(MDWidget)
        self.widget_2.setMaximumSize(QtCore.QSize(1111111, 58))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_encode = QtWidgets.QPushButton(self.widget_2)
        self.btn_encode.setMinimumSize(QtCore.QSize(90, 40))
        self.btn_encode.setMaximumSize(QtCore.QSize(90, 40))
        self.btn_encode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_encode.setStyleSheet("QPushButton {\n"
"    display: inline-block;\n"
"    border-radius: 4px;\n"
"    background-color: #66afe9;\n"
"    border: none;\n"
"    color: #FFFFFF;\n"
"    text-align: center;\n"
"    font: 11pt \"微软雅黑\";\n"
"    transition: all 0.5s;\n"
"    cursor: pointer;\n"
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
        self.btn_encode.setObjectName("btn_encode")
        self.horizontalLayout_2.addWidget(self.btn_encode)
        self.btn_decode = QtWidgets.QPushButton(self.widget_2)
        self.btn_decode.setMinimumSize(QtCore.QSize(90, 40))
        self.btn_decode.setMaximumSize(QtCore.QSize(90, 40))
        self.btn_decode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_decode.setStyleSheet("QPushButton {\n"
"    display: inline-block;\n"
"    border-radius: 4px;\n"
"    background-color: #66afe9;\n"
"    border: none;\n"
"    color: #FFFFFF;\n"
"    text-align: center;\n"
"    font: 11pt \"微软雅黑\";\n"
"    transition: all 0.5s;\n"
"    cursor: pointer;\n"
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
        self.btn_decode.setObjectName("btn_decode")
        self.horizontalLayout_2.addWidget(self.btn_decode)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.widget_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(MDWidget)
        QtCore.QMetaObject.connectSlotsByName(MDWidget)
        MDWidget.setTabOrder(self.txt_left, self.txt_right)
        MDWidget.setTabOrder(self.txt_right, self.btn_encode)
        MDWidget.setTabOrder(self.btn_encode, self.btn_decode)

    def retranslateUi(self, MDWidget):
        _translate = QtCore.QCoreApplication.translate
        MDWidget.setWindowTitle(_translate("MDWidget", "Form"))
        self.txt_left.setPlaceholderText(_translate("MDWidget", "Input:"))
        self.txt_right.setPlaceholderText(_translate("MDWidget", "Output:"))
        self.btn_encode.setText(_translate("MDWidget", "编码"))
        self.btn_decode.setText(_translate("MDWidget", "解码"))
