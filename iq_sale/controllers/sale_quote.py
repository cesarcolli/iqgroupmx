# -*- coding: utf-8 -*-

import logging

from odoo.addons.website_quote.controllers.main import sale_quote
from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)

class SaleQuote(sale_quote):

    @http.route("/quote/<int:order_id>/<token>", type='http', auth="public", website=True)
    def view(self, order_id, pdf=None, token=None, message=False, **post):

        so_comment_mail = request.env['mail.message'].search([
            ('model', '=', 'sale.order'), 
            ('res_id', '=', order_id),
            ('message_type', '=', 'comment'),
        ], limit=1)

        if so_comment_mail.id:

            if len(so_comment_mail.notification_ids) > 0:
                so_comment_mail.notification_ids[0].email_status = 'read'

        return super(SaleQuote, self).view(order_id=order_id, pdf=pdf, token=token, message=message, post=post)