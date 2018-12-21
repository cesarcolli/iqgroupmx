# -*- coding: utf-8 -*-
# © <2018> <Omar Torres (otorresgi18@gmail.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class MailNotification(models.Model):
    _inherit = 'mail.notification'

    email_status = fields.Selection(
        selection_add=[
            ('read', 'Leído')
        ]
    )