# -*- coding: utf-8 -*-
# © <2018> <Omar Torres (otorres@proogeeks.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class iq_customer_project(models.Model):
    _name = 'iq.customer.project'
    _description = 'IQ CUSTOMER PROJECT'

    name = fields.Char(
        string='Nombre',
        required=True
    )
    folio = fields.Char(
        string='Folio'
    )
    customer_id = fields.Many2one(
        string='Cliente',
        comodel_name='res.partner'
    )
    doc_date = fields.Date(
        string='Fecha'
    )
    customer_num = fields.Char(
        string='Número de Cliente'
    )
    currency = fields.Selection(
        string='Moneda',
        selection=[
            ('MX', 'MX'), 
            ('USD', 'USD'),
            ('EUR', 'EUR')
        ],
        size=3
    )
    waranty_start = fields.Date(
        string='Fecha Inicio de Garantía'
    )
    waranty_end = fields.Date(
        string='Fecha Fin de Garantía'
    )
    customer_num = fields.Char(
        string='Número de Cliente'
    )
    project_name = fields.Char(
        string='Nombre del Proyecto'
    )
    trade_name = fields.Char(
        string='Nombre Comercial del Cliente'
    )
    ledger_name = fields.Char(
        string='Razón Social'
    )
    customer_rfc = fields.Char(
        string='R.F.C'
    )
    customer_contacts = fields.Char(
        string='Contactos'
    )
    iq_contact_ids = fields.One2many(
        string='Contactos',
        comodel_name='iq.customer.contact',
        inverse_name='iq_project_id'
    )
    operator_name = fields.Char(
        string='Nombre Comercial'
    )
    operator_ledger_name = fields.Char(
        string='Razón Social'
    )
    operator_rfc = fields.Char(
        string='R.F.C'
    )
    op_contacts = fields.Char(
        string='Contactos'
    )
    op_contact_ids = fields.One2many(
        string='Contactos',
        comodel_name='iq.operator.contact',
        inverse_name='iq_project_id'
    )
    product_a = fields.Char(
        string='Equipo estacionamiento'
    )
    product_b = fields.Char(
        string='Mantenimiento'
    )
    product_c = fields.Char(
        string='Boletos'
    )
    product_d = fields.Char(
        string='Refacciones'
    )
    product_a_type = fields.Selection(
        string='Equipo estacionamiento',
        size=1,
        selection=[
            ('C', 'Cliente'),
            ('O', 'Operador')
        ]
    )
    product_b_type = fields.Selection(
        string='Mantenimiento',
        size=1,
        selection=[
            ('C', 'Cliente'),
            ('O', 'Operador')
        ]
    )
    product_c_type = fields.Selection(
        string='Boletos',
        size=1,
        selection=[
            ('C', 'Cliente'),
            ('O', 'Operador')
        ]
    )
    product_d_type = fields.Selection(
        string='Refacciones',
        size=1,
        selection=[
            ('C', 'Cliente'),
            ('O', 'Operador')
        ]
    )
    product_f_type = fields.Selection(
        string='Otros',
        size=1,
        selection=[
            ('C', 'Cliente'),
            ('O', 'Operador')
        ]
    )
    maint_policy = fields.Float(
        string='Póliza'
    )
    maint_policy_type = fields.Char(
        string='Tipo de póliza'
    )
    maint_policy_a = fields.Char(
        string='a) 5x8x5 con 1 Prv. Y 1 Corr.'
    )
    maint_policy_b = fields.Char(
        string='b) 7x24x365 con 1 Prev. y 1 Corr.'
    )
    maint_policy_c = fields.Char(
        string='c) Técnico en sitio'
    )
    maint_policy_d = fields.Char(
        string='d) Fecha de facturación'
    )
    maint_policy_e = fields.Char(
        string='e) Otros'
    )
    ticket_month = fields.Float(
        string='1.- Consumo mensual promedio'
    )
    ticket_order_type = fields.Char(
        string='2.- Tipo de orden'
    )
    ticket_custom = fields.Char(
        string='3.- Boleto personalizado'
    )
    ticket_brand = fields.Char(
        string='Marca'
    )
    ticket_model = fields.Char(
        string='Modelo'
    )
    ticket_tech = fields.Char(
        string='Tecnología'
    )
    ticket_order_interval = fields.Char(
        string='5.- Frecuencia de surtido'
    )
    price_ticket = fields.Char(
        string='1.- Boletos'
    )
    price_arm_bar = fields.Char(
        string='2.- Brazos de barrera'
    )
    price_car_bar = fields.Char(
        string='3.- Barrera Vehicular'
    )
    price_pension_card = fields.Char(
        string='4.- Tarjetas de pensionados'
    )
    price_service_call = fields.Char(
        string='5.- Llamada de Servicio'
    )
    comments = fields.Text(
        string='Observaciones'
    )


