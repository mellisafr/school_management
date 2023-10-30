from odoo import models, fields, api
import datetime 


class Presensi (models.Model):
    _name = 'school_management.presensi'
    _description = 'Presensi'
    _order = 'tanggal asc'
    _rec_name = 'tanggal'

    #status
    status_presensi = fields.Selection([
        ('rancangan', 'Rancangan'),
        ('selesai', 'Selesai')
    ], default='rancangan')

    #field mandatory
    tanggal = fields.Date(default=datetime.date.today())
    kelas_id = fields.Many2one('school_management.kelas', string='Kelas')
    pelajaran_id = fields.Many2one('school_management.pelajaran', string='Mata Pelajaran')
    guru_id = fields.Many2one('school_management.guru', string='Nama Guru')
    bukti_presensi = fields.Binary(string='Bukti Presensi')
    kehadiran_ids = fields.One2many('school_management.kehadiran', 'presensi_id')

    def action_selesai(self):
        self.write({'status_presensi': 'selesai'})
