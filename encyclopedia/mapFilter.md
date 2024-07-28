# mapFilter
> Fonctions

Retourne une nouvelle table contenant toutes les valeurs de la table source **map** pour lesquels le prédicat **callback** appliquée a renvoyé *true*.

La fonction **callback** prend les arguments *(valeur, clé, table)* dans cet ordre.

*Exemple* :
```leekscript
var map = [1: '1', 2: '2', 3: '3']
var result = mapFilter(map, function(value, key, map) {
    return key % 2 == 1
}) // [1: '1', 3: '3']
```

#### Paramètres

- **map** : La table.
- **callback** : Le prédicat.

#### Retour

- **filtered** : La table filtrée.

