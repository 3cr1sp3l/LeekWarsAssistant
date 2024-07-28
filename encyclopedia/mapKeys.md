# mapKeys
> Fonctions

Renvoie une liste contenant toutes les clés de la table **map**.

#### Paramètres

- **map** : La table.

#### Retour

- **keys** : Les clés de la table.

#### Exemples

```
mapKeys([:]) // []
```

```
var table = [1: 'a', 2: 'b': 3: 'c']
mapKeys(table) // [1, 2, 3]
```

```
var table = ['a': 1, 'b': 2, 'c': 3]
mapKeys(table) // ["a", "b", "c"]
```

#### Voir aussi

- [[mapValues]]