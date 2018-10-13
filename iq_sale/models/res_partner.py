# -*- coding: utf-8 -*-
# © <2018> <Omar Torres (otorres@proogeeks.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def report_customer_address(self):

        return '%s%s%s\n%s%s%s%s%s%s%s' % (
            '%s' % self.street if self.street else '',
            '%s' % ', ' if self.street and self.street2 else '',
            '%s' % self.street2 if self.street2 else '',
            '%s' % self.zip if self.zip else '',
            '%s' % ', ' if self.zip and (self.city or self.state_id.id or self.country_id.id) else '',
            '%s' % self.city if self.city else '',
            '%s' % ', ' if self.city and (self.state_id.id or self.country_id.id) else '',
            '%s' % self.state_id.name if self.state_id.name else '',
            '%s' % ', ' if self.state_id.id and self.country_id.id else '',
            '%s' % self.country_id.name if self.country_id.name else ''            
        )