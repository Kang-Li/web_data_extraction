# -*- coding: utf-8 -*-
from odoo import http

# class WebDataExtraction(http.Controller):
#     @http.route('/web_data_extraction/web_data_extraction/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/web_data_extraction/web_data_extraction/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('web_data_extraction.listing', {
#             'root': '/web_data_extraction/web_data_extraction',
#             'objects': http.request.env['web_data_extraction.web_data_extraction'].search([]),
#         })

#     @http.route('/web_data_extraction/web_data_extraction/objects/<model("web_data_extraction.web_data_extraction"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('web_data_extraction.object', {
#             'object': obj
#         })