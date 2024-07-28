# getTurn
> Fonctions

Renvoie le tour actuel du combat. 
Le nombre de tours maximum est [[MAX_TURNS]].

*Exemple* : se booster au tour 2 :
```
if (getTurn() == 2) {
	useChip(CHIP_MOTIVATION)
	useChip(CHIP_PROTEIN)
}
```

#### Retour

- **turn** : Le tour actuel du combat.


