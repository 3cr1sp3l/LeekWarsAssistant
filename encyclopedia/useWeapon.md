# useWeapon
> Fonctions

Utilise l'arme sélectionnée sur l'entité **entity**.

*Exemple* : utiliser le pistolet sur l'ennemi le plus proche :
```
var enemy = getNearestEnemy()
setWeapon(WEAPON_PISTOL)
useWeapon(enemy)
```

#### Paramètres

- **entity** : Entité ciblée.

#### Retour

- **result** : Une valeur strictement supérieure à 0 si l'attaque a été lancée. Les valeurs de retour de useWeapon sont :
	- [[USE_CRITICAL]], en cas de coup critique
	- [[USE_SUCCESS]], en cas de réussite
	- [[USE_FAILED]], en cas de d'échec
	- [[USE_INVALID_TARGET]], si la cible n'existe pas
	- [[USE_NOT_ENOUGH_TP]], si votre entité n'a pas assez de TP
	- [[USE_INVALID_POSITION]], si la portée est mauvaise ou la ligne de vue n'est pas dégagée

Les valeurs [[USE_SUCCESS]] et [[USE_CRITICAL]] valant respectivement 1 et 2, et les autres 0 ou étant négatives, il est possible de savoir si l'utilisation de l'arme a réussi en effectuant le test :
```
if (useWeapon(entity) > 0) {
	// L'utilisation a réussi !
} else {
	// L'utilisation a échoué !
}
```

#### Voir aussi

- [[setWeapon]] : équipe une arme.
- [[useWeaponOnCell]] : utiliser une arme sur une cellule au lieu d'une entité.
- [[getCellToUseWeapon]] : détermine une cellule d'où utiliser une arme.
- [[useChip]] : utiliser une puce.
