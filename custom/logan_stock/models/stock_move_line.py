from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class StockMoveLoneExtend(models.Model):
    _inherit = 'stock.move.line'

    user = fields.Char(string='Modificado por:', compute='_compute_user')
    reason = fields.Char(string='Motivo de modificación', related='location_id.quant_ids.reason')

    @api.model
    def _compute_user(self):
        for record in self:
            record.user = record.create_uid.name
