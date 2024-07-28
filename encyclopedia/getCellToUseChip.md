# getCellToUseChip
> Fonctions

Renvoie une cellule où votre entité pourra utiliser la puce **chip** sur l'entité **entity**.
La cellule renvoyée n'est pas forcément la plus proche.
Si aucune cellule n'est possible, la fonction renvoie `-1`.

Exemple pour lancer un [[Rocher]] :
```
var cell = getCellToUseChip(CHIP_ROCK, enemy)
moveTowardCell(cell)
useChip(CHIP_ROCK, enemy)
```

#### Paramètres

- **chip** : La puce que l'entité veut pouvoir utiliser.
- **entity** : L'entité cible.
- **ignoredCells** : Tableau de cellules à ignorer. Par défaut un tableau vide.

#### Retour

- **cell** : La cellule d'où la puce pourra être utilisée.
