from PyQt5.QtWidgets import QWidget
from ui.Forms.uic_MainForm import Ui_Form


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.mainForm = Ui_Form()
        self.mainForm.setupUi(self)
        self.initFunc()
        pass

    def initFunc(self):
        self.mainForm.pushButton.clicked.connect(self.click)
        pass

    def click(self):
        print(1)
        pass

    pass
