#!/usr/bin/env python3
"""
Script d'initialisation simple - chambres et 1 compte admin
"""

import os
from app import create_app
from app.models import db, User, Chambre, RoleEnum

app = create_app(os.getenv('FLASK_ENV', 'development'))

def init_db():
    """Initialiser complètement la base"""
    with app.app_context():
        # Créer les chambres
        if Chambre.query.first() is None:
            chambres_data = [
                {"numero": "101", "localite": "Bungalow A", "code": "111111"},
                {"numero": "102", "localite": "Bungalow A", "code": "222222"},
                {"numero": "103", "localite": "Bungalow A", "code": "333333"},
                {"numero": "201", "localite": "Bungalow B", "code": "444444"},
                {"numero": "202", "localite": "Bungalow B", "code": "555555"},
                {"numero": "203", "localite": "Bungalow B", "code": "666666"},
                {"numero": "301", "localite": "Chalet 1", "code": "777777"},
                {"numero": "302", "localite": "Chalet 1", "code": "888888"},
            ]
            
            print("\n🔑 Chambres créées:")
            print("Numéro | Code      | Localité")
            print("-------|-----------|----------")
            
            for data in chambres_data:
                chambre = Chambre(
                    numero=data["numero"],
                    code_acces=data["code"],
                    localite=data["localite"]
                )
                db.session.add(chambre)
                print(f"{data['numero']}    | {data['code']}    | {data['localite']}")
            
            db.session.commit()
            print(f"\n✅ {len(chambres_data)} chambres OK!\n")
        
        # Créer l'admin
        admin = User.query.filter_by(username="admin").first()
        if not admin:
            admin = User(
                username="admin",
                email="admin@village.fr",
                nom_client="Administrateur",
                role=RoleEnum.ADMIN.value
            )
            admin.set_password("admin123")
            db.session.add(admin)
            db.session.commit()
            print("👤 Compte admin créé")
            print("   Utilisateur: admin")
            print("   Mot de passe: admin123\n")
        else:
            print("✓ Admin existe déjà\n")

if __name__ == '__main__':
    print("""
    ╔════════════════════════════════════╗
    ║   Initialisation BD                ║
    ╚════════════════════════════════════╝
    """)
    init_db()
    print("✅ Prêt!")
