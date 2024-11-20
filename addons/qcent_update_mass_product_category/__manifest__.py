# -*- coding: utf-8 -*-
# Copyright (C) Quocent Pvt. Ltd.
# All Rights Reserved
{
    "name": "Product Category Mass Update",
    "version": "16.0.1.0.0",
    "summary": "This app enables efficient bulk updates and replacements of product categories in Odoo. It simplifies managing and modifying categories for multiple products at once.",
    "category": "Update Tool",
    "license": "LGPL-3",
    "author": "Quocent Pvt. Ltd.",
    "website": "https://www.quocent.com",
    "description": "This app facilitates the bulk update and replacement of product categories in Odoo, allowing users to efficiently manage large numbers of products.",
    "depends": ["base","stock"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "wizard/update_mass_product_catagory_wizard.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
    "installable": True,
}
