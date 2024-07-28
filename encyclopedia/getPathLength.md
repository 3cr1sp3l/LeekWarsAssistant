# getPathLength
> Fonctions

Renvoie la longueur du chemin le plus court entre deux cellules **cell1** et **cell2**, en esquivant les obstacles, en ignorant les cellules contenues dans le tableau **ignoredCells**. Cette fonction équivaut à `count(getPath(cell1, cell2, ignoredCells))`.
Si un joueur se situe sur une cellule ignorée, le chemin peut passer sur lui.

La cellule de départ **cell1** n'est jamais comptée dans le résultat. La cellule **cell2** est comptée dans le résultat si et seulement si elle est vide ou ignorée par **ignoredCells**.

Si aucun chemin n'existe entre les deux cellules, **getPathLength** renvoie `null`.

#### Paramètres

- **cell1** : La cellule de départ.
- **cell2** : La cellule d'arrivée.
- **ignoredCells** : Le tableau des cellules à ignorer. Par défaut une liste vide.

#### Retour

- **length**
	- Si un chemin existe : la longueur du chemin entre **cell1** et **cell2**.
	- Si le chemin n'a pas été trouvé : `null`.
