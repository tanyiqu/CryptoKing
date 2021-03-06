from PyQt5.QtWidgets import QWidget
from ui.Widgets.Example.EncodeDecode.Ui_EncodeDecodeWidget import Ui_EncodeDecodeWidget
import ui.Widgets.Example.EncodeDecode.example as example
from PyQt5.QtGui import QTextOption


class EncodeDecodeWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.widget = Ui_EncodeDecodeWidget()
        self.widget.setupUi(self)
        self.initFunc()
        pass

    def initFunc(self):
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
