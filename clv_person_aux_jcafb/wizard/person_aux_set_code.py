# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PersonAuxSetCode(models.TransientModel):
    _description = 'Person (Aux) Set Code'
    _name = 'clv.person_aux.set_code'

    def _default_personaux_ids(self):
        return self._context.get('active_ids')
    person_aux_ids = fields.Many2many(
        comodel_name='clv.person_aux',
        relation='clv_person_aux_set_code_rel',
        string='Persons (Aux)',
        default=_default_personaux_ids
    )

    person_aux_verification_exec = fields.Boolean(
        string='Person (Aux) Verification Execute',
        default=True,
    )

    def do_person_aux_set_code(self):
        self.ensure_one()

        for person_aux in self.person_aux_ids:

            _logger.info(u'%s %s', '>>>>>', person_aux.name)

            person_aux._person_aux_set_code()

            if self.person_aux_verification_exec:
                person_aux._person_aux_verification_exec()

        return True
