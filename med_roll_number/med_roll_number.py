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
from openerp.osv import osv, fields

class im_roll_number(osv.Model):
    _name = 'im.roll.number'
    _rec_name = 'roll_number'

    _columns = {
            'roll_number': fields.char(size=8, string='Roll Number', required=True),
            # 'course_id': fields.many2one('op.course', string='Course', required=True),
            # 'batch_id': fields.many2one('op.batch', string='Batch', required=True),
            # 'standard_id': fields.many2one('op.standard', string='Standard', required=True),
            # 'division_id': fields.many2one('op.division', string='Division'),
            'patient_id': fields.many2one('im.patient', string='Patient', required=True),
    }

