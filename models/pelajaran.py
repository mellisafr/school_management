from odoo import models, fields, api


class Pelajaran (models.Model):
    _name = 'school_management.pelajaran'
    _description = 'Pelajaran'
    _order = 'pelajaran asc'
    _rec_name = 'pelajaran'

    pelajaran = fields.Char(string='Nama Gedung')
    guru_ids = fields.One2many(comodel_name='school_management.guru', inverse_name='pelajaran_id', string='Nama Guru')
    tipe_mapel = fields.Selection([
        ('umum', 'Umum'),
        ('jurusan', 'Jurusan'),
    ], string='Tipe', default='umum')