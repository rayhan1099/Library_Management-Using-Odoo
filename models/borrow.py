from odoo import models, fields

class Borrow(models.Model):
    _name = 'library.borrow'
    _description = 'Library Borrow'

    book_id = fields.Many2one('library.book', string='Book', required=True)
    borrower_name = fields.Char(string='Borrower Name', required=True)
    borrow_date = fields.Date(string='Borrow Date', required=True, default=fields.Date.today)
    return_date = fields.Date(string='Return Date')
    state = fields.Selection([
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
    ], string='Status', default='borrowed')
