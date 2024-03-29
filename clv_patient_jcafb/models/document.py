# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Patient(models.Model):
    _inherit = 'clv.patient'

    document_ids = fields.One2many(
        string='Documents',
        comodel_name='clv.document',
        compute='_compute_document_ids_and_count',
    )
    count_documents = fields.Integer(
        string='Documents (count)',
        compute='_compute_document_ids_and_count',
    )
    count_documents_2 = fields.Integer(
        string='Documents 2 (count)',
        compute='_compute_document_ids_and_count',
    )

    def _compute_document_ids_and_count(self):
        for record in self:

            # search_domain = [
            #     ('ref_id', '=', self._name + ',' + str(record.id)),
            # ]
            search_domain = [
                # ('ref_name', '=', record.name),
                ('ref_code', '=', record.code),
            ]
            documents_2 = self.env['clv.document'].search(search_domain)

            if record.phase_id.id is not False:
                search_domain.append(
                    ('phase_id.id', '=', record.phase_id.id),
                )
            documents = self.env['clv.document'].search(search_domain)

            record.count_documents = len(documents)
            record.count_documents_2 = len(documents_2)
            record.document_ids = [(6, 0, documents.ids)]
