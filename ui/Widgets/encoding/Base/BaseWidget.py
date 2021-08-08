from PyQt5.QtWidgets import QWidget
from ui.Widgets.encoding.Base.uic_Base import Ui_Form


class BaseWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.widget = Ui_Form()
        self.widget.setupUi(self)
        self.initFunc()
        pass

    def initFunc(self):
        self.widget.pushButton.clicked.connect(self.encode)
        pass

    def encode(self):
        text = self.widget.plainTextEdit.toPlainText()
        self.widget.plainTextEdit_2.setPlainText(text * 2)
        pass

    pass
