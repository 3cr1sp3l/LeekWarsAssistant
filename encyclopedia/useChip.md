useChip(nombre chip, nombre entity) → entier result
====================================================

> Fonctions

Utilise la puce **chip** sur l'entité **entity**, ou sur vous-même si le second paramètre n'est pas fourni.

_Exemple_ : Utiliser la puce [Motivation](/encyclopedia/fr/Motivation) sur moi-même :

    1useChip(CHIP_MOTIVATION)

_Exemple_ : Utiliser la puce [Décharge](/encyclopedia/fr/Décharge) sur un enemi :

    1useChip(CHIP_SHOCK, enemy)

#### Paramètres

* **chip** : Chip à utiliser.
* **entity** : Entité cible, par défaut votre entité.

#### Retour

* **result** : Une valeur strictement supérieure à 0 si l'attaque a été lancée. Les valeurs de retour de useChip sont :
  * [USE\_CRITICAL](/encyclopedia/fr/USE CRITICAL), en cas de coup critique
  * [USE\_SUCCESS](/encyclopedia/fr/USE SUCCESS), en cas de réussite
  * [USE\_FAILED](/encyclopedia/fr/USE FAILED), en cas de d'échec
  * [USE\_INVALID\_TARGET](/encyclopedia/fr/USE INVALID TARGET), si la cible n'existe pas
  * [USE\_NOT\_ENOUGH\_TP](/encyclopedia/fr/USE NOT ENOUGH TP), si votre entité n'a pas assez de TP
  * [USE\_INVALID\_COOLDOWN](/encyclopedia/fr/USE INVALID COOLDOWN), si la puce n'est pas encore utilisable
  * [USE\_INVALID\_POSITION](/encyclopedia/fr/USE INVALID POSITION), si la portée est mauvaise ou la ligne de vue n'est pas dégagée

Les valeurs [USE\_SUCCESS](/encyclopedia/fr/USE SUCCESS) et [USE\_CRITICAL](/encyclopedia/fr/USE CRITICAL) valant respectivement 1 et 2, et les autres 0 ou étant négatives, il est possible de savoir si l'utilisation de la puce a réussi en effectuant le test :

    if (useChip(chip, entity) > 0) {
        // L'utilisation a réussi !
    } else {
        // L'utilisation a échoué !
    }

#### Voir aussi

* [useChipOnCell](/encyclopedia/fr/useChipOnCell) : Utiliser une puce sur une cellule au lieu d'une entité.
* [getCellToUseChip](/encyclopedia/fr/getCellToUseChip) : Déterminer une cellule d'où utiliser une puce.
* [useWeapon](/encyclopedia/fr/useWeapon) : Utiliser une arme.
* [resurrect](/encyclopedia/fr/resurrect) : Utiliser la puce [Résurrection](/encyclopedia/fr/Résurrection).
* [summon](/encyclopedia/fr/summon) : [Invoquer un bulbe](Bulbes) comme [Bulbe Chétif](/encyclopedia/fr/Bulbe_Chétif).
