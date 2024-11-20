# -*- coding: utf-8 -*-
# Part of Quocent. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class Inventory(models.Model):
    _inherit = 'stock.picking'

    purchase_id = fields.Many2one('purchase.order', string="Purchase Order")
    purchase_count = fields.Integer("Purchase count", compute='_compute_purchase_count')

    #this button method is used to redirect purchase order from receipt order.
    def action_inventory_purchase_order(self):
        if self.purchase_id:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Purchase Order',
                'view_mode': 'form',
                'res_model': 'purchase.order',
                'res_id': self.purchase_id.id,
                'target': 'current',
            }

    #this method is used to count the purchase order.



    def _compute_purchase_count(self):
        for purchase in self:
            purchase.purchase_count = 1 if purchase.purchase_id else 0
