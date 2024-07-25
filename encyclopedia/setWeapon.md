setWeapon(nombre weapon)
========================

> Fonctions

Équipe l'arme **weapon** sur votre entité.

Cette fonction coûte **1PT** !

Pour éviter de rééquiper la même arme et de perdre ce PT à chaque tour, il est possible d'utiliser une condition

    if

comme ceci :

    if (getWeapon() != WEAPON_PISTOL) {
        setWeapon(WEAPON_PISTOL)
    }

#### Paramètres

*   **weapon** : Id de l'arme à équiper.