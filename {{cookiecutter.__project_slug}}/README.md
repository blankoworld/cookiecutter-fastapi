# {{ cookiecutter.__project_slug }}

API utilisant FastAPI pour proposer des {{ cookiecutter.__project_slug }}.

# Pré-requis

* make
* python3

# Données

Les données sont situées dans le fichier **data.json** situé dans le dossier `data`.

Elles sont au format CSV. Il suffit d'ouvrir cela avec un tableur.

# Utilisation

Créez un environnement virtuel Python, entrez dedans puis installez les dépendances&nbsp;: 

```bash
make venv && make enter
make deps
```

# Lancement du serveur

À chaque fois il faudra entrer dans l'environnement virtuel via la commande `make enter`.

Puis faites&nbsp;: 

```bash
make server
```

pour lancer le serveur uvicorn.

# Documentation

Une fois le serveur lancé, allez sur l'adresse suivante&nbsp;: http://localhost:8000/docs

Vous trouverez - normalement - assez de doc pour comprendre les routes disponibles

# Tests

Entrez dans l'environnement virtuel avec la commande `make enter` puis faites&nbsp;:

```bash
make test
```

# Licence

Ce logiciel est sous licence EUPL v1.2 (Cf. le fichier LICENSE).

This software is available under the terms of EUPL licence (Cf. LICENCE file).
