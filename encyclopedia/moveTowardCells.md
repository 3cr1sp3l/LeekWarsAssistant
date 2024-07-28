# moveTowardCells
> Fonctions

Rapproche votre entité de la première cellule d'un ensemble de cellules **cells**, en utilisant au maximum **mp** points de mouvement.

Si, parmi l'ensemble de cellules **cells**, il y a une cellule à portée de déplacement et qui rapproche votre entité de la première cellule de **cells**, alors l'entité va se déplacer sur la cellule de **cells** la plus proche de la case de départ de l'entité.

Si, parmi l'ensemble de cellules **cells**, il n'y a aucune cellule à portée de déplacement et qui rapproche votre entité de la première cellule de **cells**, alors l'entité va se rapprocher de la première cellule de l'ensemble de cellules **cells** en utilisant au maximum **mp** points de mouvement.

#### Paramètres

- **cells** : Le tableau contenant la cellule vers laquelle votre entité doit se rapprocher, et les cellules sur lesquelles votre entité va se déplacer si elles sont à portée.
- **mp** : Le nombre maximum de PM à utiliser. Par défaut, pas de limite.

#### Retour

- **mp** : Le nombre de points de mouvements utilisés.
