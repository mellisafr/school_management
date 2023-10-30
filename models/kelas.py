from odoo import models, fields, api


class Kelas (models.Model):
    _name = 'school_management.kelas'
    _description = 'Kelas'
    _order = 'kelas asc'
    _rec_name = 'kelas'

    tingkat = fields.Selection([
        ('10', '10'),
        ('11', '11'),
        ('12', '12')
    ], string='Tingkat')
    jurusan = fields.Selection([
        ('RPL', 'Rekayasa Perangkat Lunak'),
        ('TKJ', 'Teknik Komputer Jaringan'),
        ('SIJA', 'Sistem Informatika Jaringan dan Aplikasi')
    ], string='Jurusan')
    rombel = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    ], string='Rombel')
    wali_kelas_id = fields.Many2one(comodel_name='school_management.guru', string='Wali Kelas')
    jumlah_murid = fields.Char(string='Jumlah Murid')
    murid_ids = fields.One2many(comodel_name='school_management.murid', inverse_name='kelas_id', string='Daftar Murid')
    gedung_id = fields.Many2one(comodel_name='school_management.gedung', string='Letak')
    
    kelas = fields.Char()

    @api.onchange('tingkat','jurusan', 'rombel')
    def _onchange_kelas(self):
        if self.tingkat and self.jurusan and self.rombel:
            self.kelas = str(self.tingkat) + ' ' + str(self.jurusan) + ' ' + str(self.rombel)
        else:
            self.kelas = ''