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
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['website_quote','sale_management', 'sale_stock', 'iq_sale_terms'],

    # always loaded
    'data': [
        'reports/iq_sale_order_main.xml',
        'reports/iq_sale_order_report.xml',
        'wizards/product_tech_file.xml',
        'views/sale_order.xml',
        'views/product_template.xml',
        'views/iq_customer_project.xml',
        'views/iq_customer_contact.xml',
        'views/iq_operator_contact.xml',
        'views/res_partner.xml',
    ]
}