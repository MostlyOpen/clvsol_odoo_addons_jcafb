# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Address (Aux) (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Address (Aux) Module customizations for CLVhealth-JCAFB Solution.',
    'version': '15.0.6.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_address_aux',
        'clv_document',
        'clv_community',
        'clv_event',
        'clv_lab_test',
        'clv_base_jcafb',
    ],
    'data': [
        'data/document.xml',
        'data/community_member.xml',
        'data/event_attendee.xml',
        'data/lab_test.xml',
        'data/default_value.xml',
        'views/document_view.xml',
        'views/community_member_view.xml',
        'views/event_attendee_view.xml',
        'views/lab_test_view.xml',
        'views/address_aux_code_view.xml',
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
