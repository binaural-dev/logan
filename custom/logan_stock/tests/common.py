from odoo.tests import common

class TestStockCommon(common.SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(TestStockCommon, cls).setUpClass()
        
        cls.ProductObj = cls.env['product.product']
        cls.product_quant = cls.env['product.quant']
        cls.product_template = cls.env['product.template']
        cls.StockPackObj = cls.env['stock.move.line']
        cls.PickingObj = cls.env['stock.picking']



        # Create product

        cls.productA = cls.ProductObj.create({'name': 'Product A', 'type': 'product'})
        cls.productB = cls.ProductObj.create({'name': 'Product B', 'type': 'product'})
        cls.productC = cls.ProductObj.create({'name': 'Product C', 'type': 'product'})
        cls.productD = cls.ProductObj.create({'name': 'Product D', 'type': 'product'})

        # Create quant

        cls.quantA = cls.product_quant.create({'product_id': cls.productA.id, 'qty': 10})
        cls.quantB = cls.product_quant.create({'product_id': cls.productB.id, 'qty': 10})
        cls.quantC = cls.product_quant.create({'product_id': cls.productC.id, 'qty': 10})
        cls.quantD = cls.product_quant.create({'product_id': cls.productD.id, 'qty': 10})

        # Create template

        cls.templateA = cls.product_template.create({'name': 'Template A', 'type': 'product'})
        cls.templateB = cls.product_template.create({'name': 'Template B', 'type': 'product'})
        cls.templateC = cls.product_template.create({'name': 'Template C', 'type': 'product'})
        cls.templateD = cls.product_template.create({'name': 'Template D', 'type': 'product'})

        # Create template quant

        cls.template_quantA = cls.product_quant.create({'product_id': cls.templateA.id, 'qty': 10})
        cls.template_quantB = cls.product_quant.create({'product_id': cls.templateB.id, 'qty': 10})
        cls.template_quantC = cls.product_quant.create({'product_id': cls.templateC.id, 'qty': 10})
        cls.template_quantD = cls.product_quant.create({'product_id': cls.templateD.id, 'qty': 10})

        # Create pack

        cls.packA = cls.StockPackObj.create({'product_id': cls.templateA.id, 'product_uom_qty': 10})
        cls.packB = cls.StockPackObj.create({'product_id': cls.templateB.id, 'product_uom_qty': 10})
        cls.packC = cls.StockPackObj.create({'product_id': cls.templateC.id, 'product_uom_qty': 10})
        cls.packD = cls.StockPackObj.create({'product_id': cls.templateD.id, 'product_uom_qty': 10})

        # Create picking

        cls.pickingA = cls.PickingObj.create({
            'picking_type_id': cls.env.ref('stock.picking_type_out').id, 
            'location_id': cls.env.ref('stock.stock_location_stock').id, 
            'location_dest_id': cls.env.ref('stock.stock_location_customers').id
            })
        cls.pickingB = cls.PickingObj.create({
            'picking_type_id': cls.env.ref('stock.picking_type_out').id, 
            'location_id': cls.env.ref('stock.stock_location_stock').id, 
            'location_dest_id': cls.env.ref('stock.stock_location_customers').id
            })
        cls.pickingC = cls.PickingObj.create({
            'picking_type_id': cls.env.ref('stock.picking_type_out').id, 
            'location_id': cls.env.ref('stock.stock_location_stock').id, 
            'location_dest_id': cls.env.ref('stock.stock_location_customers').id
            })
        cls.pickingD = cls.PickingObj.create({
            'picking_type_id': cls.env.ref('stock.picking_type_out').id, 
            'location_id': cls.env.ref('stock.stock_location_stock').id, 
            'location_dest_id': cls.env.ref('stock.stock_location_customers').id
            })



