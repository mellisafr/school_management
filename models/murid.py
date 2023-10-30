from odoo import models, fields, api


class Murid (models.Model):
    _name = 'school_management.murid'
    _description = 'Murid'
    _order = 'kelas_id asc'
    _rec_name = 'nama_murid'

    nama_murid = fields.Char(string='Nama Murid')
    kelas_id = fields.Many2one('school_management.kelas', string='Kelas')
    gender = fields.Selection([
        ('p', 'Perempuan'),
        ('l', 'Laki-laki')
    ], string='Jenis Kelamin')