# I - Les bases de données

Les project doit traiter toutes sortes de donnée, et ainsi répondre a des besoins très différents.
Nous faisons donc appelles à des paradigmes adaptés a ces derniers.

Les deux bases de données suivantes seront destinées a voir leur volume de données augmenter rapidement, nous avons donc choisi des techno dites "**clustérisées**", et permettent donc une augmentation du volume de stockage facile avec une bonne continuité de service. Deplus elles proposent de la redondence de données.

## MongoDB

**MongoDB** est une base de données utilisant le paradigme “Document Oriented”. Elle permet de stocker des documents sous format *JSON* donc purement textuels. Cette base nous permettra de stocker les tweets, news, ainsi que les infos des films concernés. Ce paradigme étant particulièrement flexible il nous permettera aussi de stocker le fruit de nos traitement *machine learning* (ex: analyse de sentiments).

## HDFS

Le ***Hadoop Distributed File System*** n’est pas vraiment une base de données comme on peut l’entendre, mais pourrait plus s’apparenter à un dossier partagé de Windows. Elle prend place dans notre projet pour stocker les affiches des films : dossier partagé permettant le stockage d’images tandis que des bases de données classiques (*SQL*, *Mongodb*, etc…), ne peuvent pas stocker directement des fichiers, mais les convertissent en chaîne de caractères.

Dans notre cas nous l'utiliserons pour stocker les posters des films, pour ensuite les proposer au client mais aussi, pour faire du traitement d'image dans notre *pipeline michine-learning*.

## Redis

Une base de données clé-valeur légère qui nous permet de stocker les clefs API de facon sécurisé, donc ne pas les avoir en dur dans le repo. git.

# II - Récupération des données

## 1. Les sources

La partie la plus critique des projets *big-data* est la récupération de données de qualité (de facon économique si possible). Dans notre cas, pour avoir un volume conséquent de donnée nous utilisons des sources diverses et variées, autant dans leur conception que dans leur modèle économique.
Étant en projet universitaire nous nous sommes limités à des données gratuites et donc limitées.

### a. Twitter

Plus que toutes autres sources d'informations, les données sociales révèlent ce qui compte le plus pour les gens et Twitter est devenu avec le temps un incontournable atout pour toute personne voulant connaître l’opinion publique.

Comme expliqué précédemment l’objectif est de récupérer les tweets parlant d’un film puis de les analyser pour en sortir une note témoignant de sa popularité, ou non. Pour se faire, Python nous a encore une fois émerveillé de par sa communauté, en nous proposant une librairie, Tweepy, proposant en quelques lignes de récupérer toutes les données voulues.

Nous restons cependant restreints par le compte développeur de Twitter et sa limite de mille tweets par minute.

Une fois les tweets organisés et analysés, ils sont envoyés dans une base de données elasticsearch.

### b. TMDB

TMDB est une base de données communautaire (reprenant le concept de Wikipédia) contenant tous les films sortis, leurs noms, leurs posters et bien d’autres informations non- essentielles à notre projet. Encore une fois Python nous régale avec des librairies prêtes à l’emploi : grâce TmdbSimple nous pouvons facilement récupérer les posters des dernières sorties pour ensuite les proposer à nos utilisateurs. Il n’y a, à ce jour, aucun quota sur le nombre de requêtes pour l’API TMDB.

### c. Flux RSS

Les Flux RSS viennent de deux sources différentes :

- Allociné : Site français très connu. Nous avons utilisé deux des flux proposés par ce site, à savoir "À l'affiche" et “Cette semaine” comme catégorie pour n’avoir que des actualités sur le monde du cinéma.
- Screenrant : une plateforme anglophone qui propose elle aussi un flux RSS.

La complexité dans la gestion des flux RSS était la transformation des données afin de les normalisées d’un flux à l’autre. Nous voulions pouvoir par la suite traiter les données de façon simple, et cela nécessitait qu’un tri et une manipulation des données soit réalisé en amont.

