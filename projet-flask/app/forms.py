from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, Regexp
from app.models import StatusEnum, PriorityEnum

# ==================== FORMULAIRES D'AUTHENTIFICATION ====================

class ConnexionClientForm(FlaskForm):
    """Connexion client - numéro chambre et code d'accès"""
    num_chambre = StringField('Numéro de chambre',
                              validators=[
                                  DataRequired(message='Numéro de chambre requis'),
                                  Length(min=1, max=20)
                              ])
    code_acces = StringField('Code d\'accès',
                            validators=[
                                DataRequired(message='Code d\'accès requis'),
                                Length(min=6, max=6, message='Le code doit faire 6 chiffres'),
                                Regexp(r'^\d{6}$', message='Le code doit contenir uniquement des chiffres')
                            ])
    submit = SubmitField('Se connecter')


class SignupClientForm(FlaskForm):
    """Formulaire d'inscription client"""
    nom_client = StringField('Nom', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[Optional(), Length(max=120)])
    num_chambre = StringField('Numéro de chambre', validators=[DataRequired(), Length(min=1, max=20)])
    code_acces = StringField('Code d\'accès (6 chiffres)', 
                           validators=[
                               DataRequired(), 
                               Length(min=6, max=6),
                               Regexp(r'^\d{6}$', message='Doit être 6 chiffres')
                           ])
    password = StringField('Mot de passe (optionnel)', validators=[Optional(), Length(min=6)])
    submit = SubmitField('S\'enregistrer')


# ==================== FORMULAIRES TICKETS ====================

class TicketForm(FlaskForm):
    """Créer un nouveau ticket"""
    titre = StringField('Titre du problème',
                       validators=[
                           DataRequired(message='Le titre est requis'),
                           Length(min=5, max=100, message='Entre 5 et 100 caractères')
                       ])
    
    description = TextAreaField('Description détaillée',
                               validators=[
                                   DataRequired(message='La description est requise'),
                                   Length(min=10, message='Au moins 10 caractères')
                               ])
    
    location = StringField('Localisation (pièce/zone)',
                          validators=[
                              DataRequired(message='La localisation est requise'),
                              Length(min=3, max=100)
                          ])
    
    priorite = SelectField('Niveau de priorité',
                          choices=[(p.value, p.value) for p in PriorityEnum],
                          default=PriorityEnum.NORMALE.value)
    
    submit = SubmitField('Signaler le problème')


class UpdateStatusForm(FlaskForm):
    """Mettre à jour le statut d'un ticket (admin uniquement)"""
    titre = StringField('Titre du problème',
                       validators=[
                           DataRequired(message='Le titre est requis'),
                           Length(min=5, max=100, message='Entre 5 et 100 caractères')
                       ])
    
    description = TextAreaField('Description détaillée',
                               validators=[
                                   DataRequired(message='La description est requise'),
                                   Length(min=10, message='Au moins 10 caractères')
                               ])
    
    statut = SelectField('Nouveau statut',
                        choices=[(s.value, s.value) for s in StatusEnum],
                        validators=[DataRequired(message='Sélectionnez un statut')])
    notes = TextAreaField('Notes (optionnel)', validators=[Optional()])
    submit = SubmitField('Mettre à jour le ticket')
