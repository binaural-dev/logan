from odoo.addons.mail.tests.common import mail_new_test_user
from odoo.exceptions import ValidationError, UserError
from odoo.tests.common import SavepointCase, Form
from odoo.tests import tagged



@tagged('post_install', '-at_install')
class TestStockQuant(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(TestStockQuant, cls).setUpClass()

        cls.StockQuant = cls.env['stock.quant']
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

        cls.product_4 = cls.env['product.product'].create({
            'name': 'Product 4',
            'type': 'product',
        })

        cls.product_5 = cls.env['product.product'].create({
            'name': 'Product 5',
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
        
        cls.location_4 = cls.env['stock.location'].create({
            'name': 'Location 4',
            'usage': 'internal',
        })

        cls.location_5 = cls.env['stock.location'].create({
            'name': 'Location 5',
            'usage': 'internal',
        })

        cls.location_6 = cls.env['stock.location'].create({
            'name': 'Location 6',
            'usage': 'internal',
        })
        
        cls.quant_1 = cls.StockQuant.create({
            'user_id': cls.stock_user.id,
            'product_id': cls.product_1.id,
            'location_id': cls.location_1.id,
            'quantity': 5.0,
            'reason': 'Test',
        })

        cls.quant_2 = cls.StockQuant.create({
            'user_id': cls.stock_user.id,
            'product_id': cls.product_1.id,
            'location_id': cls.location_1.id,
            'quantity': 5.0,
            'reason': 'Test',
        })

        cls.quant_3 = cls.StockQuant.create([{
            'user_id': cls.stock_user.id,
            'product_id': cls.product_1.id,
            'location_id': cls.location_1.id,
            'quantity': 5.0,
            'reason': 'aaa',
        }])

    def test_03_stock_quant_create_without_reason(self):
        """
        Test creando stock quant sin motivo
        """
        with self.assertRaises(ValidationError):
            self.StockQuant.create({
                'user_id': self.stock_user.id,
                'product_id': self.product_1.id,
                'location_id': self.location_1.id,
                'quantity': 5.0,
                'reason': False,
            })


    def test_property_user(self):
        """
        Test que comprueba que el campo user es correcto
        """
        self.assertEqual(self.quant_1.user_id.name, self.stock_user.name)


    def test_property_reason(self):
        """
        Test que comprueba que el campo reason es correcto
        """
        self.assertEqual(self.quant_2.reason, 'Test')
        