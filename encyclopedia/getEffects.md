# getEffects
> Fonctions

Retourne la liste des effets de l'entité d'id **entity**. Pour récupérer directement la liste des effets de votre entité, utilisez [[getEffects]] sans paramètre.

#### Paramètres

 - **entity** : L'id de l'entité dont la liste des effets sera retourné.

#### Retour

 - **effects** : La liste des effets actuellement présents sur l'entité **entity**. La liste des effets est un tableau contenant les effets. Un effet est lui-même un tableau de 8 cases de la forme : 
```
 [type, value, caster_id, turns, critical, item_id, target_id, modifiers]
```
 - *type* est le type de l'effet parmi :
	 - [[EFFECT_DAMAGE]], **value** est le nombre de dégâts
	 - [[EFFECT_HEAL]], **value** est le nombre de PV soignés
	 - [[EFFECT_BUFF_STRENGTH]], **value** est la force gagnée
	 - [[EFFECT_BUFF_AGILITY]], **value** est l'agilité gagnée
	 - [[EFFECT_BUFF_TP]], **value** est le nombre de PT gagnés
	 - [[EFFECT_BUFF_MP]], **value** est le nombre de PM gagnés
	 - [[EFFECT_ABSOLUTE_SHIELD]], **value** est le bouclier absolu gagné
	 - [[EFFECT_RELATIVE_SHIELD]], **value** est le bouclier relatif gagné
	 - [[EFFECT_DEBUFF]], indique un débuff, **value** est le pourcentage d'effets retiré.
etc.
 - *value* : La valeur de l'effet.
 - *caster_id* : L'id de l'entité qui a lancé l'effet.
 - *turns* : Le nombre de tours restants de l'effet.
 - *critical* : Est-ce que l'effet est un coup critique.
 - *item_id* : L'id de l'item qui a provoqué cet effet.
 - *target_id* : L'id de la cible de l'effet (**entity**).
 - *modifiers* : Les modificateurs de l'effet (masque de bits avec les constantes **EFFECT_MODIFIER_***).