from PyQt5.QtWidgets import QWidget
from ui.Widgets.Encoding.CaseConversion.Ui_CaseConversion import Ui_CaseConversion

import ui.Widgets.Encoding.CaseConversion.core as core


class CaseConversionWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.widget = Ui_CaseConversion()
        self.widget.setupUi(self)
        self.initFunc()
        pass

        # 初始化

    def initFunc(self):
        # 设置文本不自动换行
        # self.widget.txt_left.setWordWrapMode(QTextOption.WrapMode)

        self.widget.btn_upper.clicked.connect(self.upper)
        self.widget.btn_lower.clicked.connect(self.lower)
        pass

    # 大写
    def upper(self):
        # print('encode')
        # 获取文本框中的内容
        txt_left = self.widget.txt_left.toPlainText()
        txt_right = core.upper(txt_left)
        print(txt_right)
        self.widget.txt_right.setPlainText(txt_right)
        pass

    # 小写
    def lower(self):
        print('decode')
        # 获取文本框中的内容
        txt_left = self.widget.txt_left.toPlainText()
        txt_right = core.lower(txt_left)
        print(txt_right)
        self.widget.txt_right.setPlainText(txt_right)
        pass

    pass
