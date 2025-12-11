# -*- coding: utf-8 -*-
{
    'name': 'Nóminas Tienda de Ropa',
    'version': '1.0',
    'author': 'Harold',
    'category': 'Human Resources',
    'summary': 'Gestión de nóminas y declaraciones de renta para la tienda de ropa',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/nomina_views.xml',
        'views/renta_anual_views.xml',
        'views/nominas_menu.xml',
    ],
    'installable': True,
    'application': True,
}
