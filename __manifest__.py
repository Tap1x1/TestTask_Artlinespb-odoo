{
    'name': 'Odoo_Tap1x1',
    'version': '1.0',
    'author': 'Tap1x1',
    'category': 'Sales',
    'description': 'Модуль для добавления функционала в Quotations в Odoo Community Edition v.16',
    'depends': ['base','sale'],
    'data': [
        'views/sale_order_view.xml',
        'views/custom_sale_report.xml',
    ],
    'installable': True,
    'application': True,
}