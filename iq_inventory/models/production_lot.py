# -*- coding: utf-8 -*-
# © <2018> <Cesar Colli (cesarcolli@ideanet.com.mx)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    warranty_start_date = fields.Date(
        string='Inicio de garantía',
        help='Fecha de inicio de garantía')

    warranty_end_date = fields.Date(
        string='Fin de garantía',
        help='Fecha de inicio de garantía')
