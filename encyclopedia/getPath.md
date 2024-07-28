# getPath
> Fonctions

Renvoie le plus court chemin en évitant les obstacles entre deux cellules **cell1** et **cell2**, si celui-ci existe, en ignorant les cellules contenues dans le tableau **ignoredCells**.

La cellule de départ **cell1** ne fait jamais partie du chemin résultant. La cellule **cell2** fait partie du chemin résultant si et seulement si elle est vide.

Si aucun chemin n'existe entre les deux cellules, **getPath** renvoie `null`.

Attention, il est possible que `getPath(cell1, cell2) != getPath(cell2, cell1)`.
	
#### Paramètres

- **start** : La cellule de départ.
- **end** : La cellule d'arrivée.
- **ignoredCells** : Le tableau des cellules à ignorer. Par défaut une liste vide.

#### Retour

- **path**
	- Si un chemin existe : un tableau contenant les cellules constituant le chemin entre les deux cellules
	- Si le chemin n'a pas été trouvé : `null`.
	
#### Exemples

```
var path = getPath(getCell(), getCell(enemy))
mark(path, COLOR_RED) // Affiche le chemin entre moi et l'ennemi
```
	
#### Voir aussi

- [[getCellDistance]]
- [[getPathLength]]
