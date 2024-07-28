# getCell
> Fonctions

Retourne la cellule où se trouve l'entité d'id <b>entity</b>.
Utilisez `getCell()` sans paramètre pour récupérer votre cellule.

*Exemple* : calculer la distance entre moi et l'enemi, et se booster s'il est proche :
```
var distance = getCellDistance(getCell(), getCell(enemy))
if (distance < 10) {
	useChip(CHIP_PROTEIN)
}
```

#### Paramètres

- **entity** : L'id de l'entité dont la cellule sera retournée, par défaut votre entité.

#### Retour

- **cell** : Le numéro de la cellule où se trouve l'entité <b>entity</b>.

#### Voir aussi

- [[getCellX]]
- [[getCellY]]
- [[getCellFromXY]]
- [[getCellDistance]]