{
    'name': "Dispatch Management System",
    'version': '1.0',
    'depends': ['base','fleet','stock_picking_batch'],
    'author': "Dhruvin (dhka)",
    'category': 'Category',
    'description': """
    Description text
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_vehicle_model_category.xml',
        'views/stock_picking_batch_views.xml',
        'views/stock_picking_views.xml',
    ],
}
