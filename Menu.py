from asyncio.proactor_events import constants
from tkinter import W
from unicodedata import name
from PyQt5.QtWidgets import  QWidget, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy, QStackedWidget
from functools import partial
from config import config

########## 注册菜单按钮，放在这单独管理 ##########


# 用于切换widget
def change_widget(stackedWidget: QStackedWidget, action):
    print(action['name'])
    stackedWidget.setCurrentIndex(stackedWidget.addWidget(action['callback_widget']))
    pass


# 注册菜单
def register_menu_list(mainForm):

    # 构造所有的Widget
    config2 = []
    for group in config:
        dict1 = {}
        actions = []
        for action in group['actions']:
            gp = {}
            gp['name'] = action['name']
            gp['callback_widget'] = action['callback_widget']()
            actions.append(gp)
            pass
        dict1['group_name'] = group['group_name']
        dict1['actions'] = actions
        config2.append(dict1)
        pass

    toolBox = mainForm.toolBox
    # 先清空所有菜单
    while (toolBox.count() != 0):
        toolBox.removeItem(0)
        pass

    # 根据配置添加
    for group in config2:
        # 添加一个菜单
        w1 = QWidget()
        l1 = QVBoxLayout()
        # 依次添加按钮
        for action in group['actions']:
            b1 = QPushButton(action['name'])
            # 给按钮设置监听
            b1.clicked.connect(partial(change_widget,mainForm.stackedWidget, action))
            l1.addWidget(b1)
            pass
        w1.setLayout(l1)
        # 加个弹簧
        spacerItem = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        l1.addItem(spacerItem)
        # 将这个菜案添加只toolbox
        toolBox.insertItem(-1, w1, group['group_name'])
        pass

    # 设置默认菜单
    toolBox.setCurrentIndex(0)
    pass
