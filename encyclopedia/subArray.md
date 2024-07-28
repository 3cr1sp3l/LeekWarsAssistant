# subArray
> Fonctions

Retourne un sous-tableau de <b>array</b> commençant à la position <b>start</b> et finissant à la position <b>end</b>.

#### Paramètres

- **array** : Tableau source.
- **start** : Position de départ.
- **end** : Position de fin.

#### Retour

- **newArray** : Le sous-tableau.

#### Exemples

```
var tableau = [0, 1, 2, 3, 4, 5]
debug(subArray(tableau, 2, 4)) // [2, 3, 4]
```

Avec un tableau associatif :
```
var tableauAssoc = [2: 0, 3: 1, 4: 2, 5: 3, 6: 4, 7: 5]
debug(subArray(tableauAssoc, 2, 4)) // [2, 3, 4] et non [0, 1, 2]
```