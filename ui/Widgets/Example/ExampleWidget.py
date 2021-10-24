from PyQt5.QtWidgets import QWidget
from ui.Widgets.Example.uic_ExampleWidget import Ui_ExampleWidget
import ui.Widgets.Example.example as example
from PyQt5.QtGui import QTextOption


class ExampleWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.widget = Ui_ExampleWidget()
        self.widget.setupUi(self)
        self.initFunc()
        pass

        # 初始化

    def initFunc(self):
        # 设置文本不自动换行
        # self.widget.txt_left.setWordWrapMode(QTextOption.WrapMode)

        self.widget.btn_encode.clicked.connect(self.encode)
        self.widget.btn_decode.clicked.connect(self.decode)
        pass

    def encode(self):
        # print('encode')
        # 获取文本框中的内容
        txt_left = self.widget.txt_left.toPlainText()
        txt_right = example.encode(txt_left)
        print(txt_right)
        self.widget.txt_right.setPlainText(txt_right)
        pass

    def decode(self):
        print('decode')
        # 获取文本框中的内容
        txt_left = self.widget.txt_left.toPlainText()
        txt_right = example.decode(txt_left)
        print(txt_right)
        self.widget.txt_right.setPlainText(txt_right)
        pass

    pass
