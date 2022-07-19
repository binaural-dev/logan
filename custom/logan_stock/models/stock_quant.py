from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class StockQuantExtend(models.Model):
    _inherit = 'stock.quant'

    reason = fields.Char(string='Motivo de modificación', required=True)

    @api.constrains('reason')
    def _check_reason(self):
        for record in self:
            if not record.reason:
                raise ValidationError('El motivo de modificación es requerido')
