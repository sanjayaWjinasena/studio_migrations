# -*- coding: utf-8 -*-
"""product.product Studio-field port.

Studio's original related expression was 'stock_quant_ids.available_quantity'
which traverses a One2many — Odoo's related resolver rejects that on
eager Python setup. Reimplemented as a small compute that sums
available_quantity across quants, preserving the field's original intent.
"""
from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    x_studio_available_qty = fields.Float(
        string='Available Qty',
        compute='_compute_x_studio_available_qty',
        readonly=True,
    )

    @api.depends('stock_quant_ids.available_quantity')
    def _compute_x_studio_available_qty(self):
        for rec in self:
            rec.x_studio_available_qty = sum(
                rec.stock_quant_ids.mapped('available_quantity')
            )
