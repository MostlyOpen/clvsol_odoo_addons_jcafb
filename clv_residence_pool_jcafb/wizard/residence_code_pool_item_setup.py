# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResidenceCodePoolSetUp(models.TransientModel):
    _description = 'Residence Code Pool Setup'
    _name = 'clv.residence.code_pool.item_setup'

    def _default_residence_code_pool_ids(self):
        return self._context.get('active_ids')
    residence_code_pool_ids = fields.Many2many(
        comodel_name='clv.residence.code_pool',
        relation='clv_residence_code_pool_residence_code_pool_item_setup_rel',
        string='Residence Code Pools',
        default=_default_residence_code_pool_ids
    )
    code_quantity = fields.Integer(
        string='Code Quantity',
        help="Quantity of Codes",
    )

    def do_residence_code_pool_item_setup(self):
        self.ensure_one()

        ResidenceCodePoolItem = self.env['clv.residence.code_pool.item']

        for residence_code_pool in self.residence_code_pool_ids:

            _logger.info(u'%s %s (%s)', '>>>>>', residence_code_pool.name, self.code_quantity)

            count = 0
            while count < self.code_quantity:
                count += 1

                values = {
                    'residence_code_pool_id': residence_code_pool.id,
                    'code_sequence': residence_code_pool.code_sequence,
                }
                residence_code_pool_item = ResidenceCodePoolItem.create(values)
                # residence_code_pool_item.code = '/'

                _logger.info(u'%s %s', '>>>>>>>>>>', residence_code_pool_item.code)

        return True
