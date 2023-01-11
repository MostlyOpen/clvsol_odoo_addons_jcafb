# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class LabTestReportCodePoolSeek(models.TransientModel):
    _description = 'Lab Test Report Code Pool Seek'
    _name = 'clv.lab_test.report.code_pool.item_seek'

    def _default_lab_test_report_code_pool_ids(self):
        return self._context.get('active_ids')
    lab_test_report_code_pool_ids = fields.Many2many(
        comodel_name='clv.lab_test.report.code_pool',
        relation='clv_lab_test_report_code_pool_item_seek_rel',
        string='Lab Test Report Code Pools',
        default=_default_lab_test_report_code_pool_ids
    )

    def do_lab_test_report_code_pool_item_seek(self):
        self.ensure_one()

        LabTestReportCodePoolItem = self.env['clv.lab_test.report.code_pool.item']
        LabTestReport = self.env['clv.lab_test.report']

        for lab_test_report_code_pool in self.lab_test_report_code_pool_ids:

            _logger.info(u'%s %s', '>>>>>', lab_test_report_code_pool.name)

            search_domain = [
                ('lab_test_report_code_pool_id', '=', lab_test_report_code_pool.id),
            ]
            items = LabTestReportCodePoolItem.search(search_domain)

            for item in items:

                if (item.lab_test_report_id is not False):

                    item.lab_test_report_id = False

            for item in items:

                lab_test_reports = LabTestReport.search([])

                for lab_test_report in lab_test_reports:

                    if (lab_test_report.code == item.code):

                        item.lab_test_report_id = lab_test_report.id

        return True
