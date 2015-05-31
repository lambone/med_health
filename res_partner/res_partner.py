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

#from openerp.osv import osv, fields
from openerp import models, fields

class res_partner(osv.Model):
    _inherit = 'res.partner'

    _columns = {
        'relationship':fields.selection([('spouse','Spouse'),('child','Child'),('o','Other')], string='Relation'),
        'patient': fields.boolean('Patient', help="Check this box if this contact is a patient."),
        'doctor': fields.boolean('Doctor', help="Check this box if this contact is a doctor."),

        'qq': fields.char('qq', sting="QQ"),
        'wechat': fields.char('wechat',string= "Wechat"),
        'weibo': fields.char('weibo', string="Weibo"),
    }

