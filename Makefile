# Makefile

# Variables
PYTHON = python3
REQUIREMENTS = requirements.txt

# Cibles principales
all: install-dependencies generate-figures

# Installation des dépendances
install-dependencies:
    @echo "Installation des dépendances..."
    pip install -r $(REQUIREMENTS)

# Génération des figures critiques
generate-critiques-figures:
    $(PYTHON) critiques/graphiques_comparatifs.py
    $(PYTHON) critiques/exemples_concrets.py
    $(PYTHON) critiques/schemas_explicatifs.py

# Génération des illustrations
generate-illustrations:
    $(PYTHON) illustrations-2/arbre_rouge_noir.py
    $(PYTHON) illustrations-2/delta_twins.py
    $(PYTHON) illustrations-2/evolution_tw_uv.py

# Génération des tests de performances
generate-performances-tests:
    $(PYTHON) performances-tests/dependance_logarithmique_tau.py
    $(PYTHON) performances-tests/comparaison_mei_mlei.py
    $(PYTHON) performances-tests/impact_nombre_aretes.py

# Génération de toutes les figures
generate-figures: generate-critiques-figures generate-illustrations generate-performances-tests

# Nettoyage des fichiers générés
clean:
    rm -f critiques/*.png
    rm -f illustrations-2/*.png
    rm -f performances-tests/*.png

# Réinitialisation complète (nettoyage + installation des dépendances)
reset: clean install-dependencies

.PHONY: all install-dependencies generate-critiques-figures generate-illustrations generate-performances-tests generate-figures clean reset