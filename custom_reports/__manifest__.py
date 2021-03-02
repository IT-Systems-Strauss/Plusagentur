# -*- coding: utf-8 -*-
{
    'name': "custom_reports",

    'summary': """
        Sammlung von Report Customizations""",

    'description': """
        Report Customizations in a  Module
    """,

    'author': "Plusagentur",
    'website': "https://plusagentur.de",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1.4',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/sale.report_saleorder_its_custom_document.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
