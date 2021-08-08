from PyQt5.QtWidgets import QWidget
from ui.Widgets.encoding.Base.uic_BaseWidget import Ui_BaseWidget


class BaseWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.widget = Ui_BaseWidget()
        self.widget.setupUi(self)
        self.initFunc()
        pass

    # 
    def initFunc(self):
        self.widget.pushButton.clicked.connect(self.encode)
        pass

    def encode(self):
        text = self.widget.plainTextEdit.toPlainText()
        self.widget.plainTextEdit_2.setPlainText(text * 2)
        pass

    pass
