# -*- coding: utf-8 -*-
# © <2018> <Cesar Colli (cesarcolli@ideanet.com.mx)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class Product(models.Model):
    _inherit = 'product.template'

    length = fields.Float(
        string='Largo',
        help="Largo en centímetros"
    )
    width = fields.Float(
        string='Ancho',
        help="Ancho en centímetros"
    )
    height = fields.Float(
        string='Alto',
        help="Alto en centímetros"
    )
