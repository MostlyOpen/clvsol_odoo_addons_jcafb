# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class DocumentAssociateToRelatedPatient(models.TransientModel):
    _description = 'Document Associate to Related Patient'
    _name = 'clv.document.associate_to_related_patient'

    def _default_document_ids(self):
        return self._context.get('active_ids')
    document_ids = fields.Many2many(
        comodel_name='clv.document',
        relation='clv_document_associate_to_related_patient_rel',
        string='Documents',
        default=_default_document_ids
    )

    def do_document_associate_to_related_patient(self):
        self.ensure_one()

        document_count = 0
        for document in self.document_ids:

            document_count += 1

            _logger.info(u'%s %s %s', '>>>>>', document_count, document.display_name)

            if document.ref_id.related_patient_id.id is not False:

                related_patient = document.ref_id.related_patient_id
                ref_id = related_patient._name + ',' + str(related_patient.id)
                document.ref_id = ref_id

                _logger.info(u'%s %s', '>>>>>>>>>>', document.ref_id.name)

        return True
