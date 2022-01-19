from ui.Widgets.Example.EncodeDecode.EncodeDecodeWidget import EncodeDecodeWidget
from ui.Widgets.encoding.BaseEncode.BaseWidget import BaseWidget
from ui.Widgets.encoding.CaseConversion.CaseConversionWidget import CaseConversionWidget

from ui.Widgets.Hash.MD5.MD5Widget import MD5Widget
from ui.Widgets.Hash.MD.MDWidget import MDWidget

config = [
    {
        'group_name': 'Example',
        'actions': [
            {
                'name': '编码解码1',
                'callback_widget': EncodeDecodeWidget
            },
            {
                'name': '编码解码2',
                'callback_widget': BaseWidget
            },
        ]
    },
    {
        'group_name': '编码转换',
        'actions': [
            {
                'name': '英文大小写',
                'callback_widget': CaseConversionWidget
            },
            {
                'name': 'Base编码',
                'callback_widget': BaseWidget
            },
        ]
    },
    {
        'group_name': '古典密码',
        'actions': [
            {
                'name': '编码解码3',
                'callback_widget': CaseConversionWidget
            },
        ]
    },
    {
        'group_name': 'Hash函数',
        'actions': [
            {
                'name': 'MD5',
                'callback_widget': MD5Widget
            },
            {
                'name': 'MD',
                'callback_widget': MDWidget
            },
        ]
    },
    {
        'group_name': '其他',
        'actions': [
            {
                'name': '编码解码3',
                'callback_widget': CaseConversionWidget
            },
        ]
    },
]
