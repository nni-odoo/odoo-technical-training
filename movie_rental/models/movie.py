from odoo import api, fields, models

class Movie(models.Model):
    _name = "movie.movie"

    name = fields.Char("Movie Name")
    year = fields.Integer("Year")
