# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PatientCodePoolSetUp(models.TransientModel):
    _description = 'Patient Code Pool Setup'
    _name = 'clv.patient.code_pool_setup'

    def _default_pool_instance_ids(self):
        return self._context.get('active_ids')
    pool_instance_ids = fields.Many2many(
        comodel_name='clv.pool.instance',
        relation='clv_patient_instance_patient_code_pool_setup_rel',
        string='Pool Instances',
        default=_default_pool_instance_ids
    )
    quantity = fields.Integer(
        string='Quantity',
        help="Quantity of Codes",
    )

    def do_patient_code_pool_setup(self):
        self.ensure_one()

        PatientCodePool = self.env['clv.patient.code_pool']

        for pool_instance in self.pool_instance_ids:

            _logger.info(u'%s %s (%s)', '>>>>>', pool_instance.name, self.quantity)

            count = 0
            while count < self.quantity:
                count += 1

                values = {
                    'pool_instance_id': pool_instance.id,
                }
                patient_code_pool = PatientCodePool.create(values)
                patient_code_pool.code = '/'

                _logger.info(u'%s %s', '>>>>>>>>>>', patient_code_pool.code)

        return True
