# getWeapon
> Fonctions

Renvoie l'arme actuellement équipée de l'entité **entity**, ou de votre entité si aucun paramètre n'est fourni.

Si aucune arme n'est équipée, la fonction renvoie la valeur `null`.

*Exemple* : si j'ai le pistolet équipé, j'utilise un boost [[Protéines]] :
```
if (getWeapon() == WEAPON_PISTOL) {
	useChip(CHIP_PROTEIN)
}
```

#### Paramètres

- **entity** : L'id de l'entité dont l'arme actuelle sera renvoyée, par défaut, vous-même.

#### Retour

- **weapon** : L'id de l'arme actuellement équipée sur l'entité **entity**, `null` si l'entité n'a pas d'arme équipée ou si l'entité n'existe pas.

#### Voir aussi

- [[getWeapons]] : renvoie toutes les armes
- [[setWeapon]] : équipe une arme
