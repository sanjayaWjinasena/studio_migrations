# -*- coding: utf-8 -*-
"""res.users Studio-field port."""
from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    x_studio_attendance_administrator = fields.Boolean(
        string='Attendance Administrator',
    )
