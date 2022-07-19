from odoo.exceptions import UserError
from odoo.tests import Form
from odoo.tests.common import TransactionCase

class TestStockMove(TransactionCase):

    def setUp(self):
        super(TestStockMove, self).setUp()
        self.demo_user = self.env['res.users'].create({
            'name': 'Demo User',
            'email': 'demo.example1.com',
            'login': 'demo',
            'groups': ['base.group_user']
        })
        self.stock_user = self.env['res.users'].create({
            'name': 'Stock User',
            'email': 'stock.example1.com',
            'login': 'stock',
            'groups': ['stock.group_stock_user']
        })
        self.product_1 = self.env['product.product'].create({
            'name': 'Product 1',
            'type': 'product',
        })
        self.product_2 = self.env['product.product'].create({
            'name': 'Product 2',
            'type': 'product',
        })
        self.product_3 = self.env['product.product'].create({
            'name': 'Product 3',
            'type': 'product',
        })
        self.location_1 = self.env['stock.location'].create({
            'name': 'Location 1',
            'usage': 'internal',
        })
        self.location_2 = self.env['stock.location'].create({
            'name': 'Location 2',
            'usage': 'internal',
        })
        self.location_3 = self.env['stock.location'].create({
            'name': 'Location 3',
            'usage': 'internal',
        })
        self.move1 = self.env['stock.move'].create({
            'name': 'test_in_1',
            'location_id': self.location_1.id,
            'location_dest_id': self.location_2.id,
            'product_id': self.product_1.id,
            'product_uom': 2,
            'product_uom_qty': 5.0,
            'picking_type_id': 1,
        })

    def test_stock_move_line_quantity_to_hand(self):
        with self.assertRaises(UserError):
            self.env['stock.move'].create({
                'name': 'test_in_1',
                'location_id': self.location_1.id,
                'location_dest_id': self.location_2.id,
                'product_id': self.product_1.id,
                'product_uom': 2,
                'product_uom_qty': 5.0,
                'picking_type_id': 1,
            })
