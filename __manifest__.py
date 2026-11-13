# -*- coding: utf-8 -*-
{
    'name': 'OpenJanela for Windows & Doors',
    'summary': 'Launch OpenJanela, the window & door configurator and production engine, from Odoo.',
    'description': """
Quoting configured windows and doors from Odoo
==============================================

This module adds an OpenJanela entry to your Odoo apps menu so your team can
reach your OpenJanela server (hosted or self-hosted) in one click.

OpenJanela is the quoting, drawing and production engine for window and door
makers: product configurator with rules-based pricing, shop drawings, bills of
material, cut lists and optimization, label printing, and shop-floor tracking.
It works *with* Odoo 19: quote configured windows and doors from the Odoo sales
order; prices, drawings and BOMs come back into Odoo.

The full integration is a thin API connection set up from the OpenJanela side
(Odoo JSON-2 API, no module needed inside Odoo). This launcher module only
provides discovery and a configurable link - it adds no tables, no fields on
your records and no business logic.
    """,
    'author': 'OpenJanela',
    'website': 'https://openjanelaerp.com',
    'category': 'Sales',
    'version': '19.0.1.0.0',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/openjanela_data.xml',
        'views/openjanela_menus.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': True,
    'currency': 'USD',
}
