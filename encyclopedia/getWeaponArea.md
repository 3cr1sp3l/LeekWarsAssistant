# getWeaponArea
> Fonctions

Renvoie le type de zone d'effet de l'arme **weapon**.

#### Paramètres

- **weapon** : L'arme dont le type de zone sera renvoyé.

#### Retour

- **area** : Le type de zone de l'arme **weapon** parmi les constantes AREA_* :
  - [[AREA_POINT]] : zone d'une seule case
  - [[AREA_LASER_LINE]] : ligne d'un laser
  - [[AREA_CIRCLE_1]] : zone circulaire de 3 cases de diamètre
  - [[AREA_CIRCLE_2]] : zone circulaire de 5 cases de diamètre
  - [[AREA_CIRCLE_3]] : zone circulaire de 7 cases de diamètre
  - etc.
