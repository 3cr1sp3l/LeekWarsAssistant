# getCellToUseWeapon
> Fonctions

Renvoie une cellule où votre entité pourra utiliser l'arme **weapon** sur l'entité **entity**.
La cellule renvoyée n'est pas forcément la plus proche.
Si aucune cellule n'est possible, la fonction renvoie `-1`.

Exemple pour utiliser le [[Laser]] :
```
var cell = getCellToUseWeapon(WEAPON_LASER, enemy)
moveTowardCell(cell)
useWeapon(enemy)
```

#### Paramètres

- **weapon** : L'arme à tester. Par défaut votre arme actuellement équipée.
- **entity** : L'entité cible.
- **ignoredCells** : Tableau de cellules à ignorer. Par défaut votre entité est ignorée.

#### Retour

- **cell** : La cellule d'où l'arme pourra être utilisée.
