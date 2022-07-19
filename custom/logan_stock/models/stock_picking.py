from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class StockPickingExtend(models.Model):
    _inherit = 'stock.picking'

    def action_confirm(self):
        res = super(StockPickingExtend, self).action_confirm()
        for record in self.move_ids_without_package:
            if record.location_qty_available <= 0:
                raise UserError('No puede confirmar una transferencia si no hay existencias en el almacén de origen')
        return res