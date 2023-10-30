from odoo import models, fields, api


class Guru (models.Model):
    _name = 'school_management.guru'
    _description = 'Guru'
    _order = 'nama_guru asc'
    _rec_name = 'nama_guru'

    nama_guru = fields.Char(string='Nama Guru')
    pelajaran_id = fields.Many2one('school_management.pelajaran', string='Mata Pelajaran')
    waktu_mengajar = fields.Float(digits=(3, 0), default=0, string='Waktu Mengajar')