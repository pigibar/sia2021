from odoo import http

class SegnalazioniController(http.Controller):
    @http.route('/segnalazioni', type='http', auth='public', website=True)
    def list_segnalazioni(self, **kwargs):
        segnalazioni = http.request.env['segnalazione.model'].search([])
        return http.request.render('gestione_segnalazioni.lista_segnalazioni', {
            'segnalazioni': segnalazioni
        })