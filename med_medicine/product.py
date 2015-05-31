# -*- encoding: utf-8 -*-
##############################################################################
#
#
#    Copyright (C) 2014-TODAY Haiforce(<http://www.haiforce.com>).
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
from openerp.osv import osv, fields
import time


class product_template(osv.Model):
    _inherit = "product.template"

    _columns = {
        'name': fields.char('Name', size=256, required=True, select=True),
    }


def _state_get(self, cr, uid, context):
    cr.execute('select name, name from product_state order by name')
    return cr.fetchall()


class product_product(osv.Model):
    """Medicine variant of product"""
    _inherit = "product.product"

    def name_get(self, cr, user, ids, context=None):
        ''' This method Returns the preferred display value (text representation) for the records with the given ids. 
        @param self : Object Pointer
        @param cr : Database Cursor
        @param uid : Current Logged in User
        @param ids :list of ids
        @param context : context arguments, like lang, time zone
        @return : tuples with the text representation of requested objects for to-many relationships
         '''

        if context is None:
            context = {}

        if isinstance(ids, (int, long)):
            ids = [ids]

        if not len(ids):
            return []

        def _name_get(d):
            name = d.get('name', '')
            ean = d.get('ean13', False)
            if ean:
                name = '[%s] %s' % (ean or '', name)
            return (d['id'], name)

        return map(_name_get, self.read(cr, user, ids, ['name', 'ean13'], context))

    def _default_categ(self, cr, uid, context=None):
        ''' This method put default category of product 
        @param self : Object Pointer
        @param cr : Database Cursor
        @param uid : Current Logged in User
        @param context : context arguments, like lang, time zone
         '''

        if context is None:
            context = {}
        if 'category_id' in context and context['category_id']:
            return context['category_id']
        md = self.pool.get('ir.model.data')
        res = False
        try:
            res = md.get_object_reference(cr, uid, 'library', 'product_category_1')[1]
        except ValueError:
            res = False
        return res

    def _tax_incl(self, cr, uid, ids, field_name, arg, context=None):
        ''' This method include tax in product 
        @param self : Object Pointer
        @param cr : Database Cursor
        @param uid : Current Logged in User
        @param ids :list of ids
        @param field_name : name of fields
        @param arg : other arguments
        @param context : context arguments, like lang, time zone
        @return : Dics
         '''

        res = {}
        for product in self.browse(cr, uid, ids):
            val = 0.0
            for c in self.pool.get('account.tax').compute(cr, uid, product.taxes_id, product.list_price, 1, False):
                val += round(c['amount'], 2)
            res[product.id] = round(val + product.list_price, 2)
        return res

    def _get_partner_code_name(self, cr, uid, ids, product, parent_id, context=None):
        ''' This method get the partner code name 
        @param self : Object Pointer
        @param cr : Database Cursor
        @param uid : Current Logged in User
        @param ids :list of ids
        @param product : name of field
        @param partner_id : name of field
        @param context : context arguments, like lang, time zone
        @return : Dics
         '''
        for supinfo in product.seller_ids:
            if supinfo.name.id == parent_id:
                return {'code': supinfo.product_code or product.default_code,
                        'name': supinfo.product_name or product.name}
        res = {'code': product.default_code, 'name': product.name}
        return res

    def _product_code(self, cr, uid, ids, name, arg, context=None):
        ''' This method get the product code 
        @param self : Object Pointer
        @param cr : Database Cursor
        @param uid : Current Logged in User
        @param ids :list of ids
        @param name : name of field
        @param arg : other argument
        @param context : context arguments, like lang, time zone
        @return : Dics
         '''

        res = {}
        if context is None:
            context = {}
        for p in self.browse(cr, uid, ids, context=context):
            res[p.id] = self._get_partner_code_name(cr, uid, [], p, context.get('parent_id', None), context=context)[
                'code']
        return res

    def copy(self, cr, uid, id, default=None, context={}):
        ''' This method Duplicate record with given id updating it with default values
        @param self : Object Pointer
        @param cr : Database Cursor
        @param uid : Current Logged in User
        @param id : id of the record to copy
        @param default : dictionary of field values to override in the original values of the copied record
        @param context : standard Dictionary
        @return : id of the newly created record 
        '''

        if default is None:
            default = {}
        default.update({'author_ids': []})
        return super(product_product, self).copy(cr, uid, id, default, context)


    _columns = {
        'name_pinyin': fields.char('Pinying', size=64, help="药品拼音名称"),
        'registration': fields.char('Registration',size=64, help="药品批文")
        'catalog_num': fields.char('Catalog number', size=64, help="It show the Identification number of books"),
        # 'lang': fields.many2one('product.lang', 'Language'),
        'code': fields.function(_product_code, method=True, type='char', string='Acronym', store=True),
        'manufacturer': fields.many2one('res.partner', string='Manufacturer'),
        'usage':fields.text('Usage'),
        # 'availability': fields.selection([('available','Available'),('notavailable','Not Available')], 'Book Availability'),
        # 'link_ids': many2manysym('product.product', 'medicine_medicine_rel', 'product_id1', 'product_id2', 'Related Medicine'),
        # "attchment_ids": fields.one2many("medicine.attachment", "product_id", "Book Attachments"),
    }

    _defaults = {
        # 'creation_date': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
        # 'availability': 'available',
        # 'categ_id': lambda self,cr,uid:self.pool.get('product.category').browse(cr,uid).categ_id.name[1],
    }

    _sql_constraints = [
        ('unique_ean13', 'unique(ean13)', 'The ean13 field must be unique across all the products'),
        ('code_uniq', 'unique (code)', 'The code of the product must be unique !')
    ]


# class medicine_attachment(osv.Model):
#     _name = "medicine.attachment"

    # _description = "Stores the attachments of the medicine"

    # _columns = {
    #     "name": fields.char("Description", size=20, required=True),
        # "product_id": fields.many2one("product.product", "Product"),
        # "date": fields.date("Attachment Date", required=True),
        # "attachment": fields.binary("Attachment"),
    # }

    # _defaults = {
    #     'date': lambda *a: time.strftime('%Y-%m-%d'),
    # }


