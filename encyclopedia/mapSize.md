# mapSize
> Fonctions

Renvoie le nombre d'entrées dans la table **map**.

#### Paramètres

- **map** : La table.

#### Retour

- **size** : La taille de **map**.

#### Exemples

Table vide :
```
mapSize([:]) // 0
```

Table avec 3 entrées :
```
var table = ['a': 1, 'b': 2, 'c': 3]
mapSize(table) // 3
```

#### Voir aussi

- [[count]] : Longueur d'une liste.
- [[length]] : Longueur d'une chaîne de caractères.