# -*- coding: utf-8 -*-
# © <2018> <Omar Torres (otorres@proogeeks.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class product_tech_file(models.TransientModel):
    _name = 'product.tech.file'
    _description = 'PRODUCT TECH FILE'

    product_id = fields.Many2one(
        string='Producto',
        comodel_name='product.template'
    )
    tech_file = fields.Binary(
        string='Ficha técnica'
    )
    filename = fields.Char(
        string='Archivo'
    )

    @api.multi
    def load_tech_file(self):

        self.product_id.tech_file_id.unlink()

        file_id = self.env['ir.attachment'].create({
            'res_id': self.product_id.id,
            'res_model': 'product.template',
            'datas': self.tech_file,
            'name': self.filename
        })

        self.product_id.tech_file_id = file_id.id