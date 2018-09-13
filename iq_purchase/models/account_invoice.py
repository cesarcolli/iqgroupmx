# -*- coding: utf-8 -*-
# © <2018> <Cesar Colli (cesarcolli@gmail.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    def _prepare_invoice_line_from_po_line(self, line):
        vals = super(AccountInvoice, self)._prepare_invoice_line_from_po_line(
            line)
        vals['discount'] = line.iq_discount
        return vals
