# arrayChunk
> Fonctions

Cette fonction est disponible à partir du LeekScript 4 et plus.
Découpe la liste **array** en sous-listes de taille **chunkSize** maximum et renvoie la liste de ces sous-listes.
La dernière sous-liste peut contenir moins de **chunkSize** élements.

#### Paramètres

- **array** : La liste à découper.
- **chunkSize** : La taille maximale des sous-listes.

#### Retour

- **chunks** : Les sous-listes produites.

#### Exemple

```
var liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
var sous_listes = arrayChunk(liste, 4)
debug(sous_listes) // [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10] ]
```