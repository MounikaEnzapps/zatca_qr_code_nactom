# -*- coding: utf-8 -*-
{
    'name': "NATCOM New",
    'author':
        'Enzapps',
    'summary': """
This module is for creating api for Invoices.
""",

    'description': """
        This module consist of track page of cargo which extend the website.
        It consist of 2 tabs Brief and History
    """,
    'website': "",
    'category': 'base',
    'version': '14.0',
    'depends': ['sale','purchase','base','account','account_invoice_ubl','natcom_pdf_new'],
    "images": ['static/description/icon.png'],
    'data': [
              'views/account.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
}
