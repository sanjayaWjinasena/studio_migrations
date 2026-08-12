# -*- coding: utf-8 -*-
{
    'name': 'Studio Migrations',
    'version': '17.0.1.0.2',
    'summary': (
        'Landing zone for x_studio_* field ports on models without a '
        'dedicated BugFix-* module yet. Fields ported here get proper '
        'Python declarations so fresh installs and future upgrades no '
        'longer depend on Studio runtime state.'
    ),
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Extra Tools',
    'license': 'LGPL-3',
    'depends': [
        'base_setup',
        'sale',            # x_studio_sale_id -> sale.order relation
        'account',         # account.move / .line / .payment / .analytic.plan
        'stock',           # stock.location / stock.lot
        'product',         # product.product
        'project',         # project.update
        'BugFix-Sales',    # x_studio_sale_id.x_studio_bank_guarantee_approved
                           # walks into sale.order.x_studio_bank_guarantee_approved,
                           # which BugFix-Sales owns — must load first.
    ],
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'auto_install': False,
    'application': False,
}
