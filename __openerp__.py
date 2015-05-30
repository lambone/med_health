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
                * Faculty
                * Medical Check
                * 

    """,
    'author': 'Haiforce',
    'website': 'http://www.haiforce.com',
    'images': [],
    'depends': ['account_accountant',
                'hr','web','website'],
    'data': [
        'security/im_security.xml',
        'med_activity/med_activity_view.xml',
        'med_parent/med_parent_view.xml',
        'med_patient/med_patient_view.xml',
        # 'im_standard/im_standard_view.xml',
        'med_health/med_health_view.xml',
        'med_faculty/med_faculty_view.xml',
        # 'im_admission/im_admission_view.xml',
        # 'im_admission/im_admission_sequence.xml',
        # 'im_hostel_room/im_hostel_room_view.xml',
        # 'im_attendance_register/im_attendance_register_view.xml',
        'med_category/med_category_view.xml',
        # 'im_attendance_sheet/im_attendance_sheet_view.xml',
        # 'im_exam/im_exam_view.xml',
        # 'im_publisher/im_publisher_view.xml',
        # 'im_religion/im_religion_view.xml',
        # 'im_attendance_line/im_attendance_line_view.xml',
        # 'im_transportation/im_transportation_view.xml',
        # 'im_book_movement/im_book_movement_view.xml',
        # 'im_book_queue/im_book_queue_view.xml',
        # 'im_book_queue/im_book_queue_sequence.xml',
        # 'im_placement_offer/im_placement_offer_view.xml',
        # 'im_marksheet_register/im_marksheet_register_view.xml',
        # 'im_classroom/im_classroom_view.xml',
        # 'im_vehicle/im_vehicle_view.xml',
        # 'im_hostel/im_hostel_view.xml',
        # 'im_division/im_division_view.xml',
        # 'im_exam_attendees/im_exam_attendees_view.xml',
        # 'wizard/exam_seating_arrangement_view.xml',
        # 'wizard/book_request_queue_view.xml',
        # 'wizard/issue_book_view.xml',
        # 'wizard/return_book_view.xml',
        # 'wizard/patient_hall_tickets_wizard_view.xml',
        # 'wizard/admission_analysis_wizard_view.xml',
        # 'im_book/im_book_view.xml',
        # 'im_batch/im_batch_view.xml',
        # 'im_marksheet_line/im_marksheet_line_view.xml',
        # 'im_course/im_course_view.xml',
        # 'im_subject/im_subject_view.xml',
        'med_tag/med_tag_view.xml',
        # 'im_result_line/im_result_line_view.xml',
        # 'im_author/im_author_view.xml',
        # 'im_exam_type/im_exam_type_view.xml',
        # 'med_facility/im_facility_view.xml',
        "med_faculty/hr_view.xml",
        # 'im_scholarship/im_scholarship_view.xml',
        # 'im_scholarship_type/im_scholarship_type_view.xml',
        'med_roll_number/med_roll_number_view.xml',
        # 'im_library/im_library_view.xml',
        # 'im_timetable/im_timetable_view.xml',
        # 'im_assignment/im_assignment_view.xml',
        # 'im_assignment_sub_line/im_assignment_sub_line_view.xml',
        # 'im_assignment_sub_history/im_assignment_sub_history_view.xml',
        # 'im_achievement/im_achievement_view.xml',
        # 'im_achievement_type/im_achievement_type_view.xml',
        # 'im_exam_res_allocation/im_exam_res_allocation_view.xml',
        # 'im_exam_room/im_exam_room_view.xml',
        # 'im_allocat_division/im_allocat_division_view.xml',
        'wizard/generate_roll_number_view.xml',
        'wizard/generate_time_table_view.xml',
        # 'wizard/time_table_report.xml',
        'wizard/im_all_patient_wizard_view.xml',
        # 'wizard/patient_attendance_report_view.xml',
        # 'wizard/patient_migrate_view.xml',
        'security/ir.model.access.csv',
        # 'im_book_movement/wizard/returndate_view.xml',
        # 'im_book_movement/wizard/reserve_book_view.xml',
        # 'im_result_template/im_result_template_view.xml',
        'menu/health_menu.xml',
        'report/report_menu.xml',
        # 'im_book_purchase/im_book_purchase_view.xml',
        # 'dashboard/librarian_dashboard_view.xml',
        'dashboard/faculty_dashboard_view.xml',
        'dashboard/patient_dashboard_view.xml',
        'menu/patient_menu.xml',
        'menu/faculty_menu.xml',
        # 'menu/library_menu.xml',
        # 'menu/parent_menu.xml',
        # 'im_exam/im_exam_workflow.xml',
        # 'im_admission/im_admission_workflow_view.xml',
        'res_company/res_company.xml',
        # 'views/report_admission_analysis.xml',
        # 'views/report_bonafide_certificate.xml',
        # 'views/report_book_barcode.xml',
        # 'views/patient_marksheet.xml',
        # 'views/transportation.xml',
        # 'views/patient_idcard.xml',
        # 'views/library_idcard.xml',
        # 'views/report_ticket.xml',
        'views/patient_label.xml',
        # 'views/report_time_table_teacher_generate.xml',
        # 'views/generate_timetable_patient.xml',
        'views/openhealth_template.xml',
        'views/homepage_template.xml',

    ],
    'demo': [
                 'demo/op.category.csv',
                 'demo/op.course.csv',
                 'demo/op.subject.csv',
                 'demo/op.batch.csv',
                 'demo/op.standard.csv',
                 'demo/op.religion.csv',
                 'demo/op.tag.csv',
                 'demo/op.book.csv',
                 'demo/op.author.csv',
                 'demo/op.division.csv',
                 'demo/op.patient.csv',
                 'demo/op.faculty.csv',
                 'demo/op.exam.type.csv',
                'demo/res.users.csv',
                'demo/res.groups.csv',
                 'demo/op.period.csv',
                 'demo/im_comapny_data.xml',
                 'demo/op.book.queue.csv',
                 ],
    'css': ['static/src/css/base.css'],
    'qweb': [
        'static/src/xml/base.xml'],
    'js': ['static/src/js/chrome.js'],
    'test': [
             'test/configuration.yml',
             'test/new_admission.yml',
             'test/new_faculty.yml'
    ],
    'images': ['images/Admission_Process.png','images/Course_list.png','images/Faculty_management.png','images/Student_Information.png','images/TimeTable.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
