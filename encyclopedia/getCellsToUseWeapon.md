# getCellsToUseWeapon
> Fonctions

Retourne la liste des cellules à partir desquelles votre entité pourra utiliser l'arme **weapon** sur l'entité **entity**.
Attention, la cellule du lanceur fera partie du résultat si l'arme a un effet sur le lanceur, comme le [[WEAPON_J_LASER]] par exemple.

#### Paramètres

- **weapon** : L'arme à tester. Par défaut votre arme actuellement équipée.
- **entity** : L'entité cible.
- **ignoredCells** : Tableau de cellules à ignorer. Par défaut votre entité est ignorée.

#### Retour

- **cells** : Liste des cellules d'où l'arme pourra être utilisée.
