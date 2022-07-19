{
	# Theme information
	'name' : 'Inventario Logan',
	'category' : 'Inventario',
	'version' : '15.0.0.1',
	'summary': 'Agrega campos para el inventario',
	'description': """
		
	""",
    
	# Dependencies
	'depends': [
		'base',
		'stock',
	],
	# Views
	'data': [
        'views/stock_move_line.xml',
		'views/stock_quant.xml',
		'views/stock_picking.xml',
	],
	# Author
	'author': 'binaural',
	'website': '',
	'maintainer': 'binaual',

	# Technical
	'installable': True,
	'auto_install': False,
}
