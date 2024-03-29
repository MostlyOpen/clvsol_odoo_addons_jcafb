# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PatientLabTestResultSetUp(models.TransientModel):
    _description = 'Patient Lab Test Result Setup'
    _name = 'clv.patient.lab_test_result_setup'

    def _default_patient_ids(self):
        return self._context.get('active_ids')
    patient_ids = fields.Many2many(
        comodel_name='clv.patient',
        relation='clv_patient_lab_test_result_setup_rel',
        string='Patients',
        default=_default_patient_ids
    )

    lab_test_type_ids = fields.Many2many(
        comodel_name='clv.lab_test.type',
        relation='clv_patient_lab_test_result_setup_lab_test_type_rel',
        string='Lab Test Types'
    )

    def _default_phase_id(self):
        phase_id = int(self.env['ir.config_parameter'].sudo().get_param(
            'clv.global_settings.current_phase_id', '').strip())
        return phase_id
    phase_id = fields.Many2one(
        comodel_name='clv.phase',
        string='Phase',
        default=_default_phase_id,
        ondelete='restrict'
    )

    def do_patient_lab_test_result_setup(self):
        self.ensure_one()

        LabTestResult = self.env['clv.lab_test.result']

        for patient in self.patient_ids:

            ref_id = patient._name + ',' + str(patient.id)

            _logger.info(u'%s %s %s', '>>>>>', patient.name, ref_id)

            for lab_test_type in self.lab_test_type_ids:
                # m2m_list = []
                # m2m_list.append((4, lab_test_type.id))

                ref_id = patient._name + ',' + str(patient.id)

                _logger.info(u'%s %s %s', '>>>>>>>>>>', ref_id, lab_test_type.id)

                values = {
                    'code_sequence': 'clv.lab_test.result.code',
                    'lab_test_type_id': lab_test_type.id,
                    'survey_id': lab_test_type.survey_id.id,
                    'ref_id': ref_id,
                    'phase_id': self.phase_id.id,
                }
                lab_test_result = LabTestResult.create(values)

                _logger.info(u'%s %s', '>>>>>>>>>>', lab_test_result.code)

        return True
