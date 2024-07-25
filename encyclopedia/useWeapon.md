useWeapon(nombre entity) → entier result
========================================

> Fonctions

Utilise l'arme sélectionnée sur l'entité **entity**.

_Exemple_ : utiliser le pistolet sur l'ennemi le plus proche :

    var enemy = getNearestEnemy()
    setWeapon(WEAPON_PISTOL)
    useWeapon(enemy)

#### Paramètres

*   **entity** : Entité ciblée.

#### Retour

*   **result** : Une valeur strictement supérieure à 0 si l'attaque a été lancée. Les valeurs de retour de useWeapon sont :
    *   [USE\_CRITICAL](/encyclopedia/fr/USE CRITICAL), en cas de coup critique
    *   [USE\_SUCCESS](/encyclopedia/fr/USE SUCCESS), en cas de réussite
    *   [USE\_FAILED](/encyclopedia/fr/USE FAILED), en cas de d'échec
    *   [USE\_INVALID\_TARGET](/encyclopedia/fr/USE INVALID TARGET), si la cible n'existe pas
    *   [USE\_NOT\_ENOUGH\_TP](/encyclopedia/fr/USE NOT ENOUGH TP), si votre entité n'a pas assez de TP
    *   [USE\_INVALID\_POSITION](/encyclopedia/fr/USE INVALID POSITION), si la portée est mauvaise ou la ligne de vue n'est pas dégagée

Les valeurs [USE\_SUCCESS](/encyclopedia/fr/USE SUCCESS) et [USE\_CRITICAL](/encyclopedia/fr/USE CRITICAL) valant respectivement 1 et 2, et les autres 0 ou étant négatives, il est possible de savoir si l'utilisation de l'arme a réussi en effectuant le test :

    if (useWeapon(entity) > 0) {
        // L'utilisation a réussi !
    } else {
        // L'utilisation a échoué !
    }

#### Voir aussi

*   [setWeapon](/encyclopedia/fr/setWeapon) : équipe une arme.
*   [useWeaponOnCell](/encyclopedia/fr/useWeaponOnCell) : utiliser une arme sur une cellule au lieu d'une entité.
*   [getCellToUseWeapon](/encyclopedia/fr/getCellToUseWeapon) : détermine une cellule d'où utiliser une arme.
*   [useChip](/encyclopedia/fr/useChip) : utiliser une puce.