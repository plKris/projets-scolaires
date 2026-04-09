"""
Module d'authentification simple - clients et admin
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import db, User, Chambre, RoleEnum
from app.forms import ConnexionClientForm, SignupClientForm
from functools import wraps

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# ==================== DÉCORATEURS ====================

def login_required(f):
    """Vérifier que l'utilisateur est connecté"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Vous devez être connecté', 'warning')
            return redirect(url_for('auth.login_client'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    """Vérifier que l'utilisateur est admin"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Vous devez être connecté', 'warning')
            return redirect(url_for('auth.login_client'))
        
        if session.get('user_role') != 'admin':
            flash('Accès réservé à l\'administrateur', 'danger')
            return redirect(url_for('main.accueil'))
        
        return f(*args, **kwargs)
    return decorated_function

# ==================== ROUTES ====================

@auth_bp.route('/login-client', methods=['GET', 'POST'])
def login_client():
    """Connexion client - numéro chambre + code (pas de password)"""
    if 'user_id' in session:
        return redirect(url_for('main.accueil'))
    
    form = ConnexionClientForm()
    if form.validate_on_submit():
        # Cherche la chambre avec numéro et code
        chambre = Chambre.query.filter_by(
            numero=form.num_chambre.data,
            code_acces=form.code_acces.data
        ).first()
        
        if not chambre:
            flash('Numéro ou code d\'accès invalide', 'danger')
            return redirect(url_for('auth.login_client'))
        
        # Connecte avec la session
        session['chambre_id'] = chambre.id
        session['chambre_numero'] = chambre.numero
        # Pour éviter les confusions avec les PK numériques, utiliser 0 comme user_id pour les clients
        session['user_id'] = 0
        session['user_role'] = 'client'
        # Token pour invalider les sessions au redémarrage du serveur
        from flask import current_app
        session['session_token'] = current_app.config['SESSION_TOKEN']
        flash(f'Bienvenue chambre {chambre.numero}!', 'success')
        return redirect(url_for('main.accueil'))
    
    return render_template('auth/login_client.html', form=form)


@auth_bp.route('/logout')
def logout():
    """Déconnexion"""
    session.clear()
    flash('Déconnecté', 'info')
    return redirect(url_for('main.accueil'))

@auth_bp.route('/admin-login', methods=['POST'])
def admin_login():
    """Connexion admin"""
    username = request.form.get('username')
    password = request.form.get('password')
    
    if not username or not password:
        flash('Identifiants requis', 'danger')
        return redirect(url_for('main.accueil'))
    
    user = User.query.filter_by(username=username).first()
    
    if user and user.check_password(password) and user.is_admin():
        session['user_id'] = user.id
        session['user_role'] = 'admin'
        # Token pour invalider les sessions au redémarrage du serveur
        from flask import current_app
        session['session_token'] = current_app.config['SESSION_TOKEN']
        flash(f'Bienvenue admin!', 'success')
        return redirect(url_for('main.accueil'))
    
    flash('Identifiants invalides', 'danger')
    return redirect(url_for('main.accueil'))


@auth_bp.route('/signup-client', methods=['GET', 'POST'])
def signup_client():
    """Créer un nouveau compte client avec chambre"""
    if 'user_id' in session:
        return redirect(url_for('main.accueil'))

    form = SignupClientForm()
    if form.validate_on_submit():
        try:
            numero = form.num_chambre.data
            code = form.code_acces.data

            # Vérifier que la chambre n'existe pas déjà
            if Chambre.query.filter_by(numero=numero).first():
                flash('Le numéro de chambre est déjà enregistré.', 'danger')
                return render_template('auth/signup_client.html', form=form)

            # Créer la chambre
            chambre = Chambre(numero=numero, code_acces=code)
            db.session.add(chambre)
            db.session.flush()

            # Créer l'utilisateur client associé si les infos sont fournies
            if form.nom_client.data:
                user = User(
                    username=f'client_{numero}',
                    email=form.email.data or '',
                    nom_client=form.nom_client.data,
                    role=RoleEnum.CLIENT.value
                )
                if form.password.data:
                    user.set_password(form.password.data)
                db.session.add(user)
                db.session.flush()
                chambre.user_id = user.id

            db.session.commit()
            flash('✅ Inscription réussie! Vous pouvez maintenant vous connecter.', 'success')
            return redirect(url_for('auth.login_client'))
        
        except Exception as e:
            db.session.rollback()
            flash(f'Erreur lors de l\'inscription: {str(e)}', 'danger')

    return render_template('auth/signup_client.html', form=form)
