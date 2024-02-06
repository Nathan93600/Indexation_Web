README.md
Comment exécuter le programme:
Pour exécuter le programme, suivez ces étapes simples:

Assurez-vous d'avoir Python installé sur votre système.

Installation et Configuration :

Dépendances : Assurez-vous d'avoir Python installé sur votre système. Les bibliothèques nécessaires incluent urllib, BeautifulSoup4, et sqlite3. Pour installer BeautifulSoup, exécutez pip install beautifulsoup4.

Exécution : Téléchargez le script du crawler. Ouvrez un terminal, naviguez jusqu'au dossier contenant le script et exécutez-le avec python main.py.

Fonctionnalités des Fonctions :

create_database(): Initialise la base de données SQLite.
insert_page(url, title): Enregistre l'URL et le titre de chaque page dans la base de données.
get_links(url): Récupère et analyse les liens d'une page web spécifiée.
can_fetch(url, user_agent='*'): Vérifie si l'URL est autorisée pour le crawling selon le fichier robots.txt.
crawl(url, crawled_urls, to_crawl, depth=0, max_depth=1): Fonction principale de crawling qui gère la récursivité et le respect des règles de politesse.
main(start_url): Point d'entrée du programme, initialise les structures de données et lance le processus de crawling.
Utilisation :

Lancez le script en spécifiant une URL de départ. Le crawler va parcourir les pages web, enregistrant les URLs et les titres dans une base de données et respectant les directives de robots.txt., exécutez main.py avec une URL de départ. Le crawler commencera à partir de cette URL, en suivant les liens tout en respectant les règles établies.