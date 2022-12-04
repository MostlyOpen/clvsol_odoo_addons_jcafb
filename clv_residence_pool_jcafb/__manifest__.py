# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Residence Code Pool (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Residence Code Pool Module customizations for CLVhealth-JCAFB Solution.',
    'version': '15.0.6.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_residence_jcafb',
        'clv_pool',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/residence_code_pool_view.xml',
        'views/residence_code_pool_item_view.xml',
        'views/pool_menu_view.xml',
        'wizard/residence_code_pool_item_setup_view.xml',
        'wizard/residence_code_pool_item_seek_view.xml',
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
