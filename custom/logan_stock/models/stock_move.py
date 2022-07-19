from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class StockMoveExtend(models.Model):
    _inherit = 'stock.move'

    location_qty_available = fields.Float(string='Cantidad disponible', compute='_compute_location_qty_available')

    #Computa la cantidad disponible en el almacén de origen
    @api.depends('product_id', 'location_id')
    def _compute_location_qty_available(self):
        for location in self:
            if location.product_id and location.location_id:
                location.location_qty_available = location.product_id.with_context(location=location.location_id.id).qty_available
            else:
                location.location_qty_available = 0.0
