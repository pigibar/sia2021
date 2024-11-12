from odoo import models, fields

class Intervento(models.Model):
    _name = 'romeeye.intervento'
    _description = 'Gestione degli interventi'

    name = fields.Char(string="Nome Intervento", required=True)
    description = fields.Text(string="Descrizione")
    date = fields.Date(string="Data Intervento", default=fields.Date.today)
    location = fields.Char(string="Luogo")
    agent_id = fields.Many2one('res.users', string="Agente Responsabile")
    status = fields.Selection([
        ('inviato', 'Inviato'),
        ('in_lavorazione', 'In Lavorazione'),
        ('risolto', 'Risolto'),
    ], default='inviato', string="Stato")

