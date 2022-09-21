{
    'name':'Odoo Academy',
    'summary':"""Acdemy app to manage training""",
    'description':"""Academy Module to manage Training.
    .Courses
    .sessions
    .attendees
    """,
    'author':'Odoo',
    'website': 'https://www.odoo.com',
    'category': '0.1',
    'depends': ['base'],
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
    ],
    'license': 'OPL-1',
    'demo':[
        'demo/academy_demo.xml',        
    ],
}