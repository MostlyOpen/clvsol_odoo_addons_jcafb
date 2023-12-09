# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Patient (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Patient Module customizations for CLVhealth-JCAFB Solution.',
    'version': '15.0.6.2',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_base_jcafb',
        'clv_patient',
        'clv_document',
        'clv_event',
        'clv_lab_test',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/patient_seq.xml',
        'data/document.xml',
        'data/event_attendee.xml',
        'data/lab_test.xml',
        'data/set_element.xml',
        'views/patient_code_view.xml',
        'views/document_view.xml',
        'views/event_attendee_view.xml',
        'views/lab_test_view.xml',
        'wizard/patient_associate_to_set_view.xml',
        'wizard/patient_document_setup_view.xml',
        'wizard/patient_document_setup_2_view.xml',
        'wizard/patient_lab_test_result_setup_2_view.xml',
        'wizard/event_attendee_patient_mass_edit_view.xml',
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
