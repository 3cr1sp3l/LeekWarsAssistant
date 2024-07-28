# useChip
> Fonctions

Utilise la puce **chip** sur l'entité **entity**, ou sur vous-même si le second paramètre n'est pas fourni.

*Exemple* : Utiliser la puce [[Motivation]] sur moi-même :
```
useChip(CHIP_MOTIVATION)
```
*Exemple* : Utiliser la puce [[Décharge]] sur un enemi :
```
useChip(CHIP_SHOCK, enemy)
```

#### Paramètres

- **chip** : Chip à utiliser.
- **entity** : Entité cible, par défaut votre entité.

#### Retour

- **result** : Une valeur strictement supérieure à 0 si l'attaque a été lancée. Les valeurs de retour de useChip sont :
	- [[USE_CRITICAL]], en cas de coup critique
	- [[USE_SUCCESS]], en cas de réussite
	- [[USE_FAILED]], en cas de d'échec
	- [[USE_INVALID_TARGET]], si la cible n'existe pas
	- [[USE_NOT_ENOUGH_TP]], si votre entité n'a pas assez de TP
	- [[USE_INVALID_COOLDOWN]], si la puce n'est pas encore utilisable
	- [[USE_INVALID_POSITION]], si la portée est mauvaise ou la ligne de vue n'est pas dégagée

Les valeurs [[USE_SUCCESS]] et [[USE_CRITICAL]] valant respectivement 1 et 2, et les autres 0 ou étant négatives, il est possible de savoir si l'utilisation de la puce a réussi en effectuant le test :
```
if (useChip(chip, entity) > 0) {
	// L'utilisation a réussi !
} else {
	// L'utilisation a échoué !
}
```


#### Voir aussi

- [[useChipOnCell]] : Utiliser une puce sur une cellule au lieu d'une entité.
- [[getCellToUseChip]] : Déterminer une cellule d'où utiliser une puce.
- [[useWeapon]] : Utiliser une arme.
- [[resurrect]] : Utiliser la puce [[Résurrection]].
- [[summon]] : [Invoquer un bulbe](Bulbes) comme [[Bulbe Chétif]].
