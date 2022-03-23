# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Family (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Family Module customizations for CLVhealth-JCAFB Solution.',
    'version': '15.0.6.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_family',
        'clv_document',
        'clv_base_jcafb',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/family_seq.xml',
        'data/document.xml',
        'data/default_value.xml',
        'views/document_view.xml',
        'views/family_code_view.xml',
        'wizard/family_document_setup_view.xml',
    ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'application': False,
    'active': False,
    'css': [],
}
