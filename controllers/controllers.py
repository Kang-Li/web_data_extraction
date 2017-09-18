# -*- coding: utf-8 -*-
from odoo import http
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class WebDataExtraction(http.Controller):
    @http.route('/web_data_extraction/target_url', type='json', auth='public', methods=['POST'], csrf=False)
    def getHtml(self, target_url, source_url):
        response = urllib2.urlopen(target_url)
        html = response.read()
        # change page base
        idx = html.index('<head>')
        if idx != -1:
            idx += len('<head>')
            dom = '<base href="' + target_url + '"/>'
            html = html[:idx] + dom + html[idx:]
        # add click control JS
        idx = html.index('</head>')
        if idx != -1:
            file_path = "/web_data_extraction/static/src/js/iframe_click.js"
            click_js = '<script src="' + source_url + file_path + '">' + "</script>"
            html = html[:idx] + click_js + html[idx:]
            print(html)

        return {
            'html': html
        }
