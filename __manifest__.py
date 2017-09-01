# -*- coding: utf-8 -*-
{
    'name': "web_data_extraction",

    'summary': """
        used to extract structural data from website""",

    'description': """
        used to extract structural data from website and these data can be used in
        other apps of odoo
    """,

    'author': "Kang Li",
    'website': "http://www.chunyutech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Marketing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "installable":True,
    "application":True,
    'qweb': [
        'static/src/xml/web_data_extraction.xml',
      ],
}