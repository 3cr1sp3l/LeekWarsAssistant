# getLife
> Fonctions

Renvoie la vie actuelle de l'entité d'id <b>entity</b>.
Utilisez getLife() sans paramètre pour récupérer votre vie.

Exemple pour se soigner si notre vie est inférieure à 50% :
```
if (getLife() < getTotalLife() * 0.5) { // Si ma vie < 50%
	useChip(CHIP_CURE)
}
```

#### Paramètres

- **entity** : L'id de l'entité dont la vie sera renvoyée.

#### Retour

- **life** : La vie actuelle de l'entité <b>entity</b>.


