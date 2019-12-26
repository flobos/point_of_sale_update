# -*- coding: utf-8 -*-
{
    'name': "point_of_sale_update",

    'summary': """
        Agrega al modulo de PoS un form para confirmar la venta""",

    'description': """
        Agrega al modulo de PoS un form para confirmar la venta
    """,

    'author': "Fernando Lobos",
    'website': "https://github.com/flobos",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','point_of_sale','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}