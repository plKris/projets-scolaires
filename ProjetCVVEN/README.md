# ProjetCVVEN

![PHP](https://img.shields.io/badge/PHP-8.1%2B-777BB4?logo=php&logoColor=white)
![CodeIgniter](https://img.shields.io/badge/CodeIgniter-4-EF4223?logo=codeigniter&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-DB-4479A1?logo=mysql&logoColor=white)
![Licence](https://img.shields.io/badge/Licence-MIT-green)

Application web de gestion de reservations hotelieres, developpee avec CodeIgniter 4.

## Sommaire

- [Apercu](#apercu)
- [Fonctionnalites](#fonctionnalites)
- [Stack technique](#stack-technique)
- [Installation](#installation)
- [Configuration](#configuration)
- [Base de donnees](#base-de-donnees)
- [Lancement en local](#lancement-en-local)
- [Tests](#tests)
- [Structure du projet](#structure-du-projet)
- [Securite et bonnes pratiques](#securite-et-bonnes-pratiques)
- [Deploiement](#deploiement)
- [Licence](#licence)

## Apercu

ProjetCVVEN permet de:

- gerer des utilisateurs (authentification, profils, roles)
- consulter les chambres disponibles
- creer et suivre des reservations
- administrer les chambres et reservations depuis une interface dediee

Le projet est base sur CodeIgniter 4 et utilise MySQL/MariaDB.

## Fonctionnalites

- connexion et inscription utilisateur
- gestion de session et controle d'acces par role
- espace utilisateur (profil, parametres)
- reservations utilisateur (creation, consultation, annulation)
- administration des chambres
- administration des reservations (suivi des statuts)
- interface responsive (Bootstrap + Font Awesome)

## Stack technique

- PHP 8.1+
- CodeIgniter 4
- MySQL ou MariaDB
- Bootstrap 5
- Font Awesome
- PHPUnit 10

## Installation

1. Cloner le projet.
2. Se placer dans le dossier racine.
3. Installer les dependances Composer.

```bash
composer install
```

Si Composer n'est pas installe globalement:

```bash
php composer.phar install
```

## Configuration

1. Copier le fichier `env` en `.env`.
2. Configurer la base URL et la base de donnees dans `.env`.
3. Verifier les parametres de connexion SQL.

Exemple de configuration DB:

```dotenv
database.default.hostname = 127.0.0.1
database.default.database = ProjetCVVEN
database.default.username = root
database.default.password =
database.default.DBDriver = MySQLi
database.default.port = 3306
```

## Base de donnees

Le script SQL principal est disponible dans:

- `app/Database/Structure/structuredatabase.sql`

Importer ce fichier dans votre serveur MySQL/MariaDB avant le premier lancement.

### Installation base de donnees (premiere fois)

1. Creer une base vide (exemple: `ProjetCVVEN`).
2. Importer le dump SQL fourni.
3. Verifier que votre `.env` pointe bien vers cette base.

Exemple de commande d'import:

```bash
mysql -u root -p ProjetCVVEN < app/Database/Structure/structuredatabase.sql
```

Si la base n'existe pas encore:

```bash
mysql -u root -p -e "CREATE DATABASE ProjetCVVEN CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;"
mysql -u root -p ProjetCVVEN < app/Database/Structure/structuredatabase.sql
```

Une fois l'import termine, vous pouvez lancer l'application normalement.

## Lancement en local

```bash
php spark serve
```

Application accessible sur:

- `http://localhost:8080`

## Comptes de demonstration

Selon le jeu de donnees importe, vous pouvez disposer de comptes de test.
Pensez a modifier les mots de passe en environnement reel.

## Tests

Executer la suite de tests:

```bash
php composer.phar test
```

Ou:

```bash
vendor/bin/phpunit
```

## Structure du projet

- `app/Controllers` logique des routes et actions
- `app/Models` acces et manipulation des donnees
- `app/Views` interfaces utilisateur
- `app/Config` configuration application (routes, DB, etc.)
- `app/Database` scripts SQL, migrations, seeds
- `public` point d'entree web
- `writable` cache, sessions, logs
- `tests` tests unitaires et d'integration

## Securite et bonnes pratiques

- ne jamais versionner un vrai fichier `.env`
- utiliser un mot de passe fort pour la base de donnees
- desactiver le mode debug en production
- appliquer HTTPS en production
- limiter les comptes admin et changer les identifiants par defaut

## Commandes utiles

```bash
php spark routes
php spark migrate
php spark db:seed NomDuSeeder
php spark cache:clear
php spark logs:clear
```

## Deploiement

- configurer le serveur web pour pointer vers le dossier `public`
- verifier les permissions d'ecriture sur `writable`
- fournir un `.env` de production
- activer les logs applicatifs

## Licence

Ce projet suit la licence MIT (voir le fichier `LICENSE`).

## Auteur

ProjetCVVEN - projet academique / gestion hoteliere.
