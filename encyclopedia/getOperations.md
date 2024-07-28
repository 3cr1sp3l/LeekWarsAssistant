# getOperations
> Fonctions

Renvoie le nombre d'opérations consommées par votre entité depuis le début de son tour. Ce nombre doit rester inférieur à [[OPERATIONS_LIMIT]] pour ne pas que l'entité plante.

*Exemple* :
```
if (getOperations() > OPERATIONS_LIMIT * 0.9) {
	break // 90% des opérations utilisées, on arrête.
}
```

#### Retour

- **operations** : Nombre d'opérations consommées par votre entité depuis le début de son tour.


