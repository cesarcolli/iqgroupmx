# -*- coding: utf-8 -*-
{
    'name': "IQ INVENTORY",

    'summary': """IQ company inventory functionality""",

    'description': """

    """,

    'author': "Omar Torres",
    'website': "http://proogeeks.com",

    # Categories can be used to filter modules in modules listing
    'category': 'IQ',
    'version': '1.3',

    # any module necessary for this one to work correctly
    'depends': ['sale_stock'],

    # always loaded
    'data': [
        'views/product_views.xml',
        'reports/iq_stock_picking_main.xml',
        'reports/iq_stock_picking_move.xml',
        'reports/iq_stock_picking_delivery.xml',
    ]
}
