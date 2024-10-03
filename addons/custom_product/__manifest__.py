{
    'name': 'Custom Product',
    'version': '16.0.1.0.0',
    'summary': 'Кастомный модуль для управления товарами',
    'description': """
        Модуль добавляет модель товара с дополнительными полями и представлениями.
    """,
    'author': 'Ваше Имя',
    'website': 'http://yourwebsite.com',
    'category': 'Inventory',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
