from odoo import api, fields, models, exceptions, _


class PartnerInterest(models.Model):
    _description = 'Partner interest category'
    _name = 'iq.partner.interest'

    name = fields.Char(string='Interest Name', required=True, translate=True)
    color = fields.Integer(string='Color Index')
    active = fields.Boolean(default=True, help="The active field allows you to hide the category without removing it.")
    partner_ids = fields.Many2many('res.partner', column1='x_interest_id', column2='partner_id', string='Partners')


class ResPartner(models.Model):
    """Assigns 'ref' from a sequence on creation and copying"""
    _inherit = 'res.partner'

    @api.multi
    def _get_next_ref(self, vals=None):
        return self.env['ir.sequence'].next_by_code('res.partner')

    @api.model
    def create(self, vals):
        if not vals.get('ref') and self._needsRef(vals=vals):
            vals['ref'] = self._get_next_ref(vals=vals)
        return super(ResPartner, self).create(vals)

    @api.multi
    def copy(self, default=None):
        default = default or {}
        if self._needsRef():
            default['ref'] = self._get_next_ref()
        return super(ResPartner, self).copy(default)

    @api.multi
    def write(self, vals):
        for partner in self:
            if not vals.get('ref') and partner._needsRef(vals) and \
                    not partner.ref:
                vals['ref'] = self._get_next_ref(vals=vals)
            super(ResPartner, partner).write(vals)
        return True

    @api.multi
    def _needsRef(self, vals=None):
        """
        Checks whether a sequence value should be assigned to a partner's 'ref'

        :param vals: known field values of the partner object
        :return: true iff a sequence value should be assigned to the\
                      partner's 'ref'
        """
        if not vals and not self:  # pragma: no cover
            raise exceptions.UserError(_(
                'Either field values or an id must be provided.'))
        # only assign a 'ref' to commercial partners
        if self:
            vals = {}
            vals['is_company'] = self.is_company
            vals['parent_id'] = self.parent_id
        return vals.get('is_company') or not vals.get('parent_id')

    @api.model
    def _commercial_fields(self):
        """
        Make the partner reference a field that is propagated
        to the partner's contacts
        """
        return super(ResPartner, self)._commercial_fields() + ['ref']

    @api.model
    def _default_interest(self):
        return self.env['iq.partner.interest'].browse(self._context.get('x_interest_id'))

    x_interest_id = fields.Many2many('iq.partner.interest', column1='partner_id',
                                     column2='x_interest_id', string='Categorías de interés', default=_default_interest)
