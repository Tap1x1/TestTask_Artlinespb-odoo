from odoo import api, fields, models


class SaleOrderInherited(models.Model):
    _inherit = 'sale.order'

    delivery_responsible = fields.Many2one('hr.employee', string='Оnтветственный за выдачу товара', required=True)
    test = fields.Char(string='Test', store=True, compute='_compute_test', default=lambda self: self._generate_default_test(), readonly=True, states={'draft': [('readonly', False)]})

    @api.depends('order_line', 'date_order', 'state')
    def _compute_test(self):
        for order in self:
            if order.state == 'draft':
                order.test = f"{order.amount_total} - {order.date_order.strftime('%d/%m/%Y %H:%M:%S')}"
            else:
                if order.test:
                    order.test = order.test
                else:
                    order.test = False

    @api.model
    def _generate_default_test(self):
        import random
        import string
        return ''.join(random.choice(string.ascii_letters) for _ in range(10))

    @api.onchange('test')
    def _check_test_length(self):
        for order in self:
            if order.test and len(order.test) > 50:
                raise models.ValidationError('Длина текста должна быть меньше 50 символов!')