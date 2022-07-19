from odoo.addons.mail.tests.common import mail_new_test_user
from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase
from odoo.tests import tagged

@tagged('post_install', '-at_install')
class TestStockMoveLine(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super(TestStockMoveLine, cls).setUpClass()
        cls.demo_user = mail_new_test_user(
            cls.env,
            name='Demo User',
            email = 'demo.example1.com',
            login='demo',
            groups='base.group_user'
            )
        cls.stock_user = mail_new_test_user(
            cls.env,
            name='Stock User',
            email = 'stock.example1.com',
            login='stock',
            groups='stock.group_stock_user'
            )
        cls.product_1 = cls.env['product.product'].create({
            'name': 'Product 1',
            'type': 'product',
        })
        cls.product_2 = cls.env['product.product'].create({
            'name': 'Product 2',
            'type': 'product',

        })
        cls.product_3 = cls.env['product.product'].create({
            'name': 'Product 3',
            'type': 'product',
        })

        cls.location_1 = cls.env['stock.location'].create({
            'name': 'Location 1',
            'usage': 'internal',
        })
        cls.location_2 = cls.env['stock.location'].create({
            'name': 'Location 2',
            'usage': 'internal',
        })
        cls.location_3 = cls.env['stock.location'].create({
            'name': 'Location 3',
            'usage': 'internal',
        })

        cls.move1 = cls.env['stock.move'].create({
            'name': 'test_in_1',
            'location_id': cls.location_1.id,
            'location_dest_id': cls.location_2.id,
            'product_id': cls.product_1.id,
            'product_uom': 2,
            'product_uom_qty': 5.0,
            'picking_type_id': 1,
        })

        cls.move2 = cls.env['stock.move'].create({
            'name': 'test_in_1',
            'location_id': cls.location_1.id,
            'location_dest_id': cls.location_2.id,
            'product_id': cls.product_1.id,
            'product_uom': 2,
            'product_uom_qty': 5.0,
            'picking_type_id': 1,
        })

        cls.move_line = cls.env['stock.move.line'].create({
             'move_id': cls.move1.id,
            'product_id': cls.product_1.id,
            'qty_done': 5.0,
            'product_uom_id': 2,
            'location_id': cls.location_1.id,
            'location_dest_id': cls.location_2.id,
            'user': cls.demo_user.id,
        })

    def test_user_equal_to_move_user(self):
        self.move_line.user = self.demo_user.id
        self.assertTrue(self.move_line.user)

    def test_stock_move_line_create_with_reason_and_user(self):
        move = self.env['stock.move.line'].create({
            'move_id': self.move1.id,
            'product_id': self.product_1.id,
            'qty_done': 5.0,
            'product_uom_id': 2,
            'location_id': self.location_1.id,
            'location_dest_id': self.location_2.id,
            'user': self.demo_user.id,
        })
        self.assertTrue(move.user)
