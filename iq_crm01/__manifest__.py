# -*- coding: utf-8 -*-
{
    'name': "iq_crm01",

    'summary': """IQ company sales functionality""",

    'description': """

    """,

    'author': "Francisco Ballina",

    # Categories can be used to filter modules in modules listing
    'category': 'IQ',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['crm', 'sales_team'],

    # always loaded
    'data': [
        'views/sales.xml',
    ]
}