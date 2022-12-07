# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PatientAuxLabTestRequestSetup_2(models.TransientModel):
    _description = 'Patient Lab Test Request Setup 2'
    _name = 'clv.patient_aux.lab_test.request.setup_2'

    def _default_patient_aux_ids(self):
        return self._context.get('active_ids')
    patient_aux_ids = fields.Many2many(
        comodel_name='clv.patient_aux',
        relation='clv_patient_aux_patient_aux_lab_test_request_setup_2_rel',
        string='Patients (Aux)',
        default=_default_patient_aux_ids
    )

    # lab_test_type_ids = fields.Many2many(
    #     comodel_name='clv.lab_test.type',
    #     relation='clv_lab_test_type_patient_aux_lab_test_request_setup_2_rel',
    #     string='Lab Test Types'
    # )

    lab_test_type_id = fields.Many2one(
        comodel_name='clv.lab_test.type',
        string='Lab Test Types'
    )

    lab_test_request_code = fields.Char(string='Lab Test Request Code', required=True, default='/')

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

    def do_patient_aux_lab_test_request_setup_2(self):
        self.ensure_one()

        LabTestRequest = self.env['clv.lab_test.request']

        for patient_aux in self.patient_aux_ids:

            _logger.info(u'%s %s', '>>>>>', patient_aux.name)

            # for lab_test_type in self.lab_test_type_ids:

            lab_test_type = self.lab_test_type_id

            m2m_list = []
            m2m_list.append((4, lab_test_type.id))

            ref_id = patient_aux._name + ',' + str(patient_aux.id)

            _logger.info(u'%s %s %s', '>>>>>>>>>>', ref_id, m2m_list)

            values = {
                'code_sequence': 'clv.lab_test.request.code',
                'code': self.lab_test_request_code,
                'lab_test_type_ids': m2m_list,
                'ref_id': ref_id,
                'phase_id': self.phase_id.id,
            }
            lab_test_request = LabTestRequest.create(values)

            _logger.info(u'%s %s', '>>>>>>>>>>', lab_test_request.code)

        return True
