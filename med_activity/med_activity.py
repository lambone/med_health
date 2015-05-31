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
from openerp.osv import osv, fields


class med_activity(osv.osv):
    _name = 'med.activity'

    _columns = {
        #'name': fields.char(string='Activity Name' ,size=128, required=True),
        'patient_id': fields.many2one('med.patient', string='Patient', required=True),
        'faculty_id': fields.many2one('med.faculty', string='Faculty'),
        'type_id': fields.many2one('med.activity.type', 'Activity Type'),
        'date': fields.date('Date'),
    }


class med_activity_type(osv.osv):
    _name = 'med.activity.type'

    _columns = {
        'name': fields.char(string='Activity Type', size=128, required=True),

    }




