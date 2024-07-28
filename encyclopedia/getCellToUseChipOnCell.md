# getCellToUseChipOnCell
> Fonctions

Détermine une cellule où votre entité pourra utiliser la puce **chip** sur la cellule **cell**.
La cellule renvoyée n'est pas forcément la plus proche.
Si aucune cellule n'est possible, la fonction renvoie `-1`.

#### Paramètres

- **chip** : La puce que l'entité veut pouvoir utiliser.
- **cell** : La cellule cible.
- **ignoredCells** : Tableau de cellules à ignorer. Par défaut un tableau vide.

#### Retour

- **cell** : La cellule d'où la puce pourra être utilisée.
