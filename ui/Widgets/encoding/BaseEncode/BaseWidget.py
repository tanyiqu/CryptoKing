from PyQt5.QtWidgets import QWidget
from ui.Widgets.encoding.BaseEncode.uic_BaseWidget import Ui_BaseWidget
import ui.Widgets.encoding.BaseEncode.base_core as base_core


class BaseWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.widget = Ui_BaseWidget()
        self.widget.setupUi(self)
        self.initFunc()
        pass

    # 初始化
    def initFunc(self):
        self.widget.btn_encode.clicked.connect(self.encode)
        self.widget.btn_decode.clicked.connect(self.decode)
        pass

    # 点击编码
    def encode(self):
        text = self.widget.txt_left.toPlainText()
        cipher = base_core.b64_encode(text)
        self.widget.txt_right.setPlainText(cipher)
        pass

    # 点击解码
    def decode(self):
        text = self.widget.txt_left.toPlainText()
        cipher = base_core.b64_decode(text)
        self.widget.txt_right.setPlainText(cipher)
        pass

    pass
