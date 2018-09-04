# -*- coding: utf-8 -*-
{
    'name': "IQ Purchase",

    'summary': """IQ company purchase functionality""",

    'description': """

    """,

    'author': "Cesar Colli",
    'website': "http://ideanet.odoo.com",

    # Categories can be used to filter modules in modules listing
    'category': 'IQ',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],

    # always loaded
    'data': [
        'views/purchase_views.xml'
    ]
}