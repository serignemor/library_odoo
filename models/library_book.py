from odoo import fields, models


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Un livre de la bibliothèque'

    name = fields.Char(string='Titre', required=True)
    authors = fields.Many2many('res.partner', string='Auteurs')
    publishing_house = fields.Char(string='Editeur')
    publication_date = fields.Date(string='Date de publication')
    image = fields.Binary(string='Image de couverture')
    isbn = fields.Char(string='ISBN')
    status = fields.Selection([
        ('public', 'Public'),
        ('private', 'Privé'),
    ], default='public', string='Statut')

