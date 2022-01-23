from PyQt5.QtWidgets import QWidget
from ui.Widgets.Example.EncodeOnlyMulti.Ui_EncodeOnlyMultiWidget import Ui_EncodeOnlyMultiWidget
import ui.Widgets.Example.EncodeOnlyMulti.example as example
from PyQt5.QtGui import QTextOption


class EncodeOnlyMultiWidget(QWidget):

    current_method = example.method_1

    def __init__(self):
        super().__init__()
        self.widget = Ui_EncodeOnlyMultiWidget()
        self.widget.setupUi(self)
        self.initFunc()
        pass

    def initFunc(self):
        self.widget.btn_encode.clicked.connect(self.encode)
        self.widget.combo_method.currentIndexChanged.connect(self.switch_method)
        pass

    # 切换编码算法
    def switch_method(self):
        index = self.widget.combo_method.currentIndex()
        if index == 0:
            EncodeOnlyMultiWidget.current_method = example.method_1
        elif index == 1:
            EncodeOnlyMultiWidget.current_method = example.method_2
        pass

    def encode(self):
        # 获取文本框中的内容
        txt_left = self.widget.txt_left.toPlainText()
        txt_right = EncodeOnlyMultiWidget.current_method(txt_left)
        self.widget.txt_right.setPlainText(txt_right)
        pass

    pass
