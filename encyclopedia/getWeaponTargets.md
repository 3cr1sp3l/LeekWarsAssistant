# getWeaponTargets
> Fonctions

Renvoie les entités qui seront affectées si l'arme **weapon** est utilisée sur la cellule **cell**.
Attention, le lanceur fera partie du résultat si l'arme a un effet sur son lanceur, comme le [[WEAPON_J_LASER]] par exemple.

#### Paramètres

- **weapon** : L'arme à tester.
- **cell** : La cellule cible.

#### Retour

- **targets** : Le tableau contenant les ids de tous les entités qui seront affectées.
