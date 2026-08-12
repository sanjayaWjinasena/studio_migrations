# -*- coding: utf-8 -*-
"""Post-install cleanup hook for studio_migrations.

Strips studio_customization ir.model.data rows that duplicate ownership
of the fields this module now declares. Idempotent.
"""
import logging

_logger = logging.getLogger(__name__)

# (model, field_name) pairs — kept in sync with models/*.py.
_PORTED_FIELDS = (
    ('account.move',       'x_studio_account_mandatory'),
    ('account.move',       'x_studio_advance_acc_updated'),
    ('account.move',       'x_studio_sale_id'),
    ('account.move',       'x_studio_bank_guarantee_approved'),
    ('account.move.line',  'x_studio_aaa'),
    ('account.move.line',  'x_studio_account_mandatory'),
    ('account.move.line',  'x_studio_analytic_group'),
    ('account.payment',    'x_studio_advance_payment_acc_updated'),
    ('product.product',    'x_studio_available_qty'),
    ('project.update',     'x_studio_actual_gp'),
    ('res.users',          'x_studio_attendance_administrator'),
    ('stock.location',     'x_color'),
    ('stock.lot',          'x_currency_id'),
)


def strip_studio_xmlids_for_ported_fields(env):
    Fields = env['ir.model.fields'].sudo()
    IMD = env['ir.model.data'].sudo()

    field_ids = []
    for model, name in _PORTED_FIELDS:
        rec = Fields.search([('model', '=', model), ('name', '=', name)], limit=1)
        if rec:
            field_ids.append(rec.id)

    if not field_ids:
        return

    stale = IMD.search([
        ('module', '=', 'studio_customization'),
        ('model', '=', 'ir.model.fields'),
        ('res_id', 'in', field_ids),
    ])
    if not stale:
        return

    _logger.info(
        "studio_migrations: unlinking %d studio_customization xmlids for "
        "fields now owned by this module.",
        len(stale),
    )
    stale.unlink()


def post_init_hook(env):
    strip_studio_xmlids_for_ported_fields(env)
