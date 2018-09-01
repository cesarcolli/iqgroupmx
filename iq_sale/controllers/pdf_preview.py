# -*- coding: utf-8 -*-

import os
import base64

from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import content_disposition

class PdfPreview(http.Controller):

    @http.route('/web/pdf_viewer/<int:pdf_id>/<string:pdf_name>', type='http', auth="user")
    def pdf_preview(self, pdf_id, pdf_name, **kw):

        pdf = request.env['ir.attachment'].browse([pdf_id])

        if not pdf.id:
            return 'PDF no encontrado'

        pdf_content = base64.b64decode(pdf.datas)

        if not pdf_content:
            return 'PDF no encontrado'

        return request.make_response(
            pdf_content,
            [
                ('Content-Type', 'application/pdf'),
                ('Content-Disposition: inline;', content_disposition('%s.pdf' % pdf.name))
            ]
        )