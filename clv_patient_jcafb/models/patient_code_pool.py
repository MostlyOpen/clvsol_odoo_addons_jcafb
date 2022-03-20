# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PatientCodePool(models.Model):
    _description = 'Patient Code Pool'
    _name = "clv.patient.code_pool"
    _inherit = 'clv.abstract.code_pool', 'clv.abstract.code'

    code = fields.Char(string='Patient Code', required=False, default='/')

    code_sequence = fields.Char(default='clv.person.code')

    patient_id = fields.Many2one(
        comodel_name='clv.patient',
        string='Related Patient',
        ondelete='restrict'
    )
