from odoo import models, fields, api
from odoo.exceptions import ValidationError


class PurchaseOrderNoteSectionWizard(models.TransientModel):
    _name = 'purchase.order.note.section.wizard'
    _description = 'Wizard to update Purchase Order Sections and Notes'

    purchase_order_id = fields.Many2one('purchase.order', string='Purchase Order', required=True)
    line_ids = fields.One2many('purchase.order.note.section.wizard.line', 'wizard_id', string='Order Lines')

    @api.model
    def default_get(self, fields):
        res = super(PurchaseOrderNoteSectionWizard, self).default_get(fields)

        purchase_order_id = self._context.get('purchase_order_id')
        purchase_order = self.env['purchase.order'].browse(purchase_order_id)

        print(f"Purchase Order: {purchase_order}")

        # Filter lines for section and note types
        lines = purchase_order.order_line.filtered(lambda l: l.display_type in ['line_section', 'line_note'])

        # Debug to see filtered lines
        print(f"Filtered Lines: {lines}")

        line_vals = []
        for line in lines:
            print(f"Processing line: {line.id}, display_type: {line.display_type}, name: {line.name}")
            line_vals.append((0, 0, {
                'order_line_id': line.id,
                'display_type': line.display_type,
                'name': line.name,
            }))
        res.update({
            'purchase_order_id': purchase_order.id,
            'line_ids': line_vals,
        })

        print(f"Resulting line_vals: {line_vals}")

        return res

    def action_update(self):
        print("Initiated update process")
        purchase_order = self.purchase_order_id
        # Call the existing unlock method
        if purchase_order.state not in ['draft', 'sent']:
            purchase_order.sudo().button_unlock()  # function already present in bass
            print("Order unlocked using action_unlock method")
        try:
            for line in self.line_ids:
                print(f"Checking line with ID: {line.order_line_id.id}")
                if line.order_line_id:
                    if line.display_type == 'line_section':
                        print("Updating section")
                        line.order_line_id.sudo().write({
                            'name': line.update,
                        })
                    elif line.display_type == 'line_note':
                        print("Updating note")
                        line.order_line_id.sudo().write({
                            'name': line.update,
                        })
        except Exception as e:
            print(f"An error occurred: {e}")
            raise

        purchase_order.sudo().button_done()  # already present in base code
        print("Order relocked using action_lock method")


class PurchaseOrderNoteSectionWizardLine(models.TransientModel):
    _name = 'purchase.order.note.section.wizard.line'
    _description = 'Order Lines for Updating Section and Notes in Wizard'

    wizard_id = fields.Many2one('purchase.order.note.section.wizard', string='Wizard')
    order_line_id = fields.Many2one('purchase.order.line', string='Order Line', required=True)
    display_type = fields.Selection(related='order_line_id.display_type', string='Type')
    name = fields.Char(string='Existing')
    update = fields.Char(string='Update')
