# -*- coding: utf-8 -*-
# Copyright (C) Quocent Pvt. Ltd.
# All Rights Reserved
{
    'name': "Action Button In RO Navigate To Linked PO",
    'version': "16.0.0.0",
    'summary': "Quocent Inventory Customization for Purchase Order.",
    'description': "This module is use to customize Inventory to navigate Purchase order",
    'website': "https://www.quocent.com",
    'license': 'LGPL-3',
    'author': "Quocent Pvt. Ltd.",
    'category': "Inventory",
    'depends': ["base","stock","purchase"],
    'data': [
        "views/qcent_inventory_customization_purchase_order.xml",
        ],
    'images': [
            'static/description/banner.png',
        ],
    'installable': True,
}

