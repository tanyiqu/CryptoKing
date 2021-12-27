# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'x:\Python\.Project\CryptoKing\ui\Forms\MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(840, 580)
        Form.setStyleSheet("")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.w_head = QtWidgets.QFrame(Form)
        self.w_head.setMinimumSize(QtCore.QSize(0, 80))
        self.w_head.setStyleSheet("background-color: #66afe9;")
        self.w_head.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.w_head.setFrameShadow(QtWidgets.QFrame.Raised)
        self.w_head.setObjectName("w_head")
        self.btn_close = QtWidgets.QPushButton(self.w_head)
        self.btn_close.setGeometry(QtCore.QRect(810, 10, 16, 16))
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.btn_min = QtWidgets.QPushButton(self.w_head)
        self.btn_min.setGeometry(QtCore.QRect(780, 10, 16, 16))
        self.btn_min.setText("")
        self.btn_min.setObjectName("btn_min")
        self.lbl_app_name = QtWidgets.QLabel(self.w_head)
        self.lbl_app_name.setGeometry(QtCore.QRect(12, 10, 181, 41))
        self.lbl_app_name.setStyleSheet("font: 24pt \"微软雅黑\";\n"
"color: #fff;")
        self.lbl_app_name.setObjectName("lbl_app_name")
        self.verticalLayout_5.addWidget(self.w_head)
        self.w_main = QtWidgets.QWidget(Form)
        self.w_main.setObjectName("w_main")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.w_main)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.w_main)
        self.widget.setMinimumSize(QtCore.QSize(200, 0))
        self.widget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBox = QtWidgets.QToolBox(self.widget)
        self.toolBox.setStyleSheet("*{\n"
"    color: #000;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 4px;\n"
"    background-color: #66afe9;\n"
"    border: none;\n"
"    color: #FFFFFF;\n"
"    height:35px;\n"
"    min-height:35px;\n"
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
" ")
        self.toolBox.setObjectName("toolBox")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 182, 378))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_4.setContentsMargins(-1, 4, -1, 4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_example = QtWidgets.QPushButton(self.page_2)
        self.btn_example.setMinimumSize(QtCore.QSize(0, 39))
        self.btn_example.setStyleSheet("")
        self.btn_example.setObjectName("btn_example")
        self.verticalLayout_4.addWidget(self.btn_example)
        self.btn_case_conversion = QtWidgets.QPushButton(self.page_2)
        self.btn_case_conversion.setMinimumSize(QtCore.QSize(0, 39))
        self.btn_case_conversion.setStyleSheet("")
        self.btn_case_conversion.setObjectName("btn_case_conversion")
        self.verticalLayout_4.addWidget(self.btn_case_conversion)
        self.btn_base_encode = QtWidgets.QPushButton(self.page_2)
        self.btn_base_encode.setMinimumSize(QtCore.QSize(0, 39))
        self.btn_base_encode.setStyleSheet("")
        self.btn_base_encode.setObjectName("btn_base_encode")
        self.verticalLayout_4.addWidget(self.btn_base_encode)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.toolBox.addItem(self.page_2, "")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 182, 378))
        self.page.setObjectName("page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_3.setContentsMargins(-1, 4, -1, 4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.pushButton_11 = QtWidgets.QPushButton(self.page)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_3.addWidget(self.pushButton_11)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.toolBox.addItem(self.page, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btn_md5 = QtWidgets.QPushButton(self.page_4)
        self.btn_md5.setObjectName("btn_md5")
        self.verticalLayout_6.addWidget(self.btn_md5)
        self.btn_md = QtWidgets.QPushButton(self.page_4)
        self.btn_md.setMinimumSize(QtCore.QSize(0, 39))
        self.btn_md.setObjectName("btn_md")
        self.verticalLayout_6.addWidget(self.btn_md)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.toolBox.addItem(self.page_4, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 182, 378))
        self.page_3.setObjectName("page_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_2.setContentsMargins(-1, 4, -1, 4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.toolBox.addItem(self.page_3, "")
        self.verticalLayout.addWidget(self.toolBox)
        self.horizontalLayout.addWidget(self.widget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.w_main)
        self.stackedWidget.setMinimumSize(QtCore.QSize(640, 480))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.HelloWidget = QtWidgets.QWidget()
        self.HelloWidget.setObjectName("HelloWidget")
        self.stackedWidget.addWidget(self.HelloWidget)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.verticalLayout_5.addWidget(self.w_main)

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CryptoKing"))
        self.lbl_app_name.setText(_translate("Form", "CryptoKing"))
        self.btn_example.setText(_translate("Form", "Example"))
        self.btn_case_conversion.setText(_translate("Form", "英文大小写转换"))
        self.btn_base_encode.setText(_translate("Form", "Base编码"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Form", "编码转换"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.pushButton_11.setText(_translate("Form", "PushButton"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "古典密码"))
        self.btn_md5.setText(_translate("Form", "MD5"))
        self.btn_md.setText(_translate("Form", "MD系列"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("Form", "Hash函数"))
        self.pushButton_6.setText(_translate("Form", "PushButton"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("Form", "其他"))
