from PyQt5.QtWidgets import QWidget
from ui.Forms.uic_MainForm import Ui_Form

from ui.Widgets.encoding.BaseEncode.BaseWidget import BaseWidget


class MainForm(QWidget):
    # 在此定义变量
    abc = '123abc'

    def __init__(self):
        super().__init__()
        self.mainForm = Ui_Form()
        self.mainForm.setupUi(self)
        self.initFunc()
        self.mainForm.pushButton.setText(self.abc)
        pass

    def initFunc(self):
        self.mainForm.pushButton.clicked.connect(self.click)
        pass

    def click(self):
        print(1)

        # self.mainForm.widget = BaseWidget()
        # self.ww = BaseWidget()

        base = BaseWidget()

        self.mainForm.stackedWidget.addWidget(base)

        # print(self.mainForm.stackedWidget.currentWidget)

        self.mainForm.stackedWidget.setCurrentWidget(base)


        pass

    pass
