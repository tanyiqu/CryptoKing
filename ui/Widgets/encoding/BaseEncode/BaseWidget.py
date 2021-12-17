from PyQt5.QtWidgets import QWidget
from ui.Widgets.encoding.BaseEncode.Ui_BaseWidget import Ui_BaseWidget
import ui.Widgets.encoding.BaseEncode.base_core as base_core


class BaseWidget(QWidget):
    current_encode_method = base_core.b64_encode
    current_decode_method = base_core.b64_decode

    def __init__(self):
        super().__init__()
        self.widget = Ui_BaseWidget()
        self.widget.setupUi(self)
        self.initFunc()
        BaseWidget.current_encode_method = base_core.b64_encode
        BaseWidget.current_decode_method = base_core.b64_decode
        pass

    # 初始化
    def initFunc(self):
        self.widget.btn_encode.clicked.connect(self.encode)
        self.widget.btn_decode.clicked.connect(self.decode)
        self.widget.combo_method.currentIndexChanged.connect(self.switch_method)
        pass

    # 切换编码算法
    def switch_method(self):
        index = self.widget.combo_method.currentIndex()
        if index == 0:
            BaseWidget.current_encode_method = base_core.b64_encode
            BaseWidget.current_decode_method = base_core.b64_decode
        elif index == 1:
            BaseWidget.current_encode_method = base_core.b32_encode
            BaseWidget.current_decode_method = base_core.b32_decode
        elif index == 2:
            BaseWidget.current_encode_method = base_core.b16_encode
            BaseWidget.current_decode_method = base_core.b16_decode
        pass

    # 点击编码
    def encode(self):
        text = self.widget.txt_left.toPlainText()
        cipher = BaseWidget.current_encode_method(text)
        self.widget.txt_right.setPlainText(cipher)
        pass

    # 点击解码
    def decode(self):
        text = self.widget.txt_left.toPlainText()
        cipher = BaseWidget.current_decode_method(text)
        self.widget.txt_right.setPlainText(cipher)
        pass

    pass
