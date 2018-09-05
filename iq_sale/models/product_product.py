# -*- coding: utf-8 -*-
# © <2018> <Omar Torres (otorresgi18@gmail.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    tech_file_id = fields.Many2one(
        string='Ficha técnica',
        comodel_name='ir.attachment',
        domain="[('res_id', '=', id)]"
    )

    @api.multi
    def product_pdf_preview(self):

    	return {
            'type' : 'ir.actions.act_url',
            'url': '/web/pdf_viewer/%s/%s' % (self.tech_file_id.id, self.tech_file_id.name),
            'target': 'new'
        }

    def tech_file_url(self):

        url = self.env['ir.config_parameter'].get_param('web.base.url', '').strip()

        return '%s/web/pdf_viewer/%s/%s' % (url, self.tech_file_id.id, self.tech_file_id.name) if self.tech_file_id.id else False
