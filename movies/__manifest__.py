# -*- coding: utf-8 -*-
{
    'name': "Movie Record",

    'summary': """
        Manage and store movie details efficiently.""",

    'description': """
        This module allows users to manage and store comprehensive details about movies.
    """,

    'author': "Company",
    'website': "https://www.company.com",
    'category': 'Record',
    'version': '16.0.1.0.0',
    'application': 'true',
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
