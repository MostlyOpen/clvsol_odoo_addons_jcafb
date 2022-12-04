# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Lab Test Code Pool (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Lab Test Code Pool Module customizations for CLVhealth-JCAFB Solution.',
    'version': '15.0.6.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_lab_test_jcafb',
        'clv_pool',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/lab_test_request_code_pool_view.xml',
        'views/lab_test_request_code_pool_item_view.xml',
        'views/lab_test_result_code_pool_view.xml',
        'views/lab_test_result_code_pool_item_view.xml',
        'views/pool_menu_view.xml',
        'wizard/lab_test_request_code_pool_item_setup_view.xml',
        'wizard/lab_test_request_code_pool_item_seek_view.xml',
        'wizard/lab_test_result_code_pool_item_setup_view.xml',
        'wizard/lab_test_result_code_pool_item_seek_view.xml',
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
