# 🔧 Gestion des Incidents - Village de Vacances

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-13AA52?logo=mongodb&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-3.0%2B-FF0000?logo=database&logoColor=white)

Système complet de signalement, suivi et gestion des incidents et demandes de maintenance pour un village de vacances. Permet aux vacanciers de signaler des problèmes et aux techniciens de suivre les interventions en temps réel.

## 📋 Table des matières

- [Aperçu](#aperçu)
- [Fonctionnalités](#fonctionnalités)
- [Stack Technique](#stack-technique)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [Architecture](#architecture)
- [Tests](#tests)
- [API](#api)
- [Ressources](#ressources)

## 🎯 Aperçu

**Gestion des Incidents** est une application web qui permet :
- 🆘 **Signaler** des incidents (formulaire simple)
- 📌 **Suivre** le statut des tickets en temps réel
- 👷 **Assigner** les incidents aux techniciens
- 📊 **Visualiser** un tableau de bord avec les statistiques
- 🔔 **Notifier** les utilisateurs des changements de statut
- 📈 **Analyser** les incidents par type et priorité

### Acteurs
- **Vacanciers** : Signalent les problèmes
- **Coordinateur** : Assignation et suivi
- **Techniciens** : Interventions et résolution

## ✨ Fonctionnalités

### Signalement (Vacanciers)
- ✅ Formulaire de signalement d'incident (CRUD)
- ✅ Choix du type d'incident (électricité, plomberie, électroménager, etc.)
- ✅ Sélection de la priorité (basse, normale, haute, urgente)
- ✅ Localisation du problème (numéro de bungalow/chalet)
- ✅ Description détaillée avec possibilité de pièces jointes
- ✅ Suivi en temps réel du statut

### Gestion et Suivi (Coordinateur/Admin)
- ✅ **Tableau de bord** avec vue d'ensemble
- ✅ **Liste des incidents** avec filtres et recherche
- ✅ **Changement de statut** : Ouvert → En cours → Résolu → Fermé
- ✅ **Assignation** aux techniciens disponibles
- ✅ **Notes privées** et commentaires publics
- ✅ **Historique** de tous les changements
- ✅ **Rapports** et statistiques
- ✅ **Notifications** par email

### Suivi Technicien
- ✅ Liste des incidents qui lui sont assignés
- ✅ Détails complets du problème
- ✅ Interface de mise à jour (commentaires, heures de travail)
- ✅ Clôture des tickets après intervention

## 🛠️ Stack Technique

| Technologie | Version | Usage |
|-------------|---------|-------|
| Python | 3.10+ | Langage principal |
| Flask | 3.0+ | Framework web |
| SQLAlchemy | 3.0+ | ORM (SQL) |
| MongoDB | 5.0+ | Base de données NoSQL |
| WTForms | 3.1+ | Formulaires |
| Flask-WTF | 1.2+ | Intégration WTForms |
| PyMongo | 4.6+ | Driver MongoDB |
| Email-validator | 2.1+ | Validation emails |

## 📦 Installation

### Prérequis
- Python 3.10 ou supérieur
- MongoDB (local ou cloud : MongoDB Atlas)
- pip (gestionnaire de paquets Python)
- Git

### Étapes

```bash
# 1. Cloner le repository
git clone <url-repo>
cd projet-flask

# 2. Créer un environnement virtuel
python3 -m venv venv

# 3. Activer l'environnement virtuel
# Sur Linux/macOS :
source venv/bin/activate
# Sur Windows :
venv\Scripts\activate

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Configurer l'environnement
cp .env.example .env
# Éditer .env et configurer les variables

# 6. Initialiser la base de données
python init_db.py

# 7. Lancer l'application
python app.py
# Ou via le script :
bash demarrer.sh
```

L'application sera accessible à : `http://localhost:5000`

## ⚙️ Configuration

### Variables d'environnement (.env)

```env
# Environnement Flask
FLASK_ENV=development
FLASK_DEBUG=True

# Serveur
FLASK_HOST=0.0.0.0
FLASK_PORT=5000

# Base de données MongoDB
MONGODB_URI=mongodb://localhost:27017
MONGODB_DB=incidents_db

# Ou MongoDB Atlas :
MONGODB_URI=mongodb+srv://user:password@cluster.mongodb.net/incidents_db?retryWrites=true&w=majority

# Sécurité
SECRET_KEY=your-secret-key-here

# Email (pour notifications)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_USE_TLS=True

# Admin
ADMIN_USERNAME=admin
ADMIN_PASSWORD=secure_password
```

## 🚀 Utilisation

### URLs principales

#### Accueil et signalement
```
http://localhost:5000/              # Page d'accueil
http://localhost:5000/incident/new  # Signaler un incident
```

#### Admin (Tableau de bord)
```
http://localhost:5000/admin              # Dashboard
http://localhost:5000/admin/incidents    # Lister les incidents
http://localhost:5000/admin/incidents/id # Détail et gestion
```

### Flux utilisateur

#### Vacancier
1. Accéder à la page d'accueil
2. Cliquer sur "Signaler un problème"
3. Remplir le formulaire :
   - Type d'incident
   - Priorité
   - Localisation
   - Description détaillée
4. Soumettre
5. Recevoir un numéro de ticket
6. Suivre le statut en ligne

#### Coordinateur/Admin
1. Connecter via `/admin`
2. Consulter le tableau de bord
3. Pour chaque incident :
   - Assigner à un technicien
   - Changer le statut
   - Ajouter des notes
   - Générer des rapports

## 🏗️ Architecture

### Structure du projet

```
projet-flask/
├── app/
│   ├── __init__.py          # Initialisation Flask
│   ├── models.py            # Modèles (SQLAlchemy + MongoDB)
│   ├── forms.py             # Formulaires WTForms
│   ├── routes.py            # Points d'entrée (routes)
│   ├── auth.py              # Authentification
│   └── static/              # CSS, JS, images
│       ├── css/
│       ├── js/
│       └── images/
├── templates/               # Templates HTML Jinja2
│   ├── base.html            # Template de base
│   ├── index.html           # Accueil
│   ├── incident_form.html   # Formulaire signalement
│   ├── incident_detail.html # Détail d'un incident
│   └── admin/               # Templates admin
├── app.py                   # Point d'entrée principal
├── config.py                # Configuration
├── init_db.py               # Initialisation BD
├── requirements.txt         # Dépendances
├── .env                     # Variables d'environnement
└── demarrer.sh              # Script de démarrage
```

### Modèles de données

#### Incident (MongoDB)
```
{
  _id: ObjectId,
  numero_ticket: String (unique),
  type: String (enum),
  priorite: String (enum),
  localisation: String,
  description: String,
  statut: String (enum),
  createur_id: ObjectId,
  assignee_id: ObjectId (optional),
  date_creation: DateTime,
  date_modification: DateTime,
  commentaires: [
    { auteur: String, texte: String, date: DateTime }
  ],
  photos: [String] (URLs)
}
```

#### Utilisateur (SQLAlchemy)
```
- id (Integer)
- username (String, unique)
- password (String, hashed)
- email (String)
- role (String: vacancier, coordinateur, technicien)
- date_creation (DateTime)
```

## 🔄 Flux des statuts

```
Ouvert → En cours → Résolu → Fermé
```

**Transitions** :
- Vacancier crée ticket → **Ouvert**
- Admin assigne → **En cours**
- Technicien intervient → **Résolu**
- Admin vérifie → **Fermé**

## ✅ Tests

```bash
# Lancer les tests
python -m pytest

# Tests spécifiques
python -m pytest tests/test_incident.py

# Avec couverture de code
python -m pytest --cov=app tests/
```

## 🔐 Sécurité

- ✅ Authentification par session
- ✅ Hachage des mots de passe (Werkzeug)
- ✅ Validation CSRF sur les formulaires
- ✅ Validation des formulaires côté serveur
- ✅ Validation des uploads (type, taille)
- ✅ Protection des routes sensibles
- ✅ Injection SQL prévenue (SQLAlchemy ORM)
- ✅ Input sanitization

## 📊 Tableau de bord Admin

Le dashboard affiche :
- 📈 Nombre total d'incidents
- ⏳ Incidents en attente
- 🔴 Incidents urgents
- ✅ Incidents résolus
- 👷 Charge de travail par technicien
- 📊 Graphiques statistiques

## 🔌 API

Endpoints disponibles :

```
GET  /api/incidents              # Liste les incidents
GET  /api/incidents/<id>         # Détail d'un incident
POST /api/incidents              # Créer un incident
PUT  /api/incidents/<id>         # Modifier un incident
DELETE /api/incidents/<id>       # Supprimer un incident
POST /api/incidents/<id>/comment # Ajouter un commentaire
```

**Authentification** : Token JWT (optionnel)

## 🚀 Déploiement

### Production

```bash
# Avec Gunicorn
pip install gunicorn
gunicorn --workers 4 --bind 0.0.0.0:5000 app:app

# Avec une reverse proxy (Nginx/Apache)
# Voir configuration dans docs/deployment.md
```

## 📚 Ressources

- [Documentation Flask](https://flask.palletsprojects.com/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/)
- [MongoDB Documentation](https://docs.mongodb.com/)
- [SQLAlchemy ORM](https://www.sqlalchemy.org/)
- [WTForms](https://wtforms.readthedocs.io/)

## 📝 Licence

Propriété intellectuelle - Usage privé

## 👨‍💻 Support

Pour toute question ou bug report, consultez la section Issues du repository.

## 🎯 Roadmap Future

- [ ] Intégration SMS pour notifications
- [ ] Mobile app (React Native)
- [ ] Système de notation des techniciens
- [ ] Statistiques avancées et rapports PDF
- [ ] Intégration calendrier pour planification
- [ ] Chat en direct avec support
