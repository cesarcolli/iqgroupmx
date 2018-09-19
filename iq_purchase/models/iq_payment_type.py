# -*- coding: utf-8 -*-
# © <2018> <Omar Torres (otorres@proogeeks.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class iq_payment_type(models.Model):
    _name = 'iq.payment.type'
    _description = 'IQ PAYMENT TYPE'

    name = fields.Char(
        string='Nombre',
        required=True
    )
