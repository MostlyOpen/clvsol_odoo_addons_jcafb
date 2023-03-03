# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import UserError


class PatientRec(models.Model):
    _name = "clv.patient_rec"
    _inherit = 'clv.patient_rec', 'clv.abstract.code'

    code = fields.Char(string='Patient Code', required=False, default=False)
    code_sequence = fields.Char(default='clv.person.code')

    @api.constrains('code')
    def _check_code(self):

        for record in self:

            if record.code is not False:

                sequence_str = ''
                for c in record.code:
                    if c.isdigit():
                        sequence_str = sequence_str + c
                sequence_str = sequence_str[:len(sequence_str) - 2]
                format_code = self.env['clv.abstract.code'].format_code(sequence_str)

                if record.code != format_code:
                    raise UserError(u'Invalid Code!')
