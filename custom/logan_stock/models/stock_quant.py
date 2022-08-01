from odoo import models, fields, api


class StockQuantExtend(models.Model):

    _inherit = 'stock.quant'

    reason = fields.Char(string='Motivo de modificación', required=True)


    """
    Al 30 de julio del 2022 el equipo de desarrollo se dio cuenta que para poder crear un campo modificable dentro del
    stock.quant es necesario agregarlo en _get_inventory_fields_create (esto no pasa en odoo14)
    """
    @api.model
    def _get_inventory_fields_create(self):
        """ Returns a list of fields user can edit when he want to create a quant in `inventory_mode`.
        """
        res = super()._get_inventory_fields_create()
        res.append('reason')
        return res
