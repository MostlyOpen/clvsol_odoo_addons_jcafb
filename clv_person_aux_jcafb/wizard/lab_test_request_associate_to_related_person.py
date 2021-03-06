# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class LabTestRequestAssociateToRelatedPerson(models.TransientModel):
    _description = 'Lab Test Request Associate to Related Person'
    _name = 'clv.lab_test.request.associate_to_related_person'

    def _default_lab_test_request_ids(self):
        return self._context.get('active_ids')
    lab_test_request_ids = fields.Many2many(
        comodel_name='clv.lab_test.request',
        relation='clv_lab_test_request_associate_to_related_person_rel',
        string='Lab Test Requests',
        default=_default_lab_test_request_ids
    )

    def do_lab_test_request_associate_to_related_person(self):
        self.ensure_one()

        lab_test_request_count = 0
        for lab_test_request in self.lab_test_request_ids:

            lab_test_request_count += 1

            _logger.info(u'%s %s %s', '>>>>>', lab_test_request_count, lab_test_request.display_name)

            if lab_test_request.ref_id.related_person_id.id is not False:

                related_person = lab_test_request.ref_id.related_person_id
                ref_id = related_person._name + ',' + str(related_person.id)
                lab_test_request.ref_id = ref_id

                _logger.info(u'%s %s', '>>>>>>>>>>', lab_test_request.ref_id.name)

        return True
