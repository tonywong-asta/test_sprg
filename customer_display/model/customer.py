from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    customer_name = fields.Char(String="Customer Name", compute='display_customer')

    def display_customer(self):
        for rec in self:
            res = self.env['sale.order'].search([('name', '=', rec.origin)])
            if res:
                rec.customer_name = res.partner_id.name
            else:
                rec.customer_name = " "

