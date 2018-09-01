# -*- coding: utf-8 -*-

from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    quotation_sec_about = fields.Boolean(
        string='¿Quiénes somos?',
        default=True
    )
    quotation_sec_services = fields.Boolean(
        string='Servicios',
        default=True
    )
    quotation_sec_conditions = fields.Boolean(
        string='Condiciones comerciales',
        default=True
    )
    quotation_sec_info = fields.Boolean(
        string='Información adicional',
        default=True
    )
    quotation_sec_customers = fields.Boolean(
        string='Nuestros Clientes',
        default=True
    )