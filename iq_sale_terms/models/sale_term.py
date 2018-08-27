from odoo import api, fields, models, exceptions, _


class SaleTerm(models.Model):
    _description = 'IQ sale term'
    _name = 'iq.sale.term'

    name = fields.Char(
        'Name', required=True, translate=True,
        help="Nombre de la condición comercial")
    code = fields.Char(
        'Code', size=3, required=True,
        help="Codigo de la condición comercial")
    active = fields.Boolean(
        'Active', default=True,
        help="Indica si está activo")
    term_type = fields.Selection([
        ('delivery', 'Tiempo de entrega'),
        ('installation-time', 'Tiempo de instalación'),
        ('equipment', 'Equipo'),
        ('installation', 'Instalación'),
        ('expenses', 'Viáticos'),
        ('civil-work', 'Obra civil y eléctrico'),
        ('shipping', 'Envío')],
        readonly=True, default='draft', translate=True)
