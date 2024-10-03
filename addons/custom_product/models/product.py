from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Product(models.Model):
    _name = 'custom.product'
    _description = 'Product'

    name = fields.Char(string='Название', required=True)
    color = fields.Char(string='Цвет')
    delivery_date = fields.Date(string='Дата поставки')
    price = fields.Float(string='Цена', required=True)
    quantity = fields.Integer(string='Количество')
    height = fields.Float(string='Высота')
    width = fields.Float(string='Ширина')
    depth = fields.Float(string='Глубина')
    volume = fields.Float(string='Объём', compute='_compute_volume', store=True)

    @api.depends('height', 'width', 'depth')
    def _compute_volume(self):
        for record in self:
            if record.height and record.width and record.depth:
                record.volume = record.height * record.width * record.depth
            else:
                record.volume = 0.0

    @api.constrains('price')
    def _check_price_positive(self):
        for record in self:
            if record.price < 0:
                raise ValidationError('Цена не может быть отрицательной.')
