# -*- coding: utf-8 -*-
# © <2018> <Omar Torres (otorres@proogeeks.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    iq_payment_type_id = fields.Many2one(
        string='Forma de pago',
        comodel_name='iq.payment.type'
    )
    iq_purchase_agent_id = fields.Many2one(
        string='Agente',
        comodel_name='res.users'
    )
    notes = fields.Text(
        default=lambda self: self.env['res.company']._company_default_get(self._name).iq_purchase_default_terms
    )