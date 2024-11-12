from odoo import http

class RomeyeInterventoController(http.Controller):

    @http.route('/romeeye/interventi/', auth='user', website=True)
    def list_interventi(self):
        interventi = http.request.env['romeeye.intervento'].search([])
        return http.request.render('romeeye.intervento_list', {
            'interventi': interventi
        })

    @http.route('/romeeye/intervento/<model("romeeye.intervento"):intervento>/', auth='user', website=True)
    def intervento_detail(self, intervento):
        return http.request.render('romeeye.intervento_detail', {
            'intervento': intervento
        })
