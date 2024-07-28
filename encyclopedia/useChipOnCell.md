# useChipOnCell
> Fonctions

Utilise la puce **chip** sur la cellule **cell**.

#### Paramètres

- **chip** : Chip à utiliser.
- **cell** : Cellule cible.

#### Retour

- **result** : Une valeur strictement supérieure à 0 si l'attaque a été lancée. Les valeurs de retour de useChipOnCell sont :
	- [[USE_CRITICAL]], en cas de coup critique
	- [[USE_SUCCESS]], en cas de réussite
	- [[USE_FAILED]], en cas de d'échec
	- [[USE_INVALID_TARGET]], si la cible n'existe pas
	- [[USE_NOT_ENOUGH_TP]], si votre entité n'a pas assez de TP
	- [[USE_INVALID_COOLDOWN]], si la puce n'est pas encore utilisable
	- [[USE_INVALID_POSITION]], si la portée est mauvaise ou la ligne de vue n'est pas dégagée

Les valeurs [[USE_SUCCESS]] et [[USE_CRITICAL]] valant respectivement 1 et 2, et les autres 0 ou étant négatives, il est possible de savoir si l'utilisation de la puce a réussi en effectuant le test :
```
if (useChipOnCell(chip, cell) > 0) {
	// L'utilisation a réussi !
} else {
	// L'utilisation a échoué !
}
```

#### Voir aussi

- [[useChip]] : Utiliser une puce sur une entité au lieu d'une cellule.
- [[getCellToUseChip]] : Déterminer une cellule d'où utiliser une puce.
- [[useWeapon]] : Utiliser une arme.
- [[resurrect]] : Utiliser la puce [[Résurrection]].
- [[summon]] : Invoquer un bulbe comme [[Bulbe Chétif]].
