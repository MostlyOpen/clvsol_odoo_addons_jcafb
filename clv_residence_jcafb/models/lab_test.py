# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Residence(models.Model):
    _inherit = 'clv.residence'

    lab_test_request_ids = fields.One2many(
        string='Lab Test Requests',
        comodel_name='clv.lab_test.request',
        compute='_compute_lab_test_request_ids_and_count',
    )
    count_lab_test_requests = fields.Integer(
        string='Lab Test Requests (count)',
        compute='_compute_lab_test_request_ids_and_count',
    )
    count_lab_test_requests_2 = fields.Integer(
        string='Lab Test Requests 2 (count)',
        compute='_compute_lab_test_request_ids_and_count',
    )

    def _compute_lab_test_request_ids_and_count(self):
        for record in self:

            # search_domain = [
            #     ('ref_id', '=', self._name + ',' + str(record.id)),
            # ]
            search_domain = [
                ('ref_name', '=', record.name),
                ('ref_code', '=', record.code),
            ]
            lab_test_requests_2 = self.env['clv.lab_test.request'].search(search_domain)

            if record.phase_id.id is not False:
                search_domain.append(
                    ('phase_id.id', '=', record.phase_id.id),
                )
            lab_test_requests = self.env['clv.lab_test.request'].search(search_domain)

            record.count_lab_test_requests = len(lab_test_requests)
            record.count_lab_test_requests_2 = len(lab_test_requests_2)
            record.lab_test_request_ids = [(6, 0, lab_test_requests.ids)]

    lab_test_result_ids = fields.One2many(
        string='Lab Test Results',
        comodel_name='clv.lab_test.result',
        compute='_compute_lab_test_result_ids_and_count',
    )
    count_lab_test_results = fields.Integer(
        string='Lab Test Results (count)',
        compute='_compute_lab_test_result_ids_and_count',
    )
    count_lab_test_results_2 = fields.Integer(
        string='Lab Test Results 2 (count)',
        compute='_compute_lab_test_result_ids_and_count',
    )

    def _compute_lab_test_result_ids_and_count(self):
        for record in self:

            # search_domain = [
            #     ('ref_id', '=', self._name + ',' + str(record.id)),
            # ]
            search_domain = [
                ('ref_name', '=', record.name),
                ('ref_code', '=', record.code),
            ]
            lab_test_results_2 = self.env['clv.lab_test.result'].search(search_domain)

            if record.phase_id.id is not False:
                search_domain.append(
                    ('phase_id.id', '=', record.phase_id.id),
                )
            lab_test_results = self.env['clv.lab_test.result'].search(search_domain)

            record.count_lab_test_results = len(lab_test_results)
            record.count_lab_test_results_2 = len(lab_test_results_2)
            record.lab_test_result_ids = [(6, 0, lab_test_results.ids)]

    lab_test_report_ids = fields.One2many(
        string='Lab Test Reports',
        comodel_name='clv.lab_test.report',
        compute='_compute_lab_test_report_ids_and_count',
    )
    count_lab_test_reports = fields.Integer(
        string='Lab Test Reports (count)',
        compute='_compute_lab_test_report_ids_and_count',
    )
    count_lab_test_reports_2 = fields.Integer(
        string='Lab Test Reports 2 (count)',
        compute='_compute_lab_test_report_ids_and_count',
    )

    def _compute_lab_test_report_ids_and_count(self):
        for record in self:

            # search_domain = [
            #     ('ref_id', '=', self._name + ',' + str(record.id)),
            # ]
            search_domain = [
                ('ref_name', '=', record.name),
                ('ref_code', '=', record.code),
            ]
            lab_test_reports_2 = self.env['clv.lab_test.report'].search(search_domain)

            if record.phase_id.id is not False:
                search_domain.append(
                    ('phase_id.id', '=', record.phase_id.id),
                )
            lab_test_reports = self.env['clv.lab_test.report'].search(search_domain)

            record.count_lab_test_reports = len(lab_test_reports)
            record.count_lab_test_reports_2 = len(lab_test_reports_2)
            record.lab_test_report_ids = [(6, 0, lab_test_reports.ids)]
