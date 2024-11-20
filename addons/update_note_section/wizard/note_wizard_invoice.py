from odoo import models, fields, api
from odoo.exceptions import ValidationError


class InvoiceNoteSectionWizard(models.TransientModel):
    _name = 'invoice.note.section.wizard'
    _description = 'Wizard to update Invoice Sections and Notes'

    invoice_id = fields.Many2one('account.move', string='Invoice', required=True)
    line_ids = fields.One2many('invoice.note.section.wizard.line', 'wizard_id', string='Order Lines')

    @api.model
    def default_get(self, fields):
        res = super(InvoiceNoteSectionWizard, self).default_get(fields)

        invoice_id = self._context.get('invoice_id')
        invoice = self.env['account.move'].browse(invoice_id)

        print(f"Invoice: {invoice}")

        # Filter lines for section and note types
        lines = invoice.invoice_line_ids.filtered(lambda l: l.display_type in ['line_section', 'line_note'])

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
            'invoice_id': invoice.id,
            'line_ids': line_vals,
        })

        print(f"Resulting line_vals: {line_vals}")

        return res

    def action_update(self):
        print("Initiated update process")
        invoice = self.invoice_id
        # Call the existing unlock method
        if invoice.state not in 'draft':
            invoice.sudo().button_draft()  # function already present in bass
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

        invoice.sudo().action_post()  # already present in base code
        print("Order relocked using action_lock method")


class InvoiceNoteSectionWizardLine(models.TransientModel):
    _name = 'invoice.note.section.wizard.line'
    _description = 'Order Lines for Updating Section and Notes in Wizard'

    wizard_id = fields.Many2one('invoice.note.section.wizard', string='Wizard')
    order_line_id = fields.Many2one('account.move.line', string='Order Line', required=True)
    display_type = fields.Selection(related='order_line_id.display_type', string='Type')
    name = fields.Char(string='Existing')
    update = fields.Char(string='Update')