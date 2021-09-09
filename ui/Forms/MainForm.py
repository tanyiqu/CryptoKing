from PyQt5.QtWidgets import QWidget
from ui.Forms.uic_MainForm import Ui_Form


from ui.Widgets.Example.ExampleWidget import ExampleWidget
from ui.Widgets.encoding.BaseEncode.BaseWidget import BaseWidget


class MainForm(QWidget):
    # 在此定义变量
    abc = '123abc'

    def __init__(self):
        super().__init__()
        self.mainForm = Ui_Form()
        self.mainForm.setupUi(self)
        self.initFunc()
        pass

    def initFunc(self):
        # 连接信号槽
        self.mainForm.btn_example.clicked.connect(self.example)
        self.mainForm.btn_base_encode.clicked.connect(self.base_encode)
        self.mainForm.btn_case_conversion.clicked.connect(self.case_conversion)
        pass

    def example(self):
        print('测试组件')
        ex = ExampleWidget()
        self.mainForm.stackedWidget.addWidget(ex)
        self.mainForm.stackedWidget.setCurrentWidget(ex)
        pass

    def case_conversion(self):
        print('字母大小写转换')
        pass

    def base_encode(self):
        print('Base编码')
        base = BaseWidget()
        self.mainForm.stackedWidget.addWidget(base)
        self.mainForm.stackedWidget.setCurrentWidget(base)
        pass

    pass
