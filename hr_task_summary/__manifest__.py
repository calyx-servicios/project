# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Task Summary',
    'author': 'Calyx Servicios S.A., Odoo Community Association (OCA)',
    'website': 'http://odoo.calyx-cloud.com.ar/',
    'license': 'AGPL-3',
    'version': '11.0.1.0.0',
    'development_status': 'Production/Stable',
    'application': False,
    'installable': True,
    'depends': ['hr', 'project','hr_timesheet'],
    'data': [
        'views/hr_views.xml',
     ],
}
