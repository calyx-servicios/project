from odoo import models, fields, api, _
import datetime

class ProjectProject(models.Model):
    _inherit = "project.project"


    def get_effective_planned_hours(self):
        planned_hours = 0.0
        effective_hours = 0.0
        total_planned_hours = ""
        total_effective_hours = ""
        if self.task_ids: 
            for task in self.task_ids:
                planned_hours = planned_hours + task.planned_hours
                effective_hours = effective_hours + task.effective_hours
        hour, minute = divmod(planned_hours, 1)
        total_planned_hours = "{}:{}".format(int(hour), int(minute*60))
        hour, minute = divmod(effective_hours, 1)
        total_effective_hours = "{}:{}".format(int(hour), int(minute*60))
        self.effective_planned_hours = (total_planned_hours + "/" + total_effective_hours)

    def get_total_balance(self):
        total_balance = 0.0
        if self.extra_accounts: 
            for account in self.extra_accounts:
                total_balance += account.balance
        self.total_balance = total_balance


    extra_accounts = fields.One2many("project.project.lines",
    "extra_account_ids", string="related analytics accounts")
    effective_planned_hours = fields.Char(compute="get_effective_planned_hours")
    total_balance = fields.Monetary(compute="get_total_balance")

    @api.onchange("analytic_account_id")
    def onchange_analytic_account_id(self):
        if self.analytic_account_id:
            self.extra_accounts = [(0,0,{"accounts_id":self.analytic_account_id.id})]