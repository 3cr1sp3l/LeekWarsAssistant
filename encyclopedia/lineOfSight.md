# lineOfSight
> Fonctions

Vérifie la ligne de vue entre la cellule **start** et la cellule **end**, en ignorant les entitées dans le tableau **entityToIgnore**.

*Exemple* : `if (lineOfSight(getCell(), getCell(enemy))`

L'algorithme se décrit comme suit :
- Tracer un segment entre les centres des deux cellules testées.
- Faire la liste des cellules traversées par ce segment. Une cellule n'est pas considérée comme traversée si le segment frôle son bord, ou bien si elle est ignorée.
- Si une seule de ces cellules traversée est un obstacle ou contient une entité, la ligne de vue est bloquée, sinon elle est dégagée.

#### Paramètres

- **start** : Cellule de départ.
- **end** : Cellule cible.
- **entityToIgnore** (optionnel) : Entité à ignorer ou tableau d'entitées à ignorer, par défaut, votre entité est ignorée.

#### Retour

- **los** : (booléen)
	- `null` si **start** ou **end** n'est pas une cellule de la carte ;
	- `true` si la ligne de vue est dégagée ;
	- `false` sinon.
	
#### Démonstration

Cliquez sur une cellule pour afficher toutes les cellules qui sont en ligne de vue avec.

{{ line-of-sight }}
