from odoo import models, fields

class Author(models.Model):
    _name = 'library.author'
    _description = 'Library Author'

    name = fields.Char(string='Name', required=True)
    birthdate = fields.Date(string='Birth Date')
    biography = fields.Text(string='Biography')
