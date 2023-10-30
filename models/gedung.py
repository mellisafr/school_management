from odoo import models, fields, api


class Gedung (models.Model):
    _name = 'school_management.gedung'
    _description = 'Gedung'
    _order = 'gedung asc'
    _rec_name = 'gedung'

    gedung = fields.Char(string='Nama Gedung')
    kelas_ids = fields.One2many(comodel_name='school_management.kelas', inverse_name='gedung_id', string='Kelas')