# getWeaponEffects
> Fonctions

Renvoie les effets de l'arme **weapon**.

#### Paramètres

- **weapon** : L'id de l'arme dont les effets seront retournés.

#### Retour

- **effects** : Un tableau contenant les effets de l'arme **weapon**. Chaque effet est lui-même un tableau de la forme
[type, min, max, turns, targets, modifiers].
	- **type** est une constante parmis les constantes d'effet : [[EFFECT DAMAGE|EFFECT_DAMAGE]], [[EFFECT_HEAL]], [[EFFECT_ABSOLUTE_SHIELD]], [[EFFECT_RELATIVE_SHIELD]], [[EFFECT_DEBUFF]], [[EFFECT_BUFF_STRENGTH]], [[EFFECT_BUFF_AGILITY]], [[EFFECT_BUFF_MP]], [[EFFECT_BUFF_TP]] etc.
	- **min** et **max** sont la valeur minimum et maximum de l'effet (comme indiqué dans le marché).
	- **turns** est la durée de l'effet en nombre de tours.
	- **targets** représente les joueurs qui seront touchés par cet effet dans la zone. Il s'agit d'une combinaison binaire des constantes :
		- [[EFFECT_TARGET_ALLIES]] : Affecte les alliés
		- [[EFFECT_TARGET_ENEMIES]] : Affecte les ennemis
		- [[EFFECT_TARGET_CASTER]] : Affecte le lanceur
		- [[EFFECT_TARGET_SUMMONS]] : Affecte les invocations
		- [[EFFECT_TARGET_NON_SUMMONS]] : Affecte les entités non invoquées
	- **modifiers** représente les modificateurs de l'effet. Il s'agit d'une combinaison binaire des constantes :
		- [[EFFECT_MODIFIER_STACKABLE]] : L'effet est cumulable.
		- [[EFFECT_MODIFIER_MULTIPLIED_BY_TARGETS]] : L'effet est multiplié par le nombre de cibles touchées dans la zone.
		- [[EFFECT_MODIFIER_ON_CASTER]] : Affecte toujours le lanceur.

#### Exemples

Récupérer les dégâts moyens d'une arme :
```
var effects = getWeaponEffects(WEAPON_PISTOL)
var dégâtsMoyens = (effects[0][1] + effects[0][2]) / 2
```

Lire les cibles *targets* :
```
if (targets & EFFECT_TARGET_ALLIES) debug('Affecte les alliés')
if (targets & EFFECT_TARGET_ENEMIES) debug('Affecte les ennemis')
if (targets & EFFECT_TARGET_CASTER) debug('Affecte le lanceur')
if (targets & EFFECT_TARGET_SUMMONS) debug('Affecte les invocations')
if (targets & EFFECT_TARGET_NON_SUMMONS) debug('Affecte les poireaux')
```

Lire les modificateurs :
On peut lire cette valeur de la manière suivante :
```
if (modifiers & EFFECT_MODIFIER_STACKABLE) debug("L'effet est cumulable")
if (modifiers & EFFECT_MODIFIER_MULTIPLIED_BY_TARGETS) debug("L'effet est multiplié par le nombre de cibles")
if (modifiers & EFFECT_MODIFIER_ON_CASTER) debug("Affecte le lanceur")
```
