# -*- coding: utf-8 -*-
# Copyright (C) Quocent Pvt. Ltd.
# All Rights Reserved

from odoo import models, fields

class UpdateMassProductCategory(models.TransientModel):
    _name = 'update.mass.product.category'
    _description = 'Update Mass Product Category'

    product_category_id = fields.Many2one("product.category", string="Product Category")

    def cancel(self):
        return {'type': 'ir.actions.act_window_close'}

    def apply(self):
        active_ids = self.env.context.get('active_ids', [])

        if active_ids:
            products = self.env['product.template'].browse(active_ids)
            products.write({'categ_id': self.product_category_id.id})
