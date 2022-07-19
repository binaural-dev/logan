
from odoo.addons.mail.tests.common import mail_new_test_user
from odoo.addons.product.tests import common

class TestStockCommon(common.TestProductCommon):
    @classmethod
    def setUpClass(cls):
        super(TestStockCommon, cls).setUpClass()

        cls.user_stock_user = mail_new_test_user(
            cls.env,
            name='User Stock User',
            email = 'user.example1.com',
            login='stock_user', 
            groups='stock.group_stock_user'
            )
        cls.user_stock_manager = mail_new_test_user(
            cls.env,
            name='User Stock Manager',
            email =  'user.example2.com',
            login='stock_manager', 
            groups='stock.group_stock_manager'
            )

        
