# Stack Flask MySQL

## Présentation
Le but de ce mini-projet est de créer une application python avec la librairie HTTP Flask, une base de donnée MySQL
et de la dockerisé avec docker-compose.

## Lancer le projet:
Pour lancer le projet:
```shell
docker compose up
```

Une fois que le projet est construit, pour chaque changement vous devez relancer le build de l'applicaton:
```
docker compose build app
```
puis relancer le docker compose.

## Exercice 1: Hello world
Ecrire un script python avec flask qui definie la route "/hello" qui retourne le message "Hello world"

## Exercice 2: API CRUD
Faire une API pour récupéré des données sur le mongo.

## Exercice 3: API scrap:
Créer une api qui permet de faire du scrapping.
Elle prend une requete de la forme:
/scrap?url=....
Le query param "url" permet de donner le site cible.
il doit retourner un object avec des données sur la pages:
- le mot le plus cité,
- la liste des autre url dans la page
- le nombre de balises dans la page (nombre de balise dv, a, p, ...)

## Exercice 4: API scrap marmiton
Modifier l'API pour qu'elle puisse scrap une page de recette sur le site marmiton.org
et retourne les informations nutritionnel de la recette (nombre de calories, nutriscore des ingradient)

Pour cela vous pouvez utiliser les données du site openFoodFact.

