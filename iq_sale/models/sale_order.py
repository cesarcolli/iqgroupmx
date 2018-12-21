# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)

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
    quotation_title = fields.Char(
        string='Titulo',
        size=80
    )
    customer_contact_id = fields.Many2one(
        string='Contacto',
        comodel_name='res.partner',
        domain="[('parent_id', '=', partner_id)]"
    )
    quotation_mail_state = fields.Selection(
        string='Estado correo',
        size=1,
        compute=lambda self: self._compute_quotation_mail_state(),
        selection=[
            ('O', 'SALIENTE'),
            ('S', 'ENVIADO'),
            ('R', 'RECIBIDO'),
            ('E', 'ENTREGA FALLIDA'),
            ('C', 'CANCELADO'),
            ('P', 'PENDIENTE'),
            ('Y', 'LISTO PARA ENVIAR'),
            ('D', 'LEIDO')
        ]
    )

    def _compute_quotation_mail_state(self):

        MAIL_STATE_MAP = {
            'outgoing': 'O',
            'sent': 'S',
            'received': 'R',
            'exception': 'E',
            'cancel': 'C',
            'bounce': 'B',
            'ready': 'Y',
            'read': 'D'
        }

        for item in self:
            item.quotation_mail_state = 'P'
            so_mail = self.env['mail.mail'].search([('model', '=', 'sale.order'), ('res_id', '=', item.id)], limit=1)

            if so_mail.id:
                item.quotation_mail_state = MAIL_STATE_MAP[so_mail.state]
            else:
                so_comment_mail = self.env['mail.message'].search([
                    ('model', '=', 'sale.order'), 
                    ('res_id', '=', item.id),
                    ('message_type', '=', 'comment'),
                ], limit=1)

                if so_comment_mail.id:

                    if len(so_comment_mail.notification_ids) > 0:
                        item.quotation_mail_state = MAIL_STATE_MAP[so_comment_mail.notification_ids[0].email_status]
                        

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

    @api.onchange('partner_id')
    def change_so_customer(self):
        self.customer_contact_id = self.env['res.partner'].search([('parent_id', '=', self.partner_id.id)], limit=1).id

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