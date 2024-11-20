from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrderNoteSectionWizard(models.TransientModel):
    _name = 'sale.order.note.section.wizard'
    _description = 'Wizard to update Sale Order Sections and Notes'

    sale_order_id = fields.Many2one('sale.order', string='Sale Order', required=True)
    line_ids = fields.One2many('sale.order.note.section.wizard.line', 'wizard_id', string='Order Lines')

    @api.model
    def default_get(self, fields):
        res = super(SaleOrderNoteSectionWizard, self).default_get(fields)

        sale_order_id = self._context.get('sale_order_id')
        sale_order = self.env['sale.order'].browse(sale_order_id)

        print(f"Sale Order: {sale_order}")

        # Filter lines for section and note types
        lines = sale_order.order_line.filtered(lambda l: l.display_type in ['line_section', 'line_note'])

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
            'sale_order_id': sale_order.id,
            'line_ids': line_vals,
        })

        print(f"Resulting line_vals: {line_vals}")

        return res

    def action_update(self):
        print("Initiated update process")
        sale_order = self.sale_order_id
        # Call the existing unlock method
        if sale_order.state not in ['draft', 'sent']:
            sale_order.sudo().action_unlock()  # function already present in bass
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

        sale_order.sudo().action_lock()  # already present in base code
        print("Order relocked using action_lock method")

    class SaleOrderNoteSectionWizardLine(models.TransientModel):
        _name = 'sale.order.note.section.wizard.line'
        _description = 'Order Lines for Updating Section and Notes in Wizard'

        wizard_id = fields.Many2one('sale.order.note.section.wizard', string='Wizard')
        order_line_id = fields.Many2one('sale.order.line', string='Order Line',required=True)
        display_type = fields.Selection(related='order_line_id.display_type', string='Type')
        name = fields.Char(string='Existing')
        update = fields.Char(string='Update')




