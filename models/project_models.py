# -*- coding: utf-8 -*-
"""project.update Studio-field port."""
from odoo import fields, models


class ProjectUpdate(models.Model):
    _inherit = 'project.update'

    x_studio_actual_gp = fields.Float(
        string='Actual GP',
    )
