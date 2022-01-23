from PyQt5.QtWidgets import QWidget
from ui.Widgets.Example.EncodeOnly.Ui_EncodeOnlyWidget import Ui_EncodeOnlyWidget
import ui.Widgets.Example.EncodeOnly.example as example
from PyQt5.QtGui import QTextOption


class EncodeOnlyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.widget = Ui_EncodeOnlyWidget()
        self.widget.setupUi(self)
        self.initFunc()
        pass

    def initFunc(self):
        self.widget.btn_encode.clicked.connect(self.encode)
        pass

    def encode(self):
        txt_left = self.widget.txt_left.toPlainText()
        txt_right = example.encode(txt_left)
        self.widget.txt_right.setPlainText(txt_right)
        pass

    pass
