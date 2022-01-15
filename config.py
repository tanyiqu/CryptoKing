from ui.Widgets.Example.EncodeDecode.EncodeDecodeWidget import EncodeDecodeWidget
from ui.Widgets.encoding.BaseEncode.BaseWidget import BaseWidget
from ui.Widgets.encoding.CaseConversion.CaseConversionWidget import CaseConversionWidget

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
        'group_name': 'Exampleadadasd',
        'actions': [
            {
                'name': '编码解码3',
                'callback_widget': CaseConversionWidget
            },
        ]
    },
]
