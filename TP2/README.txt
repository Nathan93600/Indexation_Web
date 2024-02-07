Dépendances
Python 3.6+
NLTK
BeautifulSoup (non utilisé directement dans les exemples fournis, mais inclus si le scraping ou le traitement HTML est nécessaire)
Pour installer NLTK et ses dépendances, exécutez :

pip install nltk

Ensuite, téléchargez les données nécessaires de NLTK en exécutant Python et en tapant :

import nltk
nltk.download('punkt')
nltk.download('stopwords')

Structure des Fichiers
main.py : Point d'entrée pour exécuter le projet.

- index_builder.py : Contient les fonctions pour construire les différents types d'indexes.
- data_processing.py : Fonctions pour le nettoyage et la tokenisation du texte.
- statistics.py : Fonction pour générer des statistiques sur les données.
- urls.json : Fichier JSON contenant les données web extraites.

Instructions d'Exécution

Pour exécuter le projet, naviguez dans le répertoire contenant main.py et exécutez :

python main.py

Cela lancera le processus de génération de statistiques et de construction des indexes à partir des données fournies dans urls.json.

Fonctionnalités

Génération de Statistiques
La fonction generate_statistics dans statistics.py calcule et affiche les statistiques de base sur les titres des documents, incluant le nombre total de documents, la longueur totale des titres, et la longueur moyenne des titres.

Construction de l'Index Non Positionnel
La fonction build_non_positional_index dans index_builder.py crée un index non positionnel qui associe chaque token unique à une liste d'identifiants de documents (indices dans le fichier JSON) où le token apparaît.

Construction de l'Index avec Stemming
La fonction build_stemmed_index applique un stemming aux tokens avant de construire l'index non positionnel, permettant une recherche plus flexible sur les variantes d'un même mot.

Construction de l'Index Positionnel
La fonction build_positional_index crée un index positionnel qui, pour chaque token, stocke une liste de documents et, pour chaque document, les positions spécifiques du token dans le titre.