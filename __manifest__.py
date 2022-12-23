# -*- coding: utf-8 -*-
{
    'name': "library",

    'summary': """
        Gestion d'une bibliothèque""",

    'description': """
        Ce module permet de gérer une bibliothèque avec les fonctionnalités telles que 
        la gestion des livres, des auteurs, des lecteurs, etc.
    """,

    'author': "UADB2",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Library',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/library_security.xml',
        'views/library_book_form_view.xml',
        'views/library_book_list_view.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
