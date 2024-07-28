# getCellToUseWeaponOnCell
> Fonctions

Détermine une cellule où votre entité pourra utiliser l'arme **weapon** sur une cellule **cell**.
La cellule renvoyée n'est pas forcément la plus proche.
Si aucune cellule n'est possible, la fonction renvoie `-1`.

#### Paramètres

- **weapon** : L'arme à tester. Par défaut votre arme actuellement équipée.
- **cell** : La cellule cible.
- **ignoredCells** : Tableau de cellules à ignorer. Par défaut votre entité est ignorée.

#### Retour

- **cell** : La cellule d'où l'arme pourra être utilisée.
