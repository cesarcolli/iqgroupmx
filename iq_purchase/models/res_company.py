# -*- coding: utf-8 -*-
# © <2018> <Omar Torres (otorres@proogeeks.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    iq_purchase_terms = fields.Boolean(
        string='Términos de compra'
    )
    iq_purchase_default_terms = fields.Text(
        string='Términos'
    )
