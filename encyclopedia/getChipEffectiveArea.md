# getChipEffectiveArea
> Fonctions

Renvoie la liste des cellules qui seront affectés si la puce **chip** est utilisée sur la cellule **cell** depuis une cellule **from**.
La fonction ne vérifie pas s'il est possible d'utiliser la puce sur la cellule **cell** ou de se rendre sur la cellule **from**.

#### Paramètres

- **chip** : La puce à tester.
- **cell** : La cellule cible.
- **from** : La cellule depuis laquelle la puce est utilisée.

#### Retour

- **cells** : Le tableau contenant les ids de toutes les cellules qui seront affectés.

#### Voir aussi

- [[getCellToUseChip]] : détermine une cellule d'où utiliser une puce.
- [[getChipCost]] : récupère le coût d'une puce.
- [[lineOfSight]] : vérifie si la ligne de vue est dégagée entre deux cellules.
- [[canUseChip]] et [[canUseChipOnCell]] : vérifie si vous pouvez utiliser la puce depuis votre cellule actuelle.
- [[getWeaponEffectiveArea]] : comme getChipEffectiveArea mais pour une arme.
