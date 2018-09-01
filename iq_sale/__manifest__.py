# -*- coding: utf-8 -*-
{
    'name': "IQ Sale",

    'summary': """IQ company sales functionality""",

    'description': """

    """,

    'author': "Omar Torres",
    'website': "http://proogeeks.com",

    # Categories can be used to filter modules in modules listing
    'category': 'IQ',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['sale_management'],

    # always loaded
    'data': [
        'reports/iq_sale_order_main.xml',
        'reports/iq_sale_order_report.xml',
        'wizards/product_tech_file.xml',
        'views/sale_order.xml',
        'views/product_template.xml',
    ]
}