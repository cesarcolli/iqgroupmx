# -*- coding: utf-8 -*-
# © <2018> <Omar Torres (otorres@proogeeks.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    iq_purchase_terms = fields.Boolean(
        string='Términos de compra',
        related='company_id.iq_purchase_terms'
    )
    iq_purchase_default_terms = fields.Text(
        string='Términos',
        related='company_id.iq_purchase_default_terms'
    )