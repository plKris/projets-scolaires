from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from enum import Enum as PyEnum
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class RoleEnum(PyEnum):
    """Rôles utilisateurs disponibles"""
    CLIENT = "client"
    ADMIN = "admin"


class StatusEnum(PyEnum):
    """États possibles d'un ticket"""
    OUVERT = "Ouvert"
    EN_COURS = "En cours"
    RESOLU = "Résolu"
    FERME = "Fermé"


class PriorityEnum(PyEnum):
    """Niveaux de priorité des tickets"""
    BASSE = "Basse"
    NORMALE = "Normale"
    HAUTE = "Haute"
    URGENTE = "Urgente"


class User(db.Model):
    """Utilisateur: administrateur, maintenance ou client"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default=RoleEnum.ADMIN.value, nullable=False)
    
    # Infos client
    nom_client = db.Column(db.String(100))
    num_chambre = db.Column(db.String(20))
    
    # Status
    actif = db.Column(db.Boolean, default=True)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password: str) -> None:
        """Hash et stocke le mot de passe"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password: str) -> bool:
        """Vérifie le mot de passe"""
        return check_password_hash(self.password_hash, password)
    
    def is_admin(self) -> bool:
        return self.role == RoleEnum.ADMIN.value

    def is_client(self) -> bool:
        return self.role == RoleEnum.CLIENT.value

    def __repr__(self) -> str:
        return f'<User {self.username} ({self.role})>'


class Chambre(db.Model):
    """Chambre du village de vacances"""
    __tablename__ = 'chambres'
    
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(20), unique=True, nullable=False)
    code_acces = db.Column(db.String(6), nullable=False)
    localite = db.Column(db.String(100))
    capacite = db.Column(db.Integer, default=2)
    occupee = db.Column(db.Boolean, default=False)
    
    # Relation à l'utilisateur
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='chambres')
    
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f'<Chambre {self.numero}>'


class Ticket(db.Model):
    """Ticket d'incident ou de maintenance"""
    __tablename__ = 'tickets'
    
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    statut = db.Column(db.String(20), default=StatusEnum.OUVERT.value, nullable=False)
    priorite = db.Column(db.String(20), default=PriorityEnum.NORMALE.value, nullable=False)
    
    # Chambre associée
    chambre_id = db.Column(db.Integer, db.ForeignKey('chambres.id'), nullable=False)
    chambre = db.relationship('Chambre', backref='tickets')

    # Utilisateurs
    createur_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    createur = db.relationship('User', foreign_keys=[createur_id], backref='tickets_crees')

    assignee_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    assignee = db.relationship('User', foreign_keys=[assignee_id], backref='tickets_assignes')
    
    # Infos supplémentaires
    reporter_email = db.Column(db.String(120))
    notes = db.Column(db.Text)
    modifie_par_admin = db.Column(db.Boolean, default=False)  # Indique si le ticket a été modifié par un admin
    
    # Timestamps
    date_creation = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    date_modification = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f'<Ticket {self.id}: {self.titre[:30]} [{self.statut}]>'
    
    def get_status_badge_color(self) -> str:
        """Retourne la classe CSS pour le badge de statut"""
        colors = {
            StatusEnum.OUVERT.value: 'danger',
            StatusEnum.EN_COURS.value: 'warning',
            StatusEnum.RESOLU.value: 'success',
            StatusEnum.FERME.value: 'secondary'
        }
        return colors.get(self.statut, 'secondary')
    
    def get_priority_badge_color(self) -> str:
        """Retourne la classe CSS pour le badge de priorité"""
        colors = {
            PriorityEnum.BASSE.value: 'info',
            PriorityEnum.NORMALE.value: 'primary',
            PriorityEnum.HAUTE.value: 'warning',
            PriorityEnum.URGENTE.value: 'danger'
        }
        return colors.get(self.priorite, 'primary')

