# -*- coding: utf-8 -*-
"""account.move / .line / .payment Studio-field port.

Fields Studio owned on the accounting layer that Fix-repair's Python
code reads and writes to (x_studio_account_mandatory, the
x_studio_advance_acc_updated / x_studio_advance_payment_acc_updated
flags, and the x_studio_sale_id -> x_studio_bank_guarantee_approved
chain that mirrors credit-gate state from sale.order onto invoices).
"""
from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    x_studio_account_mandatory = fields.Boolean(
        string='Account Mandatory',
    )
    x_studio_advance_acc_updated = fields.Boolean(
        string='Advance ACC Updated',
    )
    # Companion field needed by the related below; also referenced by
    # Studio-era view arch that ties an invoice to its originating SO.
    x_studio_sale_id = fields.Many2one(
        'sale.order',
        string='Sale Order',
        ondelete='set null',
    )
    x_studio_bank_guarantee_approved = fields.Boolean(
        string='Bank Guarantee Approved',
        related='x_studio_sale_id.x_studio_bank_guarantee_approved',
        store=True,
        readonly=True,
    )


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    # Studio's related expression traverses product_id.pricelist_id.item_ids
    # (item_ids is a One2many) which Odoo's related resolver rejects on
    # eager Python setup. Declared as a plain non-stored char — the DB
    # column never existed (store=False in Studio), so no data is lost.
    x_studio_aaa = fields.Char(
        string='AAA',
        readonly=True,
    )
    x_studio_account_mandatory = fields.Boolean(
        string='Account Mandatory',
    )
    x_studio_analytic_group = fields.Many2one(
        'account.analytic.plan',
        string='Analytic Group',
        ondelete='set null',
    )


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    x_studio_advance_payment_acc_updated = fields.Boolean(
        string='Advance Payment ACC Updated',
    )
