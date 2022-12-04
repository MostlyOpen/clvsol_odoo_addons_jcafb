# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class DocumentCodePoolSetUp(models.TransientModel):
    _description = 'Document Code Pool Setup'
    _name = 'clv.document.code_pool.item_setup'

    def _default_document_code_pool_ids(self):
        return self._context.get('active_ids')
    document_code_pool_ids = fields.Many2many(
        comodel_name='clv.document.code_pool',
        relation='clv_document_code_pool_document_code_pool_item_setup_rel',
        string='Document Code Pools',
        default=_default_document_code_pool_ids
    )
    code_quantity = fields.Integer(
        string='Code Quantity',
        help="Quantity of Codes",
    )

    def do_document_code_pool_item_setup(self):
        self.ensure_one()

        DocumentCodePoolItem = self.env['clv.document.code_pool.item']

        for document_code_pool in self.document_code_pool_ids:

            _logger.info(u'%s %s (%s)', '>>>>>', document_code_pool.name, self.code_quantity)

            count = 0
            while count < self.code_quantity:
                count += 1

                values = {
                    'document_code_pool_id': document_code_pool.id,
                    'code_sequence': document_code_pool.code_sequence,
                }
                document_code_pool_item = DocumentCodePoolItem.create(values)
                # document_code_pool_item.code = '/'

                _logger.info(u'%s %s', '>>>>>>>>>>', document_code_pool_item.code)

        return True
