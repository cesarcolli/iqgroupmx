# -*- coding: utf-8 -*-
# © <2018> <Omar Torres (otorres@proogeeks.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class iq_operator_contact(models.Model):
    _name = 'iq.operator.contact'
    _description = 'IQ OPERATOR CONTACT'

    name = fields.Char(
        string='Nombre',
        required=True
    )
    job_position = fields.Selection(
        string='Puesto',
        size=1,
        selection=[
            ('A', 'Gerente de Estacionamiento'),
            ('B', 'Gerente de plaza'),
            ('C', 'Recepción de facturas'),
            ('D', 'Responsable de pagos')
        ]
    )
    mail = fields.Char(
        string='Correo'
    )
    phone = fields.Char(
        string='Teléfono'
    )
    iq_project_id = fields.Many2one(
        string='Proyecto',
        comodel_name='iq.customer.project',
        ondelete='cascade'
    )
