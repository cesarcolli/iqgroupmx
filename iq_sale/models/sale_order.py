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
        default=False
    )
    quotation_sec_customers = fields.Boolean(
        string='Nuestros Clientes',
        default=True
    )

    def quotation_page_index(self):

        self.ensure_one()

        qt_index = []
        qt_page  = 2

        if self.quotation_sec_about:
            qt_page += 1
            qt_index.append([qt_page, 'Quiénes somos'])

        if self.quotation_sec_services:
            qt_page += 1
            qt_index.append([qt_page, 'Servicios'])

        qt_page += 1
        qt_index.append([qt_page, 'Propuesta económica'])

        if self.quotation_sec_conditions:
            qt_page += 1
            qt_index.append([qt_page, 'Condiciones comerciales'])

        if self.quotation_sec_info:
            qt_page += 1
            qt_index.append([qt_page, 'Información adicional'])

        if self.quotation_sec_customers:
            qt_page += 1
            qt_index.append([qt_page, 'Nuestros Clientes'])

        return qt_index

    def customer_location(self):

        self.ensure_one()

        customer_city = self.partner_id.city
        customer_state = self.partner_id.state_id.name

        return ('%s%s%s' % (
            customer_city or ' ',
            ', ' if customer_city and customer_state else '',
            customer_state or ' '
        )).strip()

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    line_num = fields.Integer(
        string='#',
        default=0
    )

    @api.model
    def create(self, vals):

        res = super(SaleOrderLine, self).create(vals)

        res.sudo().line_num = len(res.order_id.order_line)

        return res