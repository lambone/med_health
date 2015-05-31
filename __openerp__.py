# -*- coding: utf-8 -*-
#/#############################################################################
#
#    
#    Copyright (C) 2014-TODAY Haiforce (<http://www.haiforce.com>).
#
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
#/#############################################################################

{
    'name': 'Internet+ Medical Health',
    'version': '1.0',
    'category': 'Health',
    "sequence": 3,
    'summary': 'Manage Patient, Faculties and Clinical Institute',
    'complexity': "easy",
    'description': """
            This module provide overall Clinical management system over Odoo
            Features includes managing
                * Patient
                * Faculty (Doctor, pharmacist,etc.,
                * Medical Check
                *
    """,
    'author': 'Haiforce',
    'website': 'http://www.haiforce.com',
    'images': ['images/med_health.png'],
    'depends': ['hr','web','website'],
    'data': [
        # 'security/im_security.xml',
        # 'med_activity/med_activity_view.xml',
        # 'med_parent/med_parent_view.xml',
        'med_patient/med_patient_view.xml',
        # 'med_category/med_category_view.xml',
        # 'med_health/med_health_view.xml',
        # 'med_faculty/med_faculty_view.xml',
        # 'med_tag/med_tag_view.xml',
        # 'med_facility/im_facility_view.xml',
        # "med_faculty/hr_view.xml",
        # 'med_roll_number/med_roll_number_view.xml',
        # 'wizard/generate_roll_number_view.xml',
        # 'wizard/generate_time_table_view.xml',
        # 'wizard/im_all_patient_wizard_view.xml',
        'res_company/res_company.xml',

        # 'security/ir.model.access.csv',
        'menu/med_health_menu.xml',
        'menu/patient_menu.xml',
        # 'menu/faculty_menu.xml',
        # 'menu/parent_menu.xml',
        # 'report/report_menu.xml',
        # 'views/medhealth_template.xml',
        # 'views/homepage_template.xml',


        # 'im_batch/im_batch_view.xml',

        # 'im_allocat_division/im_allocat_division_view.xml',

        # 'wizard/time_table_report.xml',

        # 'dashboard/faculty_dashboard_view.xml',
        # 'dashboard/patient_dashboard_view.xml',

        # 'im_exam/im_exam_workflow.xml',
        # 'im_admission/im_admission_workflow_view.xml',
        # 'views/report_admission_analysis.xml',
        # 'views/report_bonafide_certificate.xml',
        # 'views/report_book_barcode.xml',
        # 'views/patient_marksheet.xml',
        # 'views/transportation.xml',
        # 'views/patient_idcard.xml',
        # 'views/library_idcard.xml',
        # 'views/report_ticket.xml',
        # 'views/patient_label.xml',
        # 'views/report_time_table_teacher_generate.xml',
        # 'views/generate_timetable_patient.xml',


    ],
    'demo': [
                 ],
    'css': ['static/src/css/base.css'],
    'qweb': [
        'static/src/xml/base.xml'],
    'js': ['static/src/js/chrome.js'],
    'test': [
    ],
    # 'images': ['images/Admission_Process.png','images/Course_list.png','images/Faculty_management.png','images/Student_Information.png','images/TimeTable.png'],

    'installable': True,
    'auto_install': False,
    'application': True,
}
