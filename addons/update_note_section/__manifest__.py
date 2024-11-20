{
    'name': 'Update Note and Section',
     'summary': """
       Update Note and Section in Locked stage
      """,
    "version": "17.0.1.0.0",
    "depends": ["sale_management"],
"data": [
    'security/ir.model.access.csv',
    'security/security.xml',
    'data/server_action.xml',
    'wizard/note_wizard_sales.xml',
    'wizard/note_wizard_purchase.xml',
    'wizard/note_wizard_invoice.xml',
        ],
    "author": "Quocent Pvt. Ltd.",
    "website": "https://quocent.com",
    'installable': True,
    'application': True,
    "license": "LGPL-3",
    'images': ['static/description/banner.png'],
}