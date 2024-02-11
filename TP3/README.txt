
# Projet de Moteur de Recherche

Ce projet implémente un système de recherche simple qui lit une requête utilisateur, la traite, filtre les documents basés sur cette requête, les classe, et enfin retourne les résultats sous forme de fichier JSON.

## Dépendances

- Python 3.6+
- NLTK (Natural Language Toolkit)

## Installation des Dépendances

Avant de lancer le projet, vous devez installer NLTK et télécharger les données nécessaires. Exécutez les commandes suivantes :

```bash
pip install nltk
python -m nltk.downloader punkt
python -m nltk.downloader stopwords
```

## Structure du Projet

Le projet est structuré comme suit :

```
search_engine/
│
├── main.py             # Point d'entrée du programme.
├── query_processor.py  # Traite la requête utilisateur.
├── document_filter.py  # Filtre les documents basés sur la requête.
├── ranking.py          # Classe les documents filtrés.
├── results_writer.py   # Écrit les résultats dans un fichier JSON.
└── README.md           # Ce fichier.
```

## Exécution

Pour lancer le projet, naviguez dans le répertoire du projet et exécutez le script `main.py` :

```bash
cd chemin/vers/search_engine
python main.py
```

Vous serez invité à entrer une requête. Après l'entrée de la requête, le système traitera la requête, filtrera et classera les documents, puis écrira les résultats dans `results.json`.

## Explication du Code

### main.py

Ce script est le point d'entrée du programme. Il orchestre le processus de recherche en appelant les fonctions définies dans les autres scripts.

### query_processor.py

Contient la fonction `process_query` qui pré-traite la requête de l'utilisateur (tokenisation, mise en minuscules, suppression des stopwords).

### document_filter.py

Implémente la fonction `filter_documents` qui filtre les documents en fonction de la présence des tokens de la requête. Supporte les modes de filtrage ET et OU.

### ranking.py

Contient la fonction `rank_documents` qui classe les documents filtrés en fonction du nombre de tokens correspondants et éventuellement d'autres critères.

### results_writer.py

Gère l'écriture des résultats filtrés et classés dans un fichier `results.json`, incluant le titre, l'URL, le nombre total de documents dans l'index, et le nombre de documents correspondant à la requête.


