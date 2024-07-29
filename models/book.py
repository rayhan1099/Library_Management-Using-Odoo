from odoo import models, fields

class Book(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    author_id = fields.Many2one('library.author', string='Author')
    category_id = fields.Many2one('library.category', string='Category')
    isbn = fields.Char(string='ISBN')
    published_date = fields.Date(string='Published Date')
    copies_available = fields.Integer(string='Copies Available')
