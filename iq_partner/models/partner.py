# -*- coding: utf-8 -*-
# © <2018> <Cesar Colli (cesarcolli@gmail.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, exceptions, _


class PartnerInterest(models.Model):
    _description = 'Partner interest category'
    _name = 'partner.interest'

    name = fields.Char(string='Interest Name', required=True, translate=True)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _default_interest(self):
        return self.env['partner.interest'].browse(self._context.get('x_interest_id'))

    x_interest_id = fields.Many2many('partner.interest', column1='partner_id',
                                     column2='x_interest_id', string='Categorías de interés', default=_default_interest)
