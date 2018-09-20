# -*- coding: utf-8 -*-
# © <2018> <Cesar Colli (cesarcolli@gmail.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    x_comercial_name = fields.Text(string='Comercial name', translate=True)
