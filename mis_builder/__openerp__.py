# -*- coding: utf-8 -*-
##############################################################################
#
#    mis_builder module for Odoo, Management Information System Builder
#    Copyright (C) 2014-2015 ACSONE SA/NV (<http://acsone.eu>)
#
#    This file is a part of mis_builder
#
#    mis_builder is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License v3 or later
#    as published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    mis_builder is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License v3 or later for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    v3 or later along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'MIS Builder',
    'version': '0.2',
    'category': 'Reporting',
    'summary': """
        Build 'Management Information System' Reports and Dashboards
    """,
    'description': """
.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
===========
MIS Builder
===========

This module allows you to build Management Information Systems dashboards.
Such style of reports presents KPI in rows and time periods in columns.
Reports mainly fetch data from account moves, but can also combine data coming
from arbitrary Odoo models. Reports can be exported to PDF, Excel and they
can be added to Odoo dashboards.

Installation
============

There is no specific installation procedure for this module.

Configuration and Usage
=======================

To configure this module, you need to:

* Go to Accounting > Configuration > Financial Reports > MIS Report Templates
where you can create report templates by defining KPI's. KPI's constitute
the rows of your reports. Such report templates are time independent.

* Then in Accounting > Reporting > MIS Reports you can create report instance
by binding the templates to time period, hence defining the columns of your
reports.

* From the MIS Report view, you can preview the report, add it to and Odoo
dashboard, and export it to Excel.

Developer notes
===============

A typical extension is to provide a mechanism to filter reports on analytic
dimensions or operational units. To implement this, you can override
_get_additional_move_line_filter and _get_additional_filter to further
filter move lines or queries based on a user selection. A typical use case
could be to add an analytic account field on mis.report.instance, or even
on mis.report.instance.period if you want different columns to show different
analytic accounts.

Known issues / Roadmap
======================

* Add 'Fiscal Year' period type.

* Allow selecting accounts by type. This is currently possible by expressing
  a query such as balp[][('account_id.user_type.code', '=', ...)].
  This will work but would be more efficient if one could write balp[
  user_type=...], as it would involve much less queries to the database.

* More tests should be added. The first part is creating test data, then it
will be easier. At the minimum, We need the following test data:

  * one account charts with a few normal accounts and view accounts,
  * two fiscal years,
  * an opening entry in the second fiscal year,
  * to test multi-company consolidation, we need a second company with it's own
    account chart and two fiscal years, but without opening entry; we also need
    a third company which is the parent of the other two and has a
    consolidation chart of account.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/account-financial-reporting/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and
welcomed feedback `here <https://github.com/OCA/account-financial-reporting
/issues/new?body=module:%20mis_builder%0Aversion:%208.0%0A%0A**Steps%20to%20
reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior
**>`_.

Credits
=======

Contributors
------------

* Stéphane Bidoul <stephane.bidoul@acsone.eu>
* Laetitia Gangloff <laetitia.gangloff@acsone.eu>
* Adrien Peiffer <adrien.peiffer@acsone.eu>
* Jordi Ballester <jordi.ballester@eficent.com>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.
    """,
    'author': 'ACSONE SA/NV,'
              'Odoo Community Association (OCA)',
    'website': 'http://acsone.eu',
    'depends': [
        'account',
        'report_xls',  # OCA/reporting-engine
    ],
    'data': [
        'wizard/mis_builder_dashboard.xml',
        'views/mis_builder.xml',
        'security/ir.model.access.csv',
        'security/mis_builder_security.xml',
    ],
    'test': [
    ],
    'demo': [
        'tests/mis.report.kpi.csv',
        'tests/mis.report.query.csv',
        'tests/mis.report.csv',
        'tests/mis.report.instance.period.csv',
        'tests/mis.report.instance.csv',
    ],
    'js': [
        'static/src/js/*.js'
    ],
    'css': [
        'static/src/css/*.css'
    ],
    'qweb': [
        'static/src/xml/*.xml'
    ],
    'installable': False,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
