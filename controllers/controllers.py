# -*- coding: utf-8 -*-
from odoo import http

class WebDataExtraction(http.Controller):
    @http.route('/web_data_extraction', auth='public')
    def list(self, **kw):
        return http.request.render('web_data_extraction.target_url', {})