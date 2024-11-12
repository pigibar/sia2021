from odoo import models, fields

class Segnalazione(models.Model):
    _name = 'segnalazione.model'
    _description = 'Gestione delle Segnalazioni'

    name = fields.Char('Titolo', required=True)
    descrizione = fields.Text('Descrizione', required=True)
    posizione = fields.Char('Posizione', required=True)
    data = fields.Date('Data', required=True, default=fields.Date.today)
    ora = fields.Float('Ora')
    stato = fields.Selection([
        ('inviata', 'Inviata'),
        ('in_lavorazione', 'In lavorazione'),
        ('risolta', 'Risolta')
    ], string='Stato', default='inviata')
    utente_id = fields.Many2one('res.users', string='Utente')
    municipio_id = fields.Many2one('res.municipio', string='Municipio')

    def some_method(self):
        # Usa il template da un altro modulo
        template = self.env.ref('website.website_template_id')
        # Fai qualcosa con il template, come renderizzarlo

class Municipio(models.Model):
    _name = 'res.municipio'
    _description = 'Municipio Responsabile'

    name = fields.Char('Nome Municipio', required=True)
    responsabile = fields.Char('Responsabile', required=True)
    telefono = fields.Char('Telefono')