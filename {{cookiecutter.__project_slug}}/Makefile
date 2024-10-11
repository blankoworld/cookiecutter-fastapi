# Variables
VENV_DIR = venv
PYTHON = python3
PIP = $(VENV_DIR)/bin/pip
ACTIVATE = source $(VENV_DIR)/bin/activate

# Cible par défaut
.PHONY: all
all: help

# Affiche les options possibles
.PHONY: help
help:
	@echo "Options disponibles:"
	@echo "  make clean    - Nettoie l'environnement virtuel et les fichiers temporaires"
	@echo "  make deps     - Installe les dépendances nécessaires au développement"
	@echo "  make enter    - Entre dans l'environnement virtuel"
	@echo "  make test     - Exécute les tests avec pytest"
	@echo "  make server   - Démarre le serveur (mode développement)"
	@echo "  make venv     - Crée l'environnement virtuel Python"

# Crée l'environnement virtuel
.PHONY: venv
venv:
	@echo "Création de l'environnement virtuel..."
	$(PYTHON) -m venv $(VENV_DIR)

# Installe les dépendances de développement
.PHONY: deps
deps: $(VENV_DIR)/bin/activate
	@echo "Installation des dépendances de développement..."
	$(PIP) install -r requirements.txt

# Lancer les tests avec pytest
.PHONY: test
test: $(VENV_DIR)/bin/activate
	@echo "Lancement des tests avec pytest..."
	PYTHONPATH=. $(VENV_DIR)/bin/pytest

# Entrez dans l'environnement virtuel
.PHONY: enter
enter: $(VENV_DIR)/bin/activate
	@echo "Activation de l'environnement virtuel. Tapez 'exit' pour quitter."
	$(ACTIVATE); zsh

# Lancer le serveur uvicorn (pour développer)
.PHONY: server
server: $(VENV_DIR)/bin/activate
	@echo "Lancement du serveur uvicorn…"
	@uvicorn app.main:app --reload

# Nettoyage des fichiers temporaires
.PHONY: clean
clean:
	@echo "Nettoyage des fichiers temporaires..."
	find . -name "*.pyc" -exec rm -f {} \;
	find . -name "__pycache__" -exec rm -rf {} \;
	rm -rf $(VENV_DIR)

