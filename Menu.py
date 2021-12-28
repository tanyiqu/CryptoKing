from ui.Widgets.Example.EncodeDecode.EncodeDecodeWidget import EncodeDecodeWidget
from ui.Widgets.encoding.BaseEncode.BaseWidget import BaseWidget
from ui.Widgets.encoding.CaseConversion.CaseConversionWidget import CaseConversionWidget


from ui.Widgets.Hash.MD5.MD5Widget import MD5Widget
from ui.Widgets.Hash.MD.MDWidget import MDWidget

# 注册菜单按钮，放在这单独管理


def register_menu(mainForm):
    ############ Example #############
    #  编码解码
    example_widget = EncodeDecodeWidget()
    mainForm.mainForm.stackedWidget.addWidget(example_widget),
    mainForm.mainForm.btn_example.clicked.connect(lambda: (
        print('Example'),
        mainForm.mainForm.stackedWidget.setCurrentWidget(example_widget)
    ))

    ############# 编码转换 #############
    # 英文大小写转换
    case_conversion_widget = CaseConversionWidget()
    mainForm.mainForm.stackedWidget.addWidget(case_conversion_widget),
    mainForm.mainForm.btn_case_conversion.clicked.connect(lambda: (
        print('英文大小写转换'),
        mainForm.mainForm.stackedWidget.setCurrentWidget(
            case_conversion_widget)
    ))

    # Base编码
    base_widget = BaseWidget()
    mainForm.mainForm.stackedWidget.addWidget(base_widget),
    mainForm.mainForm.btn_base_encode.clicked.connect(lambda: (
        print('Base编码'),
        mainForm.mainForm.stackedWidget.setCurrentWidget(base_widget)
    ))

    ############# 古典密码 #############

    ############# Hash #############
    # MD5
    md5widget = MD5Widget()
    mainForm.mainForm.stackedWidget.addWidget(md5widget),
    mainForm.mainForm.btn_md5.clicked.connect(lambda: (
        print('MD5'),
        mainForm.mainForm.stackedWidget.setCurrentWidget(md5widget)
    ))

    # MD系列
    mdwidget = MDWidget()
    mainForm.mainForm.stackedWidget.addWidget(mdwidget),
    mainForm.mainForm.btn_md.clicked.connect(lambda: (
        print('MD系列'),
        mainForm.mainForm.stackedWidget.setCurrentWidget(mdwidget)
    ))

    ############# 其他 #############

    pass
