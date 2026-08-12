# -*- coding: utf-8 -*-
"""stock.location / stock.lot Studio-field port.

Both fields were created by Studio (state=manual) but without the
x_studio_ prefix — Studio permits x_ names too, so the DB columns are
literally x_color and x_currency_id. Preserved verbatim.
"""
from odoo import fields, models


class StockLocation(models.Model):
    _inherit = 'stock.location'

    x_color = fields.Integer(
        string='Color',
    )


class StockLot(models.Model):
    _inherit = 'stock.lot'

    # Studio's related was 'product_id.stock_valuation_layer_ids.currency_id'
    # which traverses a One2many — invalid for eager Python setup. Declared
    # as a plain stored m2o; existing column data is preserved.
    x_currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        ondelete='set null',
    )
