README.md
Comment exécuter le programme:
Pour exécuter le programme, suivez ces étapes simples:

Assurez-vous d'avoir Python installé sur votre système.

Téléchargez le fichier main.py.

Ouvrez une fenêtre de terminal.

Accédez au répertoire où se trouve le fichier main.py.

Exécutez la commande suivante:


python main.py

Cette commande lancera le crawler qui explorera le site web à partir de l'URL de base fournie.

Description du fonctionnement du crawler:
Le crawler est un programme en Python conçu pour explorer un site web de manière méthodique. Voici comment il fonctionne:

Initialisation:

Le crawler commence par initialiser ses paramètres, notamment l'URL de base, les ensembles pour suivre les URLs visitées et échouées, un objet RobotFileParser pour respecter les règles de robots.txt, et une liste de domaines bloqués.
Fonction can_fetch:

Avant de visiter une URL, le crawler utilise cette fonction pour vérifier si les règles du fichier robots.txt autorisent l'accès à cette URL. Il exclut également les URLs avec des domaines bloqués.
Fonction is_html:

Cette fonction vérifie si le contenu de la réponse HTTP est de type HTML. Cela garantit que le crawler ne traite que des pages HTML.
Fonction fetch_links:

Pendant l'exploration d'une page, cette fonction analyse le contenu HTML pour extraire jusqu'à 5 liens valides qui n'ont pas encore été visités ni échoués.
Fonction crawl:

Le cœur du crawler, cette fonction commence par l'URL de base et explore de nouvelles pages en respectant les règles de politesse définies. Elle s'arrête lorsqu'elle a visité 50 URLs ou si elle ne trouve plus de liens à explorer.
Pour chaque URL visitée avec succès, le crawler l'ajoute au fichier crawled_webpages.txt.
Il gère également les erreurs d'URL, y compris les erreurs de déconnexion distante.
Les librairies utilisées et leur rôle:
time: Utilisé pour mesurer le temps d'exécution et introduire des délais.
urllib.request: Employé pour effectuer des requêtes HTTP.
urllib.parse: Utile pour manipuler les URLs.
urllib.robotparser: Nécessaire pour analyser le fichier robots.txt du site et respecter ses règles.
BeautifulSoup: Incontournable pour extraire des informations HTML de manière structurée