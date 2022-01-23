from PyQt5.QtWidgets import QWidget
from ui.Widgets.Example.EncodeDecodeMulti.Ui_EncodeDecodeMultiWidget import Ui_EncodeDecodeMultiWidget
import ui.Widgets.Example.EncodeDecodeMulti.example as example


class EncodeDecodeMultiWidget(QWidget):
    current_encode_method = example.encode_1
    current_decode_method = example.decode_1

    def __init__(self):
        super().__init__()
        self.widget = Ui_EncodeDecodeMultiWidget()
        self.widget.setupUi(self)
        self.initFunc()
        pass

    def initFunc(self):
        self.widget.btn_encode.clicked.connect(self.encode)
        self.widget.btn_decode.clicked.connect(self.decode)
        self.widget.combo_method.currentIndexChanged.connect(
            self.switch_method)
        pass

    #  切换编码算法
    def switch_method(self):
        index = self.widget.combo_method.currentIndex()
        if index == 0:
            EncodeDecodeMultiWidget.current_encode_method = example.encode_1
            EncodeDecodeMultiWidget.current_decode_method = example.decode_1
        elif index == 1:
            EncodeDecodeMultiWidget.current_encode_method = example.encode_2
            EncodeDecodeMultiWidget.current_decode_method = example.decode_2
        pass

    def encode(self):
        # 获取文本框中的内容
        txt_left = self.widget.txt_left.toPlainText()
        txt_right = EncodeDecodeMultiWidget.current_encode_method(txt_left)
        print(txt_right)
        self.widget.txt_right.setPlainText(txt_right)
        pass

    def decode(self):
        # 获取文本框中的内容
        txt_left = self.widget.txt_left.toPlainText()
        txt_right = EncodeDecodeMultiWidget.current_decode_method(txt_left)
        print(txt_right)
        self.widget.txt_right.setPlainText(txt_right)
        pass

    pass
