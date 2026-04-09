# ✈️ Mes Voyages

![PHP](https://img.shields.io/badge/PHP-8.1%2B-777BB4?logo=php&logoColor=white)
![Symfony](https://img.shields.io/badge/Symfony-6.4-000000?logo=symfony&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?logo=mysql&logoColor=white)
![Doctrine](https://img.shields.io/badge/Doctrine-ORM-EA7343?logo=database&logoColor=white)

Plateforme interactive de gestion et découverte de destinations de voyage. Explorez des destinations exotiques, consultez les voyages proposés et administrez le contenu via un panneau sécurisé.

## 📋 Table des matières

- [Aperçu](#aperçu)
- [Fonctionnalités](#fonctionnalités)
- [Stack Technique](#stack-technique)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [Architecture](#architecture)
- [Tests](#tests)
- [Ressources](#ressources)

## 🌍 Aperçu

**Mes Voyages** est une application web qui permet :
- 🗺️ **Découvrir** des destinations de voyage du monde entier
- 📖 **Consulter** les détails des voyages proposés
- ⭐ **Évaluer** et **commenter** les destinations
- 🔐 **S'authentifier** comme administrateur
- 📝 **Gérer** (CRUD) les voyages et destinations
- 🖼️ **Ajouter** des images et descriptions

### Architecture
- **Front-office** : Interface publique de découverte et consultation
- **Back-office** : Panneau d'administration (accessible via `/admin`)

## ✨ Fonctionnalités

### Front-office (Public)
- ✅ Consultation des destinations avec galeries d'images
- ✅ Détails complets des voyages (prix, dates, itinéraires)
- ✅ Système de filtrage par région/continent
- ✅ Recherche de destinations
- ✅ Avis et commentaires des voyageurs
- ✅ Carte interactive des destinations

### Back-office (Admin)
- ✅ **Authentification** sécurisée
- ✅ **Gestion des voyages** : créer, modifier, supprimer
- ✅ **Gestion des destinations** : ajouter, gérer
- ✅ **Gestion des images** : upload et galerie
- ✅ **Formulaires dynamiques** avec validation
- ✅ **Gestion des tarifs** et promotions
- ✅ **Suivi des réservations**
- ✅ **Messages flash** pour retours utilisateur

## 🛠️ Stack Technique

| Technologie | Version | Usage |
|-------------|---------|-------|
| PHP | 8.1+ | Langage principal |
| Symfony | 6.4 | Framework web |
| Doctrine ORM | 3.3+ | ORM & Migrations |
| MySQL/MariaDB | - | Base de données |
| Twig | 3.x | Moteur de templates |
| Symfony Forms | 6.4 | Formulaires |
| Symfony Security | 6.4 | Authentification |
| Asset Mapper | 6.4 | Gestion des assets |

## 📦 Installation

### Prérequis
- PHP 8.1 ou supérieur
- Composer
- MySQL/MariaDB
- Git

### Étapes

```bash
# 1. Cloner le repository
git clone <url-repo>
cd mesvoyages

# 2. Installer les dépendances
composer install

# 3. Configurer l'environnement
cp .env .env.local
# Éditer .env.local et configurer DATABASE_URL

# 4. Créer la base de données
php bin/console doctrine:database:create

# 5. Exécuter les migrations
php bin/console doctrine:migrations:migrate

# 6. Charger les données de test (optionnel)
php bin/console doctrine:fixtures:load

# 7. Lancer le serveur
php bin/console server:run
# Ou avec Symfony CLI
symfony server:start
```

L'application sera accessible à : `http://localhost:8000`

## ⚙️ Configuration

### Variables d'environnement (.env.local)

```env
# Base de données
DATABASE_URL="mysql://user:password@127.0.0.1:3306/mesvoyages"

# Environnement
APP_ENV=dev
APP_DEBUG=true

# Sécurité
ADMIN_USERNAME=admin
ADMIN_PASSWORD=secure_password

# Upload d'images
UPLOAD_DIR=public/uploads
MAX_FILE_SIZE=5242880
```

### Fichiers de configuration
- `config/packages/doctrine.yaml` - Configuration ORM
- `config/packages/security.yaml` - Authentification
- `config/routes.yaml` - Routage
- `config/services.yaml` - Services

## 🚀 Utilisation

### Accéder à l'application

#### Front-office
```
http://localhost:8000/
```

#### Back-office (Admin)
```
http://localhost:8000/admin
```

Identifiants par défaut : voir la configuration

### Flux utilisateur admin

1. Se connecter via `/admin`
2. Naviguer dans le menu :
   - **Voyages** : Lister, ajouter, modifier, supprimer
   - **Destinations** : Gérer les lieux touristiques
   - **Images** : Uploader et organiser les galeries
   - **Tarifs** : Gérer les prix et promotions
3. Se déconnecter via le bouton logout

## 🏗️ Architecture

### Structure du projet

```
mesvoyages/
├── src/
│   ├── Controller/          # Contrôleurs (Web)
│   ├── Entity/              # Classes métier (ORM)
│   ├── Form/                # Types de formulaires
│   ├── Repository/          # Requêtes custom
│   └── Kernel.php
├── templates/               # Templates Twig
├── config/
│   ├── bundles.php
│   ├── packages/            # Configuration des bundles
│   └── routes.yaml
├── migrations/              # Migrations Doctrine
├── public/
│   ├── index.php            # Point d'entrée
│   └── uploads/             # Dossier des uploads
├── tests/                   # Tests PHPUnit
└── composer.json
```

### Entités principales
- **Voyage** : Représente un voyage proposé
- **Destination** : Lieu géographique
- **Image** : Galerie de photos
- **Reservation** : Bookings utilisateurs
- **Avis** : Comments et évaluations

### Pattern MVC
- **Model** : Entités Doctrine + Repositories
- **View** : Templates Twig
- **Controller** : Classes contrôleurs Symfony

## ✅ Tests

```bash
# Lancer tous les tests
php bin/phpunit

# Tests spécifiques
php bin/phpunit tests/Controller/VoyageControllerTest.php

# Avec couverture de code
php bin/phpunit --coverage-html coverage
```

## 🔐 Sécurité

- ✅ Authentification CSRF intégrée
- ✅ Validation des formulaires serveur
- ✅ Contrôle d'accès par role (ROLE_ADMIN)
- ✅ Protection des routes sensibles
- ✅ Validation des uploads (type, taille)
- ✅ Validation des données en base

## 📊 Base de données

### Migrations
```bash
# Créer une migration
php bin/console make:migration

# Appliquer les migrations
php bin/console doctrine:migrations:migrate

# Revenir en arrière
php bin/console doctrine:migrations:migrate prev
```

## 🎨 Assets

```bash
# Compiler les assets
php bin/console asset-map:compile

# En mode watch (développement)
php bin/console asset-map:watch
```

## 📚 Ressources

- [Documentation Symfony](https://symfony.com/doc/current/index.html)
- [Doctrine ORM](https://www.doctrine-project.org/projects/orm.html)
- [Twig Templates](https://twig.symfony.com/)
- [Formulaires Symfony](https://symfony.com/doc/current/forms.html)

## 📝 Licence

Propriété intellectuelle - Usage privé

## 👨‍💻 Support

Pour toute question ou bug report, consultez la section Issues du repository.
