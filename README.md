# 📚 Projets Scolaires

Bienvenue dans cette collection de projets d'apprentissage ! Ce workspace contient plusieurs applications développées avec différentes technologies et frameworks.

---

## 🗂️ Structure du Workspace

Ce projet contient quatre applications principales :

### 1. 🎓 **MediatekFormation**
**Une plateforme de formations vidéo avec gestion administrateur**

- **Framework** : Symfony 6.4
- **Base de données** : Doctrine ORM
- **Fonctionnalités** :
  - 📺 Consulter et organiser des formations vidéo
  - 📝 Gestion de playlists (admin)
  - 🎬 Ajouter, modifier et supprimer des formations
  - 🔐 Authentification administrateur
  - 📊 Filtrage et tri des contenus
  - 🔗 Intégration YouTube
  
- **Architecture** :
  - **Front-office** : Consultation des formations et playlists
  - **Back-office** : Gestion complète accessible via `/admin`

- **Pages principales** :
  - Playlists (public)
  - Formations (public)
  - Connexion admin
  - Gestion des formations (admin)
  - Gestion des playlists (admin)

📂 Dossier : [`mediatekformation/`](mediatekformation/)

---

### 2. ✈️ **Mes Voyages**
**Une application de gestion de voyages et destinations**

- **Framework** : Symfony 6.4
- **Base de données** : Doctrine ORM
- **Fonctionnalités** :
  - 🗺️ Cataloguer des destinations de voyage
  - 🏖️ Gestion des voyages proposés
  - 📋 Formulaires de gestion avancée
  - 🔐 Système d'authentification

- **Architecture** :
  - Interface publique de consultation
  - Panneau d'administration pour la gestion

📂 Dossier : [`mesvoyages/`](mesvoyages/)

---

### 3. 🔧 **Gestion des Incidents - Village de Vacances**
**Un système de signalement et suivi de maintenance**

- **Framework** : Flask 3.0
- **Base de données** : SQLAlchemy, MongoDB
- **Fonctionnalités** :
  - 🆘 Signalement d'incidents (CRUD)
  - 📌 Suivi du statut des tickets
  - 👷 Assignation aux techniciens
  - 📊 Tableau de bord
  - 📝 Gestion des incidents en temps réel

- **Architecture** :
  - API REST avec Flask
  - Formulaires WTForms
  - Stockage flexible avec MongoDB

📂 Dossier : [`projet-flask/`](projet-flask/)

---

### 4. �️ **ProjetCVVEN**
**Plateforme de gestion de réservations pour un Village de Vacances**

- **Framework** : CodeIgniter 4
- **Base de données** : MySQL/MariaDB
- **Fonctionnalités** :
  - 👤 Authentification et inscription utilisateur
  - 🏡 Consultation des logements/bungalows disponibles
  - 📋 Gestion des réservations (création, suivi, annulation)
  - 🔑 Contrôle d'accès par rôles
  - 💼 Espace utilisateur (profil et paramètres)
  - 🛠️ Interface d'administration complète

- **Architecture** :
  - Interface responsive avec Bootstrap
  - Icônes Font Awesome
  - Gestion de sessions sécurisée
  - Admin panel dédié

📂 Dossier : [`ProjetCVVEN/`](ProjetCVVEN/)

---

## 🛠️ Pile Technologique

| Technologie | Projets | Version |
|-------------|---------|---------|
| **PHP** | MediatekFormation, Mes Voyages, ProjetCVVEN | 8.1+ |
| **Symfony** | MediatekFormation, Mes Voyages | 6.4 |
| **CodeIgniter** | ProjetCVVEN | 4 |
| **Python** | Gestion Incidents | 3.10+ |
| **Flask** | Gestion Incidents | 3.0 |
| **Doctrine ORM** | MediatekFormation, Mes Voyages | 3.1+ |
| **SQLAlchemy** | Gestion Incidents | 3.0+ |
| **MySQL/MariaDB** | ProjetCVVEN | - |
| **MongoDB** | Gestion Incidents | - |

---

## 📦 Installation Rapide

### Pour les projets Symfony

```bash
# Accédez au dossier du projet
cd mediatekformation
# ou
cd mesvoyages

# Installez les dépendances
composer install

# Configurez votre base de données dans .env

# Exécutez les migrations
php bin/console doctrine:migrations:migrate

# Lancez le serveur de développement
php bin/console server:run
```

### Pour ProjetCVVEN (CodeIgniter 4)

```bash
# Accédez au dossier
cd ProjetCVVEN

# Installez les dépendances
composer install

# Configurez votre fichier .env
cp env .env

# Lancez le serveur de développement
php spark serve
```

### Pour le projet Flask

```bash
# Accédez au dossier
cd projet-flask

# Créez un environnement virtuel
python3 -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sur Windows

# Installez les dépendances
pip install -r requirements.txt

# Lancez l'application
python app.py
```

---

## 🚀 Démarrage des Applications

### MediatekFormation
- **Front-office** : http://localhost:8000/
- **Back-office** : http://localhost:8000/admin
- Credentials : À configurer dans la base de données

### Mes Voyages
- **Application** : http://localhost:8000/
- **Admin** : http://localhost:8000/admin

### Gestion des Incidents
- **Application** : http://localhost:5000/
- **Port personnalisable** : Via variable d'environnement `FLASK_PORT`

### ProjetCVVEN
- **Application** : http://localhost:8000/ (après configuration)
- **Admin** : http://localhost:8000/admin
- **Configuration** : Via fichier `env` et `.env`

---

## 📝 Notes de Développement

### Tests
Chaque projet Symfony inclut PHPUnit pour les tests :
```bash
php bin/phpunit
```

### Configuration
- Variables d'environnement : `.env` et `.env.local`
- Configuration Symfony : `config/packages/`
- Routes : `config/routes.yaml`

### Base de Données
- **ORM Symfony** : Doctrine
- **Migrations** : `php bin/console doctrine:migrations:*`
- **MongoDB Flask** : Configuration dans `app/models.py`

---

## 💡 Ressources Utiles

- [📚 Documentation Symfony](https://symfony.com/doc/current/index.html)
- [🐍 Documentation Flask](https://flask.palletsprojects.com/)
- [📖 Doctrine ORM](https://www.doctrine-project.org/)
- [🗂️ MongoDB](https://www.mongodb.com/)

---

## ✨ Fonctionnalités Communes

Tous les projets incluent :
- ✅ Gestion d'authentification
- ✅ Operateurs CRUD
- ✅ Validation des formulaires
- ✅ Gestion des erreurs
- ✅ Tests automatisés
- ✅ Structure MVC/conventions

---

## 👤 Auteur

Projets scolaires - 2024-2026

---

## 📄 Licence

Propriété intellectuelle - Usage privé

---

**Bon développement ! 🎉**