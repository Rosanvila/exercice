Site disponible à :

http://exercice.sanchezavila.cefim.o2switch.site/


# Exercice Symfony de Fusion de Données via Python et Formulaire de Recherche

## Description
Ce projet Symfony consiste en deux parties principales :
1. Fusion de données provenant d'un fichier `.csv` et d'un fichier `.xml` en un fichier `data.json` à l'aide de Python.
2. Création d'un formulaire responsive avec Bootstrap permettant de faire une recherche via une requête AJAX sur `data.json` et d'afficher les résultats.

Le projet est lancé à l'aide de Laragon et est déployé sur o2switch.

## Prérequis
- PHP 7.4 ou supérieur
- Composer
- Python
- Laragon (pour le développement local)

## Installation

### 1. Cloner le dépôt GitHub
Clonez le dépôt sur votre machine locale :
```
git clone https://github.com/Rosanvila/exercice.git
cd votre-projet
```

### 2. Installer les dépendances PHP
Installez les dépendances PHP via Composer :

```
composer install
```

### 3. Génération du fichier "data.json"
Assurez-vous que Python est installé. Exécutez le script Python pour fusionner les fichiers .csv et .xml :

```
python assets/Python/main.py
```

### 4. Démarrer le serveur local
Lancez le serveur de développement avec Laragon ou un autre logiciel:
```
symfony server:start
```

Ouvrez votre navigateur et accédez à http://localhost:8000 (ou l'URL locale configurée par Laragon).

Utilisation :

Une fois l'application démarrée, vous pourrez utiliser le formulaire responsive pour effectuer des recherches dans le fichier data.json. Les résultats des recherches seront affichés dynamiquement sous le formulaire grâce à des requêtes AJAX.





