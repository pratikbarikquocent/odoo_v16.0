# -*- coding: utf-8 -*-
# Copyright (C) Quocent Pvt. Ltd.
# All Rights Reserved

from odoo import models, fields

class ProductVendorTaxUpdateWizard(models.TransientModel):
    _name = 'product.vendor.tax.update.wizard'
    _description = 'Bulk Product Vendor Tax Update Wizard'

    tax_operation = fields.Selection(
        [("update_taxes", "Update Taxes"),("replace_taxes", "Replace Taxes"),]
        , string="Operation",default='update_taxes'
    )
    supplier_taxes_id = fields.Many2many('account.tax',string='Vendor Tax')

    def apply(self):
        product_ids = self.env['product.template'].browse(self.env.context.get('active_ids', []))

        for product in product_ids:
            if self.tax_operation == "update_taxes":
                product.supplier_taxes_id = [(4, tax.id) for tax in self.supplier_taxes_id]
            elif self.tax_operation == "replace_taxes":
                product.supplier_taxes_id = [(6, 0, self.supplier_taxes_id.ids)]

    def cancel(self):
        return {'type': 'ir.actions.act_window_close'}
