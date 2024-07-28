# canUseWeaponOnCell
> Fonctions

Détermine si votre entité peut tirer sur la cellule **cell** avec l'arme **weapon** depuis sa cellule courante.

La fonction vérifie les points suivants :
 - Portée : comparaison entre la distance et la portée minimale et maximale de l'arme.
 - Ligne de vue dégagée entre les deux positions ([[lineOfSight]]).
 
La fonction ne vérifie pas si vous avez les [[PT]] suffisants pour le coût de l'arme ou si l'arme est équipée.

#### Paramètres

- **weapon** : L'arme à tester. Par défaut votre arme actuellement équipée.
- **cell** : Le numéro de la cellule sur laquelle vous voulez tirer.

#### Retour

- **canUse** : `true` si votre entité peut tirer sur la cellule, `false` sinon.


#### Voir aussi

- [[getCellToUseWeapon]] : détermine une cellule d'où utiliser une arme.
- [[getWeaponCost]] : récupère le coût d'une arme.
- [[lineOfSight]] : vérifie si la ligne de vue est dégagée entre deux cellules.
- [[canUseChipOnCell]] : comme canUseWeaponOnCell mais pour une puce.
- [[canUseWeapon]] : comme canUseWeaponOnCell mais pour cibler une entité plutôt qu'une cellule.
