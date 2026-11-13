# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    openjanela_url = fields.Char(
        string='OpenJanela URL',
        help='Address of your OpenJanela server (hosted or self-hosted), '
             'e.g. https://openjanelaerp.com. The OpenJanela app menu opens '
             'this address in a new tab.',
        config_parameter='openjanela.url',
    )
