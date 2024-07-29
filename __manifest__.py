{
    'name': 'Library Management',
    'version': '1.0',
    'category': 'Tools',
    'sequence': 12,
    'summary': '',
    'description': """
    """,
    'depends': [],
    'data': [
        'views/book_views.xml',
        'views/author_views.xml',
        'views/category_views.xml',
        'views/borrow_views.xml',
        'security/ir.model.access.csv',
        'views/menu_views.xml',
    ],
    'category': '',

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
