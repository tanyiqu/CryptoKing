from PyQt5.QtWidgets import QWidget
from ui.Forms.uic_MainForm import Ui_Form
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QMouseEvent

from ui.Widgets.Example.ExampleWidget import ExampleWidget
from ui.Widgets.encoding.BaseEncode.BaseWidget import BaseWidget
from ui.Widgets.encoding.CaseConversion.CaseConversionWidget import CaseConversionWidget


class MainForm(QWidget):
    # 在此定义变量

    def __init__(self):
        super().__init__()
        self.mainForm = Ui_Form()
        self.mainForm.setupUi(self)
        # 初始化外观
        self.init_appearance()
        # 功能操作
        self.init_func()
        pass

    def init_appearance(self):
        # 设置窗口无边框
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 按钮样式
        self.mainForm.btn_close.setStyleSheet("QPushButton{border-image: url(resource/imgs/close_normal.png)}"
                                              "QPushButton:hover{border-image: url(resource/imgs/close_hover.png)}")
        self.mainForm.btn_min.setStyleSheet("QPushButton{border-image: url(resource/imgs/min_normal.png)}"
                                            "QPushButton:hover{border-image: url(resource/imgs/min_hover.png)}")
        pass

    def init_func(self):
        # 关闭按钮
        self.mainForm.btn_close.clicked.connect(lambda: exit(0))

        # 实现窗口拖动
        self.set_move()

        # 连接信号槽
        self.mainForm.btn_example.clicked.connect(self.example)
        self.mainForm.btn_base_encode.clicked.connect(self.base_encode)
        self.mainForm.btn_case_conversion.clicked.connect(self.case_conversion)
        pass

    # ##### 菜单  ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    def example(self):
        print('测试组件')
        ex = ExampleWidget()
        self.mainForm.stackedWidget.addWidget(ex)
        self.mainForm.stackedWidget.setCurrentWidget(ex)
        pass

    def case_conversion(self):
        print('字母大小写转换')
        cc = CaseConversionWidget()
        self.mainForm.stackedWidget.addWidget(cc)
        self.mainForm.stackedWidget.setCurrentWidget(cc)
        pass

    def base_encode(self):
        print('Base编码')
        base = BaseWidget()
        self.mainForm.stackedWidget.addWidget(base)
        self.mainForm.stackedWidget.setCurrentWidget(base)
        pass

    # ##### 菜单  ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

    # ##### 实现窗口拖动  ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    _startPos = None
    _endPos = None
    _isTracking = False

    def set_move(self):
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
        self.show()

    def mouseMoveEvent(self, e: QMouseEvent):
        if (self._startPos is None) or (e.pos() is None):
            return
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    # ##### 实现窗口拖动  ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

    pass
