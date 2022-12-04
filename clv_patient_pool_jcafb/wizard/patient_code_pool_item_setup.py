# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PatientCodePoolSetUp(models.TransientModel):
    _description = 'Patient Code Pool Setup'
    _name = 'clv.patient.code_pool.item_setup'

    def _default_patient_code_pool_ids(self):
        return self._context.get('active_ids')
    patient_code_pool_ids = fields.Many2many(
        comodel_name='clv.patient.code_pool',
        relation='clv_patient_code_pool_patient_code_pool_item_setup_rel',
        string='Patient Code Pools',
        default=_default_patient_code_pool_ids
    )
    code_quantity = fields.Integer(
        string='Code Quantity',
        help="Quantity of Codes",
    )

    def do_patient_code_pool_item_setup(self):
        self.ensure_one()

        PatientCodePoolItem = self.env['clv.patient.code_pool.item']

        for patient_code_pool in self.patient_code_pool_ids:

            _logger.info(u'%s %s (%s)', '>>>>>', patient_code_pool.name, self.code_quantity)

            count = 0
            while count < self.code_quantity:
                count += 1

                values = {
                    'patient_code_pool_id': patient_code_pool.id,
                    'code_sequence': patient_code_pool.code_sequence,
                }
                patient_code_pool_item = PatientCodePoolItem.create(values)
                # patient_code_pool_item.code = '/'

                _logger.info(u'%s %s', '>>>>>>>>>>', patient_code_pool_item.code)

        return True
