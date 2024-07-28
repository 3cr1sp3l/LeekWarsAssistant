# arraySort
> Fonctions

Trie la liste **array** selon l'ordre défini par la fonction **callback**.

Les éléments sont comparés deux à deux, la fonction callback doit renvoyer une valeur *négative*, `0` ou *positive* selon si la premiere valeur est avant, au même niveau ou après la seconde valeur.

Exemple :
```leekscript
var liste = [4, 1, 2, 5, 3]
var resultat = arraySort(liste, function(a, b) {
	return a - b
}) // [1, 2, 3, 4, 5]
```

#### Paramètres

- **array** : Liste d'origine
- **callback** : Fonction de tri.

#### Retour

- **sortedArray** : Le tableau trié

#### Notes

- En LS1-3, si la fonction callback prend 2 paramètres, ce sont les deux valeurs qui sont envoyées, si elle en prend 4, ce sont les couples clé/valeur qui sont envoyés.

- Une fonction flèche est pratique pour simplifier l'écriture, exemple avec le code précédent :
```leekscript
arraySort([4, 1, 2, 5, 3], (a, b) => a - b) // [1, 2, 3, 4, 5]
```