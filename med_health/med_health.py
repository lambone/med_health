# -*- coding: utf-8 -*-
#/#############################################################################
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
from openerp.osv import osv, fields
import time

class im_health(osv.Model):
    _name = 'im.health'
    
    _description = """ Health Detail for Patients"""
    
    _columns = {
            'patient_id': fields.many2one('im.patient', 'Patient'),
            # 'faculty_id': fields.many2one('op.faculty', 'Faculty'),
            'height': fields.float('Height(C.M.)', required=True),
            'weight': fields.float('weight(K.G.)', required=True),
            'blood_group': fields.selection([('A+','A+ve'),('B+','B+ve'),('O+','O+ve'),\
                                             ('AB+','AB+ve'),('A-','A-ve'),('B-','B-ve'),\
                                             ('O-','O-ve'),('AB-','AB-ve')], string='Blood Group', required=True),
            'physical_challenges': fields.boolean('Physical Challenge?'),
            'physical_challenges_note': fields.text('Physical Challenge'),
            'major_diseases': fields.boolean('Major Diseases?'),
            'major_diseases_note': fields.text('Major Diseases'),
            'eyeglasses': fields.boolean('Eye Glasses?'),
            'eyeglasses_no': fields.char('Eye Glasses', size=64),
            'regular_checkup': fields.boolean('Any Regular Checkup Required?'),
            'health_line': fields.one2many('im.health.line', 'health_id', 'Checkup Line'),
    }

    _defaults = {
                'physical_challenges': False,
                'major_diseases': False,
                'regular_checkup': False,
                 }


class im_health_line(osv.Model):
    _name = 'im.health.line'
    
    _columns = {
            # 'health_id': fields.many2one('im.health', 'Health'),
            'patient_id': fields.many2one('im.patient', 'Patient', select=True, required=True, ondelete='cascade'),
            'date': fields.date('Date'),
            # 'name': fields.text('Checkup Detail', required=True),
            'blood_pressure_systolic':fields.float('Blood Systolic Pressure (mmHg)'),
            'blood_pressure_diastolic':fields.float('Blood Diastolic Pressure (mmHg)'),
            'blood_glucose':fields.float('Blood Glucose(mmol/L)'),
            'ECG':fields.float('ECG'),
            'recommendation': fields.text('Checkup Recommendation'),
    }

    _defaults = {
                'date': time.strftime('%Y-%m-%d'),
                 }



