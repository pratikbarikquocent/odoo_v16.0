# -*- coding: utf-8 -*-
# Copyright (C) Quocent Pvt. Ltd.
# All Rights Reserved

{
    "name": "Bulk Product Vendor Taxes Updates",
    "version": "16.0.1.0.0",
    "summary": "This app enables efficient bulk updates and replacements of product vendor taxes in Odoo.",
    "category": "Update Tool",
    "license": "LGPL-3",
    "author": "Quocent Pvt. Ltd.",
    "website": "https://www.quocent.com",
    "description": "This module provides efficient tool to update vendor taxes for multiple products in bulk within Odoo. It simplifies tax management for businesses by allowing users to modify the vendor tax configurations of multiple products.",
    "depends": ["base","stock","account"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        'wizards/bulk_product_vendor_tax_update_wizard.xml',
    ],
    "images": [
        "static/description/banner.png",
    ],
    "installable": True,
}

