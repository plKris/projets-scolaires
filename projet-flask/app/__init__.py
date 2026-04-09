from flask import Flask
from config import config
from app.models import db
import uuid

def create_app(config_name='development'):
    """Factory function pour créer l'application Flask"""
    app = Flask(__name__)
    
    # Configuration
    app.config.from_object(config[config_name])
    
    # Générer un token unique pour cette session du serveur (invalide les sessions au redémarrage)
    app.config['SESSION_TOKEN'] = str(uuid.uuid4())
    
    # Initialiser les extensions
    db.init_app(app)
    
    # Créer les tables dans le contexte de l'application
    with app.app_context():
        db.create_all()
    
    # Hook pour valider le session token
    @app.before_request
    def validate_session():
        from flask import session, redirect, url_for
        session_token = session.get('session_token')
        current_token = app.config['SESSION_TOKEN']
        
        # Si l'utilisateur a une session mais le token ne correspond pas, le déconnecter
        if session.get('user_id') and session_token != current_token:
            session.clear()
            return redirect(url_for('main.accueil'))
    
    # Rendre user disponible dans tous les templates
    @app.context_processor
    def inject_user():
        from flask import session
        from app.models import User
        user = None
        # `user_id` peut être un entier pour les utilisateurs admin
        # ou une valeur non-entière pour les clients (ex: identifiant basé sur chambre).
        # On vérifie proprement avant d'utiliser en tant que PK.
        user_id = session.get('user_id')
        if isinstance(user_id, int) and user_id > 0:
            user = User.query.get(user_id)
        return dict(current_user=user, user_role=session.get('user_role', 'client'))
    
    # Enregistrer les blueprints
    from app.routes import main_bp, tickets_bp
    from app.auth import auth_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(tickets_bp)
    app.register_blueprint(auth_bp)
    
    return app
