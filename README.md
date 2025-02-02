# Temporal Graph Algorithms

Ce dépôt contient l'implémentation et l'analyse de l'algorithme BuiXuan-Hourcade-Miachon pour la détection des jumeaux temporels ($\Delta$-twins) dans les graphes temporels. Le projet est lié à un rapport académique réalisé dans le cadre du cours DAAR (Données Algorithmiques et Réseaux) à l'Université Sorbonne.

[Lien vers le rapport](https://ottodpc.github.io/Temporal-Graph-Algorithms/index.html)

## Table des matières

- [Temporal Graph Algorithms](#temporal-graph-algorithms)
  - [Table des matières](#table-des-matières)
    - [Introduction](#introduction)
    - [Structure du projet](#structure-du-projet)
    - [Installation et utilisation](#installation-et-utilisation)
      - [**Utilisation avec Makefile**](#utilisation-avec-makefile)
      - [**Utilisation manuelle**](#utilisation-manuelle)
    - [Rapport](#rapport)
    - [Liens utiles](#liens-utiles)

---

### Introduction

Le problème central abordé dans ce projet est l'énumération des paires de "jumeaux temporels" dans les graphes dynamiques. Les jumeaux temporels sont définis comme des paires de sommets qui partagent exactement les mêmes voisins pendant une période donnée. L'algorithme proposé par BuiXuan, Hourcade et Miachon utilise des techniques d'affinage de partition et des arbres rouge-noir pour atteindre une complexité logarithmique en fonction de la longueur de l'historique ($\tau$).

Pour plus de détails sur l'approche théorique et les résultats expérimentaux, veuillez consulter le [rapport complet](https://ottodpc.github.io/Temporal-Graph-Algorithms/index.html).

---

### Structure du projet

Le dépôt est organisé en plusieurs dossiers principaux :

- **`critiques`** : Contient les scripts et les fichiers nécessaires pour générer les figures et les analyses critiques.
- **`illustrations-2`** : Contient les scripts et les fichiers pour créer les illustrations explicatives.
- **`performances-tests`** : Contient les scripts et les fichiers pour exécuter les tests de performance et générer les graphiques correspondants.

---

### Installation et utilisation

#### **Utilisation avec Makefile**

Générer toutes les figures et les tests de performance, **`all`** : Cible principale qui exécute les cibles `install-dependencies` et `generate-figures` :

```bash
make all
```

Pour nettoyer les fichiers générés, **`clean`** : Supprime tous les fichiers PNG générés dans les dossiers `critiques`, `illustrations-2` et `performances-tests` :

```bash
make clean
```

Pour réinstaller les dépendances et nettoyer les fichiers, **`reset`** : Réinitialise complètement le projet en nettoyant les fichiers générés et en réinstallant les dépendances :

```bash
make reset
```

#### **Utilisation manuelle**

Pour utiliser ce projet, suivez ces étapes :

1. **Cloner le dépôt** :

   ```bash
   git clone https://github.com/ottodpc/Temporal-Graph-Algorithms.git
   cd Temporal-Graph-Algorithms
   ```

2. **Installer les dépendances** :

   ```bash
   pip install -r requirements.txt
   ```

3. **Exécuter les scripts** :
   Pour générer les figures et les résultats, exécutez les scripts Python appropriés dans chaque dossier :

   ```bash
   # Dans le dossier critiques
   python graphiques_comparatifs.py
   python exemples_concrets.py
   python schemas_explicatifs.py

   # Dans le dossier illustrations-2
   python arbre_rouge_noir.py
   python delta_twins.py
   python evolution_tw_uv.py

   # Dans le dossier performances-tests
   python dependance_logarithmique_tau.py
   python comparaison_mei_mlei.py
   python impact_nombre_aretes.py
   ```

---

### Rapport

Le rapport complet est disponible sous forme d'une page web statique générée avec GitHub Pages. Vous pouvez y accéder via le lien suivant :

- [Lien vers le rapport](https://ottodpc.github.io/Temporal-Graph-Algorithms/index.html)

Le rapport couvre en détail :

- La définition du problème et la structure de données utilisée.
- Une analyse théorique et une présentation de l'algorithme BuiXuan-Hourcade-Miachon.
- Des tests de performance et des résultats expérimentaux.
- Une discussion critique de l'algorithme et des suggestions d'amélioration.

---

### Liens utiles

- **Article original** : [BuiXuan, Hourcade, Miachon, ICCNA, 2020](https://www-npa.lip6.fr/~buixuan/files/BHM20.pdf)
- **Survey sur la décomposition modulaire** : [Habib et Paul, 2010](https://www.irif.fr/~habib/Documents/HP10.pdf)
- **Cours MPRI sur l'affinage de partition** : [Michel Habib, 2013](https://www.irif.fr/~habib//Documents/cours_3-2013.pdf)
