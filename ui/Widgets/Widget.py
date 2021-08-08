from PyQt5.QtWidgets import QWidget
from ui.Widgets.uic_Widget import Ui_Form


class Widget(QWidget):

    def __init__(self):
        super().__init__()
        self.widget = Ui_Form()
        self.widget.setupUi(self)
        self.initFunc()
        pass

    pass
