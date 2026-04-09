#!/usr/bin/python3
"""
Application de Gestion des Incidents et Maintenance
Pour un village de vacances

Fonctionnalités :
- Signalement (CRUD) d'incidents via un formulaire
- Suivi d'état avec changements de statut
- Tableau de bord avec vue d'ensemble
- Assignation de tickets aux techniciens
"""

import os
from app import create_app

# Créer l'application
app = create_app(os.getenv('FLASK_ENV', 'development'))

if __name__ == '__main__':
    # Paramètres pour la ligne de commande
    debug_mode = os.getenv('FLASK_DEBUG', True)
    port = int(os.getenv('FLASK_PORT', 5000))
    host = os.getenv('FLASK_HOST', '0.0.0.0')  # Écoute sur toutes les interfaces
    
    # Force 0.0.0.0 pour accepter les connexions externes
    if host == 'localhost' or host == '127.0.0.1':
        host = '0.0.0.0'
    
    print(f"""
    ╔═══════════════════════════════════════════════════════════╗
    ║   Gestion des Incidents et Maintenance - Village          ║
    ║   Flask Application                                       ║
    ║                                                           ║
    ║   Démarrage sur http://{host}:{port}                  ║
    ║   Appuyez sur CTRL+C pour arrêter                        ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    app.run(host=host, port=port, debug=debug_mode)
