# -*- coding: utf-8 -*-
# © <2018> <Cesar Colli (cesarcolli@gmail.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models
from odoo.addons import decimal_precision as dp


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    iq_discount = fields.Float(string='Descuento (%)', digits=dp.get_precision('Discount'), default=0.0)

    _sql_constraints = [
        ('discount_limit', 'CHECK (iq_discount <= 100.0)',
         'El descuento debe ser menor que 100%.'),
    ]

    @api.depends('iq_discount')
    def _compute_amount(self):
        for line in self:
            price_unit = False
            # This is always executed for allowing other modules to use this
            # with different conditions than discount != 0
            price = line._get_discounted_price_unit()
            if price != line.price_unit:
                # Only change value if it's different
                price_unit = line.price_unit
                line.price_unit = price
            super(PurchaseOrderLine, line)._compute_amount()
            if price_unit:
                line.price_unit = price_unit

    def _get_discounted_price_unit(self):
        """Inheritable method for getting the unit price after applying
        discount(s).

        :rtype: float
        :return: Unit price after discount(s).
        """
        self.ensure_one()
        if self.iq_discount:
            return self.price_unit * (1 - self.iq_discount / 100)
        return self.price_unit


