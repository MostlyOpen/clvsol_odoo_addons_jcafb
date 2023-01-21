# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class LabTestReportAssociateToRelatedPatient(models.TransientModel):
    _description = 'Lab Test Report Associate to Related Patient'
    _name = 'clv.lab_test.report.associate_to_related_patient'

    def _default_lab_test_report_ids(self):
        return self._context.get('active_ids')
    lab_test_report_ids = fields.Many2many(
        comodel_name='clv.lab_test.report',
        relation='clv_lab_test_report_associate_to_related_patient_rel',
        string='Lab Test Reports',
        default=_default_lab_test_report_ids
    )

    def do_lab_test_report_associate_to_related_patient(self):
        self.ensure_one()

        lab_test_report_count = 0
        for lab_test_report in self.lab_test_report_ids:

            lab_test_report_count += 1

            _logger.info(u'%s %s %s', '>>>>>', lab_test_report_count, lab_test_report.display_name)

            if lab_test_report.ref_id.related_patient_id.id is not False:

                related_patient = lab_test_report.ref_id.related_patient_id
                ref_id = related_patient._name + ',' + str(related_patient.id)
                lab_test_report.ref_id = ref_id

                _logger.info(u'%s %s', '>>>>>>>>>>', lab_test_report.ref_id.name)

        return True
