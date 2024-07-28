# getWeaponPassiveEffects
> Fonctions

Renvoie les effets passifs de l'arme **weapon**.

#### Paramètres

- **weapon** : L'id de l'arme dont les effets passifs seront retournés.

#### Retour

- **passiveEffects** : Un tableau contenant les effets de l'arme **weapon**. Chaque effet est lui-même un tableau de la forme
`[type, min, max, turns, targets, modifiers]`. Ces effets sont les mêmes que ceux renvoyés par [[getWeaponEffects]].
Si il n'y a pas d'effets passifs, une liste vide est renvoyée.
