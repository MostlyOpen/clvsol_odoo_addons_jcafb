# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class LabTestRequestCodePool(models.Model):
    _description = 'Lab Test Request Code Pool'
    _name = "clv.lab_test.request.code_pool"
    _inherit = 'clv.abstract.pool'

    code_sequence = fields.Char(string='Code Sequence', default='clv.lab_test.request.code')
