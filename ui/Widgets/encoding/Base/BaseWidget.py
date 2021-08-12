from PyQt5.QtWidgets import QWidget
from ui.Widgets.encoding.Base.uic_BaseWidget import Ui_BaseWidget
import base64


class BaseWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.widget = Ui_BaseWidget()
        self.widget.setupUi(self)
        self.initFunc()
        pass

    # 
    def initFunc(self):
        self.widget.btn_encode.clicked.connect(self.encode)
        self.widget.btn_decode.clicked.connect(self.decode)
        pass

    def encode(self):
        text = self.widget.txt_left.toPlainText()
        print('text', text)
        cipher = base64.b64encode(text.encode())
        print('cipher', cipher)
        self.widget.txt_right.setPlainText(cipher.decode())
        pass

    def decode(self):
        text = self.widget.txt_left.toPlainText()
        print(text)
        cipher = base64.b64decode(text.encode())
        print(cipher)
        self.widget.txt_right.setPlainText(cipher.decode())
        pass

    pass
