# -*- coding: utf-8 -*-
# Copyright 2017 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "MIS Builder Budget",
    "summary": """
        Create budgets for MIS reports""",
    "version": "10.0.3.5.0",
    "license": "AGPL-3",
    "author": "ACSONE SA/NV, " "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/mis-builder/",
    "depends": ["mis_builder", "account"],
    "data": [
        "views/mis_report_instance_period.xml",
        "views/mis_report.xml",
        "security/mis_budget_item.xml",
        "views/mis_budget_item.xml",
        "security/mis_budget.xml",
        "views/mis_budget.xml",
        "security/mis_budget_by_account_item.xml",
        "views/mis_budget_by_account_item.xml",
        "security/mis_budget_by_account.xml",
        "views/mis_budget_by_account.xml",
    ],
    "installable": False,
    "development_status": "Production/Stable",
    "maintainers": ["sbidoul"],
}
