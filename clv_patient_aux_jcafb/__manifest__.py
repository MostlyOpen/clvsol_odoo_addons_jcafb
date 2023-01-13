# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Patient (Aux) (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Patient (Aux) Module customizations for CLVhealth-JCAFB Solution.',
    'version': '15.0.6.1',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_patient_aux',
        'clv_document',
        # 'clv_community',
        'clv_event',
        'clv_lab_test',
        'clv_base_jcafb',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/document.xml',
        # 'data/community_member.xml',
        'data/event_attendee.xml',
        'data/lab_test.xml',
        'data/default_value.xml',
        'views/document_view.xml',
        # 'views/community_member_view.xml',
        'views/event_attendee_view.xml',
        'views/lab_test_view.xml',
        'views/patient_aux_code_view.xml',
        'wizard/patient_aux_event_setup_view.xml',
        'wizard/patient_aux_document_setup_view.xml',
        'wizard/patient_aux_document_setup_2_view.xml',
        # 'wizard/patient_aux_lab_test_request_setup_view.xml',
        # 'wizard/patient_aux_lab_test_request_setup_2_view.xml',
        'wizard/patient_aux_lab_test_result_setup_2_view.xml',
        'wizard/patient_aux_set_code_view.xml',
        'wizard/document_associate_to_related_patient_view.xml',
        # 'wizard/lab_test_request_associate_to_related_patient_view.xml',
        'wizard/lab_test_result_associate_to_related_patient_view.xml',
        # 'wizard/lab_test_report_associate_to_related_patient_view.xml',
        'wizard/event_attendee_associate_to_related_patient_view.xml',
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
