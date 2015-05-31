# -*- coding: utf-8 -*-
# /#############################################################################
#
#
#    Copyright (C) 2014-TODAY Haiforce(<http://www.haiforce.com>).
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
#from openerp import models, fields
from openerp.osv import fields, osv
import time


class med_patient(osv.Model):
    _name = 'med.patient'
    _inherits = {'res.partner': 'partner_id'}

    # everytime paticipate the activity/campaign/event, will assign a unique number

    def _get_curr_roll_number(self, cr, uid, ids, fields, arg, context=None):
        ret_val = {}
        for self_obj in self.browse(cr, uid, ids, context=context):
            roll_no = 0
            seq = 0
            for roll_number in self_obj.roll_number_line:
                if roll_number.standard_id.sequence > seq:
                    roll_no = roll_number.roll_number
                    seq = roll_number.standard_id.sequence
            ret_val[self_obj.id] = roll_no

        return ret_val

    def _get_roll(self, cr, uid, ids, context=None):
        result = {}
        for line in self.pool.get('med.roll.number').browse(cr, uid, ids, context=context):
            result[line.patient_id.id] = True
        return result.keys()


    _columns = {
        'name': fields.char(size=128, string='First Name', required=True),
        # 'middle_name': fields.char(size=128, string='Middle Name', required=True),
        # 'last_name': fields.char(size=128, string='Last Name', required=True),
        'birth_date': fields.date(string='Birth Date', required=True),
        # 'blood_group': fields.selection([('A+','A+ve'),('B+','B+ve'),('O+','O+ve'),('AB+','AB+ve'),('A-','A-ve'),('B-','B-ve'),('O-','O-ve'),('AB-','AB-ve')], string='Blood Group'),
        'gender': fields.selection([('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender', required=True),
        # 'nationality': fields.many2one('res.country', string='Nationality'),
        # 'language': fields.many2one('res.lang', string='Mother Tongue'),
        'category': fields.many2one('med.category', string='Category', required=True),
        'emergency_contact': fields.many2one('res.partner', string='Emergency Contact'),
        'id_number': fields.char(size=64, string='ID Card Number'),
        # 'photo': fields.binary(string='Photo'),
        # 'course_id': fields.many2one('op.course', string='Course', required=True),
        # 'division_id': fields.many2one('op.division', string='Division'),
        # 'batch_id': fields.many2one('op.batch', string='Batch', required=True),
        # 'standard_id': fields.many2one('op.standard', string='Standard', required=True),
        # 'roll_number_line': fields.one2many('op.roll.number','patient_id','Roll Number'),
        'partner_id': fields.many2one('res.partner', 'Partner', required=True, ondelete="cascade"),
        'health_lines': fields.one2many('med.health', 'patient_id', 'Health Detail'),
        'roll_number': fields.function(_get_curr_roll_number,
                                       method=True,
                                       string='Current Roll Number',
                                       type='char',
                                       size=8,
                                       store={
                                           'med.roll.number': (_get_roll, [], 10),
                                       }),
        # 'allocation_ids': fields.many2many('op.assignment', 'im_patient_assignment_rel', 'im_patient_id','op_assignment_id', string='Assignment'),
        # 'current_position': fields.char(string='Current Position', size=256),
        'email': fields.char(string='Email', size=128),
        'phone': fields.char(string='Phone Number', size=256),
        'user_id': fields.many2one('res.users', 'User'),
        'activity_log': fields.one2many('med.activity', 'patient_id', 'Activity Log'),
        # 'relative_ids': fields.many2many('med.relatives', 'im_relative_patient_rel', 'im_relative_id', 'im_patient_id', string='Relatives'),
    }

