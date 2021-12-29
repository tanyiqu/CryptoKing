from PyQt5.QtWidgets import QWidget
from ui.Forms.Ui_MainForm import Ui_Form
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QPoint, QRectF
from PyQt5.QtGui import QMouseEvent, QColor, QPainter, QPainterPath, QBrush
import Menu


class MainForm(QWidget):
    # 在此定义变量

    def __init__(self, parent=None):
        # super().__init__()
        super(MainForm, self).__init__(parent)
        self.mainForm = Ui_Form()
        self.mainForm.setupUi(self)
        self.border_width = 8
        # 初始化外观
        self.init_appearance()
        # 功能操作
        self.init_func()
        pass

    # 设置窗口样式
    def init_appearance(self):
        # 设置窗口无边框
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)

        # 设置按钮样式
        self.mainForm.btn_close.setStyleSheet("QPushButton{border-image: url(resource/imgs/close_normal.png)}"
                                              "QPushButton:hover{border-image: url(resource/imgs/close_hover.png)}")
        self.mainForm.btn_min.setStyleSheet("QPushButton{border-image: url(resource/imgs/min_normal.png)}"
                                            "QPushButton:hover{border-image: url(resource/imgs/min_hover.png)}")
        pass

    # 设置窗口的功能
    def init_func(self):
        # 关闭按钮
        self.mainForm.btn_close.clicked.connect(lambda: exit(0))

        # 最小化
        self.mainForm.btn_min.clicked.connect(
            lambda: self.setWindowState(Qt.WindowState.WindowMinimized))

        # 实现窗口拖动
        self.set_move()

        # 注册菜单按钮
        Menu.register_menu(self)
        pass

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
