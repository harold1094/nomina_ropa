# -*- coding: utf-8 -*-
# from odoo import http


# class /var/lib/odoo/addons/18.0/nominaRopa(http.Controller):
#     @http.route('//var/lib/odoo/addons/18.0/nomina_ropa//var/lib/odoo/addons/18.0/nomina_ropa', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//var/lib/odoo/addons/18.0/nomina_ropa//var/lib/odoo/addons/18.0/nomina_ropa/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/var/lib/odoo/addons/18.0/nomina_ropa.listing', {
#             'root': '//var/lib/odoo/addons/18.0/nomina_ropa//var/lib/odoo/addons/18.0/nomina_ropa',
#             'objects': http.request.env['/var/lib/odoo/addons/18.0/nomina_ropa./var/lib/odoo/addons/18.0/nomina_ropa'].search([]),
#         })

#     @http.route('//var/lib/odoo/addons/18.0/nomina_ropa//var/lib/odoo/addons/18.0/nomina_ropa/objects/<model("/var/lib/odoo/addons/18.0/nomina_ropa./var/lib/odoo/addons/18.0/nomina_ropa"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/var/lib/odoo/addons/18.0/nomina_ropa.object', {
#             'object': obj
#         })

