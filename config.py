from ui.Widgets.Example.EncodeOnly.EncodeOnlyWidget import EncodeOnlyWidget
from ui.Widgets.Example.EncodeDecode.EncodeDecodeWidget import EncodeDecodeWidget
from ui.Widgets.Example.EncodeOnlyMulti.EncodeOnlyMultiWidget import EncodeOnlyMultiWidget
from ui.Widgets.Example.EncodeDecodeMulti.EncodeDecodeMultiWidget import EncodeDecodeMultiWidget

from ui.Widgets.Encoding.BaseEncode.BaseWidget import BaseWidget
from ui.Widgets.Encoding.CaseConversion.CaseConversionWidget import CaseConversionWidget

from ui.Widgets.Hash.MD5.MD5Widget import MD5Widget
from ui.Widgets.Hash.MD.MDWidget import MDWidget

config = [
    {
        'group_name': 'Example',
        'actions': [
            {
                'name': '单向计算',
                'callback_widget': EncodeOnlyWidget
            },
            {
                'name': '编码解码',
                'callback_widget': EncodeDecodeWidget
            },
            {
                'name': '单向计算（复选）',
                'callback_widget': EncodeOnlyMultiWidget
            },
            {
                'name': '编码解码（复选）',
                'callback_widget': EncodeDecodeMultiWidget
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
                'callback_widget': EncodeDecodeWidget
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
                'callback_widget': EncodeDecodeWidget
            },
        ]
    },
]
