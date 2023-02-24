# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import UserError


class PatientAux(models.Model):
    _name = "clv.patient_aux"
    _inherit = 'clv.patient_aux', 'clv.abstract.code'

    code = fields.Char(string='Patient Code', required=False, default=False)
    code_sequence = fields.Char(default='clv.person.code')

    def _patient_aux_set_code(self):

        for patient_aux in self:

            if patient_aux.code is False:

                vals = {}

                if patient_aux.related_patient_id.id is not False:
                    if patient_aux.related_patient_id.code is not False:
                        vals['code'] = patient_aux.related_patient_id.code
                    else:
                        vals['code'] = '/'

                else:
                    vals['code'] = '/'

                patient_aux.write(vals)

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
