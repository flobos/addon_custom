# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,api, models, _
from odoo.addons import decimal_precision as dp


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'


    @api.depends('product_id')
    @api.onchange('discount')
    def _onchange_partner_discount(self):
        if self.product_id and self.order_id.partner_id:
            if self.discount > 0:
                partner = self.order_id.partner_id
                if self.discount > partner.max_discount:
                    warning = {
                        'title': _('Warning!'),
                        'message': _(u'El valor de descuento que desea ingresar supera el descuento maximo permitido para el cliente %s!'%partner.name),
                    }
                    self.discount = partner.max_discount
                    return {'warning': warning}
