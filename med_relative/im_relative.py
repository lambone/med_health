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

class im_relative(osv.Model):
    _name = 'im.relative'

    _columns = {

            'name': fields.many2one('res.partner','Relative Name', required=True),
            'patient_ids': fields.many2many('im.patient', 'patient_relative_rel', 'med_patient', 'med_relative', string="Select Patient"),
            'user_id': fields.many2one('res.users', 'User', required=True),
    }

