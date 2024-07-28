# getWeaponEffectiveArea
> Fonctions

Renvoie la liste des cellules qui seront affectées si l'arme **weapon** est utilisée sur la cellule **cell** depuis la cellule **from**.
La fonction ne vérifie pas s'il est possible de tirer sur la cellule **cell** ou de se rendre sur la cellule **from**.

#### Paramètres

- **weapon** : L'arme à tester.
- **cell** : La cellule cible.
- **from** : La cellule depuis laquelle l'arme est utilisée.

#### Retour

- **cells** : Le tableau contenant les ids de toutes les cellules qui seront affectées.

#### Voir aussi

- [[getCellToUseWeapon]] : détermine une cellule d'où utiliser une arme.
- [[getWeaponCost]] : récupère le coût d'une arme.
- [[lineOfSight]] : vérifie si la ligne de vue est dégagée entre deux cellules.
- [[canUseWeapon]] et [[canUseWeaponOnCell]] : vérifie si vous pouvez tirer depuis votre cellule actuelle.
- [[getChipEffectiveArea]] : comme getWeaponEffectiveArea mais pour une puce.
