# -*- coding: utf-8 -*-
# © <2018> <Cesar Colli (cesarcolli@gmail.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    iq_delivery_term_id = fields.Many2one('sale.term',
                                          domain=[('term_type', '=', 'delivery')],
                                          string='Tiempo de entrega',
                                          help="Condición comercial para el tiempo de entrega")
    iq_installation_time_term_id = fields.Many2one('sale.term',
                                                   domain=[('term_type', '=', 'installation-time')],
                                                   string='Tiempo de instalación',
                                                   help="Condición comercial para el tiempo de instalación")
    iq_equipment_term_id = fields.Many2one('sale.term',
                                           domain=[('term_type', '=', 'equipment')],
                                           string='Equipo',
                                           help="Condición comercial para el equipo")
    iq_installation_term_id = fields.Many2one('sale.term',
                                              domain=[('term_type', '=', 'installation')],
                                              string='Instalación',
                                              help="Condición comercial para la instalación")
    iq_expenses_term_id = fields.Many2one('sale.term',
                                          domain=[('term_type', '=', 'expenses')],
                                          string='Viáticos',
                                          help="Condición comercial para la viáticos")
    iq_civil_work_term_id = fields.Many2one('sale.term',
                                            domain=[('term_type', '=', 'civil-work')],
                                            string='Obra civil y eléctrico',
                                            help="Condición comercial para la obra civil y eléctrico")
    iq_shipping_term_id = fields.Many2one('sale.term',
                                          domain=[('term_type', '=', 'shipping')],
                                          string='Envío',
                                          help="Condición comercial para el envío")
