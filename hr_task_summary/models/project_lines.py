from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProjectProjectLines(models.Model):
    _name = "project.project.lines"


    accounts_id = fields.Many2one("account.analytic.account", string="Analytic Account")
    display_name = fields.Char("Name", related="accounts_id.display_name")
    code = fields.Char("Reference", related="accounts_id.code")
    balance = fields.Monetary(related="accounts_id.balance", string="Balance")
    debit = fields.Monetary(related="accounts_id.debit", string="Debit")
    credit = fields.Monetary(related="accounts_id.credit", string="Credit")
    currency_id = fields.Many2one(related="accounts_id.currency_id", string="Currency")
    company_id = fields.Many2one(related="accounts_id.company_id", string="Company")
    partner_id = fields.Many2one(related="accounts_id.partner_id", string="Customer")
    project_id = fields.Integer(related="extra_account_ids.project_ids.id", string="Project")
    extra_account_ids = fields.Many2one("project.project", string="Account")
    
    @api.multi
    @api.constrains("accounts_id")
    def _check_extra_accounts(self):
        self_ids = self.search(
            ["&",("project_id", "=", self.project_id), ("accounts_id.id", "=", self.accounts_id.id), ])
        if len(self_ids) != 1:
            raise ValidationError(_("A project cannot have two identical analytic accounts"))