Par exemple, Screenrant renvoyait du texte directement tandis que Allociné nous fournissait du code HTML. Il a donc fallu analyser ce dernier et le découper pour prendre uniquement les parties qui nous intéressent.

Heureusement pour nous, le retour des flux RSS étaient tous dans le même format (JSON), donc nous avons pu les traiter de la même façon.

## 2. Les scripts

### a. Twitter

Il est question pour nous de détailler les différentes méthodes et leurs explications.

Nous débutons en définissant la classe TwitterClient qui compte 6 méthodes à savoir :

- Constructeur : init () est une méthode qui initialise un objet instancié de la classe twitter avec pour paramètre db(la base de données), sentimentModule( ), supported_languages( la langue anglaise par défaut).
- InsertDb() : C’est une méthode qui prend en paramètre une liste dont l’action est de faire une insertion dans la base de données des champs suivants : la date, le texte, nombre de retweet et nombre de
- DeleteDb() : C’est une méthode qui vide la base de données ayant pour l’index ‘’twitter’’
- GetTweets() : C’est une méthode qui prend en paramètre le mot clé à rechercher et le nombre de max de tweet à récupérer. Il a pour action de récupérer les tweets à l'aide d’un mot clé et renvoie une liste de dictionnaire.
- PushNewTweet() : C’est une méthode qui appelle la méthode insertDb() pour insérer dans la base de données les tweets qu’on récupère.
- SetSupportedLanguages() : Un setter pour la propriété supported_language de la

### b. TMDB

Les imports :

- Tmdbsimple : un wrapper python pour l’API TMDB
- Requests : sert à réaliser des requêtes HTTP
- Os : qui permet d'interagir avec le système d’exploitation
- Alphabet_detector : qui permet de savoir dans quel alphabet est écrit la chaîne de caractères
- Sys : qui retourne des informations sur le système d’exploitation

Nous avons ensuite créé une Classe python TMDBCLient avec :

- Un constructeur.
- Une méthode affichant dans la console une liste de films sous forme de menu et récupère le choix de l’utilisateur.
- Une méthode permettant la récupération de l’affiche du film. Aussi, au sein de cette méthode, nous vérifions si le dossier cible de stockage des images existe, si non, nous le créons.
- Une méthode permettant la suppression du dossier créé par la méthode précédente.

### c. Flux RSS

Les imports :

- error : Il sert à la gestion des erreurs dans lors des requêtes HTTP
- Bs4 : BeautifulSoup qui nous sert à parser le HTML renvoyé par certains flux RSS
- Feedparser : C’est un module qui nous sert à parser en json les pages html du flux RSS
- Ssl : nous sert pour une gestion des certificats, dans certains cas, lors des requêtes nous avions une erreur de

Nous avons ensuite créé une Classe python RSSClient avec :

- Un constructeur.
- Une méthode pour récupérer les feeds. Ici on peut voir la gestion des erreurs de certificats grâce au module Cette méthode permet la récupération du flux RSS et

le parse en Json.

- Un setter pour l’attribut urls de la
- Une méthode pour insérer les données en base de données. Ici, pour chaque article présent dans le flux RSS, une fois le contenu parsé si besoin, l’étude de la polarité va être réalisée avant de réaliser l’insertion en base de données.
- Une méthode qui va vider les indexes de la base de données.

Les indexes sont les clefs du dictionnaire des urls comme l’exemple ci-dessous :

```py
rss_feed = RSSClient(mongodb_client, {
    'allocinesemaine': 'http://rss.allocine.fr/ac/cine/cettesemaine',
    'allocineaffiche': 'http://rss.allocine.fr/ac/cine/alaffiche',
    'screenrant': 'https://screenrant.com/feed/',
})
```

- Une méthode permettant de tester si l’article existe déjà en base de données.
- Une méthode permettant de récupérer le contenu des balises <p></p> du HTML.
- Une méthode qui permet de récupérer le flux RSS et retourne un tableau de tous les articles non présents en base de données.
- Une dernière méthode qui permet l’insertion en base de données du tableau d’article renvoyé par la méthode précédente.

