# canUseChipOnCell
> Fonctions

Détermine si votre entité peut utiliser la puce **chip** sur la cellule **cell** depuis sa cellule courante.

La fonction vérifie les points suivants :
- Portée : comparaison entre la distance et la portée minimale et maximale de la puce.
- Ligne de vue dégagée entre les deux positions ([[lineOfSight]]).
 
La fonction ne vérifie pas si vous avez les [[PT]] suffisants pour le coût de la puce ou si la puce n'est pas en récupération (temps de récupération : [[getCooldown]]).


#### Paramètres

- **chip** : Le numéro de la puce à tester.
- **cell** : Le numéro de la cellule sur laquelle vous voulez utliser la puce.

#### Retour

- **canUse** : `true` si votre entité peut utiliser la puce, `false` sinon.


#### Voir aussi

- [[getCellToUseChip]] : détermine une cellule d'où utiliser une puce.
- [[getChipCost]] : récupère le coût d'une puce.
- [[lineOfSight]] : vérifie si la ligne de vue est dégagée entre deux cellules.
- [[canUseWeaponOnCell]] : comme canUseChipOnCell mais pour une arme.
- [[canUseChip]] : comme canUseChipOnCell mais pour cibler une entité plutôt qu'une cellule.
