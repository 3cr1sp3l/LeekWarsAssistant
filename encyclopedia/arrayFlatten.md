# arrayFlatten
> Fonctions

Retourne un nouveau tableau contenant tous les éléments du tableau source. Tous les éléments contenus dans un sous tableau sont extraits dans le nouveau tableau.

#### Paramètres

- **array** : Tableau d'origine.
- **depth** : Profondeur des sous-tableaux. Par défaut 1.

#### Retour

- **newArray** : Nouveau tableau.

#### Exemples

```
var tableau = [1, 2, [3, 4], 5, [6]]
debug(arrayFlatten(tableau)) // [1, 2, 3, 4, 5, 6]
debug(arrayFlatten([0, [1], [ [2] ], [ [ [3] ] ] ], 2)); // [0, 1, 2, [3]]
```