# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class LabTestReportCodePoolSetUp(models.TransientModel):
    _description = 'Lab Test Report Code Pool Setup'
    _name = 'clv.lab_test.report.code_pool.item_setup'

    def _default_lab_test_report_code_pool_ids(self):
        return self._context.get('active_ids')
    lab_test_report_code_pool_ids = fields.Many2many(
        comodel_name='clv.lab_test.report.code_pool',
        relation='clv_lab_test_report_code_pool_item_setup_rel',
        string='Lab Test Report Code Pools',
        default=_default_lab_test_report_code_pool_ids
    )
    code_quantity = fields.Integer(
        string='Code Quantity',
        help="Quantity of Codes",
    )

    def do_lab_test_report_code_pool_item_setup(self):
        self.ensure_one()

        LabTestReportCodePoolItem = self.env['clv.lab_test.report.code_pool.item']

        for lab_test_report_code_pool in self.lab_test_report_code_pool_ids:

            _logger.info(u'%s %s (%s)', '>>>>>', lab_test_report_code_pool.name, self.code_quantity)

            count = 0
            while count < self.code_quantity:
                count += 1

                values = {
                    'lab_test_report_code_pool_id': lab_test_report_code_pool.id,
                    'code_sequence': lab_test_report_code_pool.code_sequence,
                }
                lab_test_report_code_pool_item = LabTestReportCodePoolItem.create(values)
                # lab_test_report_code_pool_item.code = '/'

                _logger.info(u'%s %s', '>>>>>>>>>>', lab_test_report_code_pool_item.code)

        return True
