# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class LabTestRequestCodePoolSeek(models.TransientModel):
    _description = 'Lab Test Request Code Pool Seek'
    _name = 'clv.lab_test.request.code_pool.item_seek'

    def _default_lab_test_request_code_pool_ids(self):
        return self._context.get('active_ids')
    lab_test_request_code_pool_ids = fields.Many2many(
        comodel_name='clv.lab_test.request.code_pool',
        relation='clv_lab_test_request_code_pool_item_seek_rel',
        string='Lab Test Request Code Pools',
        default=_default_lab_test_request_code_pool_ids
    )

    def do_lab_test_request_code_pool_item_seek(self):
        self.ensure_one()

        LabTestRequestCodePoolItem = self.env['clv.lab_test.request.code_pool.item']
        LabTestRequest = self.env['clv.lab_test.request']

        for lab_test_request_code_pool in self.lab_test_request_code_pool_ids:

            _logger.info(u'%s %s', '>>>>>', lab_test_request_code_pool.name)

            search_domain = [
                ('lab_test_request_code_pool_id', '=', lab_test_request_code_pool.id),
            ]
            items = LabTestRequestCodePoolItem.search(search_domain)

            for item in items:

                if (item.lab_test_request_id is not False):

                    item.lab_test_request_id = False

            for item in items:

                lab_test_requests = LabTestRequest.search([])

                for lab_test_request in lab_test_requests:

                    if (lab_test_request.code == item.code):

                        item.lab_test_request_id = lab_test_request.id

        return True
