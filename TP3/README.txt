
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

Vous serez invité à entrer une requête et à choisir le mode de filtrage (AND/OR). Après l'entrée de la requête, le système traitera la requête, filtrera et classera les documents, puis écrira les résultats dans `results.json`.

## Exemple d'Exécution

```
Entrez votre requête : technology document
Choisissez le mode de filtrage (AND/OR): AND
```

### Résultats Attendus

Les résultats de votre requête seront écrits dans `results.json`, contenant les documents pertinents classés selon votre requête.

## Format des Fichiers de Données

### documents.json

```json
[
  {
    "id": 1,
    "content": "This is a sample document about technology.",
    "title": "Technology News"
  },
  {
    "id": 2,
    "content": "Another document related to health.",
    "title": "Health Update"
  }
]
```

### index.json

```json
{
  "technology": {"1": {"count": 1}},
  "sample": {"1": {"count": 1}},
  "document": {"1": {"count": 1}, "2": {"count": 1}},
  "health": {"2": {"count": 1}}
}
```

