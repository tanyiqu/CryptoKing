from PyQt5.QtWidgets import QWidget
from ui.Widgets.Example.uic_ExampleWidget import Ui_ExampleWidget


class ExampleWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.widget = Ui_ExampleWidget()
        self.widget.setupUi(self)
        self.initFunc()
        pass

    # 初始化
    def initFunc(self):
        self.widget.btn_encode.clicked.connect(self.encode)
        self.widget.btn_decode.clicked.connect(self.decode)
        pass

    def encode(self):
        print('encode')
        pass

    def decode(self):
        print('decode')
        pass

    pass
