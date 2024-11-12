{
    'name': 'Gestione delle Segnalazioni',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Modulo per gestire le segnalazioni dei cittadini.',
    'description': """
        Questo modulo consente ai cittadini di inviare segnalazioni e permette ai dipendenti comunali di gestire le segnalazioni in modo efficiente.
    """,
    'author': 'Visionari',
    'depends': ['base', 'website'],
    'data': [
        'views/segnalazione_views.xml',
        'views/website_templates.xml',
        'security/ir.model.access.csv'
    ],
    'assets': {
        'web.assets_frontend': [
            'gestione_segnalazioni/static/src/css/segnalazioni.css',
        ],
    },
    'installable': True,
    'application': True,
}