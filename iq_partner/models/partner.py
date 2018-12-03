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

    x_customer_ref = fields.Char(string='Referencia Cliente', index=True)
    x_supplier_ref = fields.Char(string='Referencia Proveedor', index=True)

    x_interest_id = fields.Many2many('partner.interest', column1='partner_id',
                                     column2='x_interest_id', string='Categorías de interés', default=_default_interest)

    x_comercial_name = fields.Char(string='Comercial name', translate=True)

    @api.multi
    def _get_next_customer_ref(self, vals=None):
        return self.env['ir.sequence'].next_by_code('res.partner.customer')

    @api.multi
    def _get_next_supplier_ref(self, vals=None):
        return self.env['ir.sequence'].next_by_code('res.partner.supplier')

    @api.model
    def create(self, vals):
        if vals.get("customer") and not vals.get('x_customer_ref'):
            vals['x_customer_ref'] = self._get_next_customer_ref(vals=vals)
        if vals.get("supplier") and not vals.get('x_supplier_ref'):
            vals['x_supplier_ref'] = self._get_next_supplier_ref(vals=vals)
        return super(ResPartner, self).create(vals)

    @api.multi
    def copy(self, default=None):
        default = default or {}
        if default['x_customer_ref']:
            default['x_customer_ref'] = self._get_next_customer_ref()
        if default['x_supplier_ref']:
            default['x_supplier_ref'] = self._get_next_supplier_ref()
        return super(ResPartner, self).copy(default)

    @api.multi
    def write(self, vals):
        for partner in self:
            if not vals.get('x_customer_ref') and vals.get("customer") and not partner.x_customer_ref:
                vals['x_customer_ref'] = self._get_next_customer_ref(vals=vals)
            if not vals.get('x_supplier_ref') and  vals.get("supplier") and not partner.x_supplier_ref:
                vals['x_supplier_ref'] = self._get_next_supplier_ref(vals=vals)
            super(ResPartner, partner).write(vals)
        return True
