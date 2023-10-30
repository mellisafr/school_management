from odoo import models, fields, api

class Kehadiran (models.Model):
    _name = 'school_management.kehadiran'
    _description = 'Kehadiran'
    _order = 'murid_id asc'
    _rec_name = 'murid_id'

    presensi_id = fields.Many2one('school_management.presensi')
    murid_id = fields.Many2one('school_management.murid')
    status_murid = fields.Selection([
        ('hadir', 'Hadir'), 
        ('sakit', 'Sakit'), 
        ('izin', 'Izin'),
        ('alfa', 'Alfa')
    ], default='hadir', required=True)