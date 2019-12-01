# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, _
from odoo.osv.expression import get_unaccent_wrapper

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = "Partners Base Chile"
  
    max_discount = fields.Float(sring="(%) Descuento ", default=10)
