# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#    Copyright (C) 2014 Haiforce.com
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name" : "IM_Health",
    "version" : "0.1",
    "author" : "Roy Yang",
    "website" : "http://www.haiforce.com",
    "category": "Health Management",
    "complexity": "easy",
    "description":
        """A module to Health Management.
        A Module support the following functionalities:
        1. Patient Information
        2. Hospital Information
        3. Doctor Information
        4. Pharma Information
        5. Medicine Information
         """,
    "depends" : ["hr", "email_template", "crm"],
    "data" : [
            # "wizard/wiz_send_email_view.xml",
            # "security/school_security.xml",
            # "school_view.xml",
            # "security/ir.model.access.csv",
            # "admission_workflow.xml",
            # "student_sequence.xml",
            # "wizard/assign_roll_no_wizard.xml",
            # "wizard/move_standards_view.xml",
            # "wizard/wiz_meeting_view.xml",
            # "indentity_card_report.xml",
    ],
  'demo': [
           # 'demo/school_demo.xml'
            ],

    'test': [
        'test/school_test.yml',
        'test/assign_roll_no_test.yml',
        ],

    "installable": True,
    "auto_install": False,
    "application": True,
}


