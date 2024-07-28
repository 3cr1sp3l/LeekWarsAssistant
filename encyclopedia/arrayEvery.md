# arrayEvery
> Fonctions

Renvoie `true` si le prédicat **callback** appliqué à chacun des éléments de la liste renvoie `true`.

*Exemples* :
`arrayEvery([1, 2, 3, 4, 5], x => x > 0) // true`
`arrayEvery([1, 2, 3, 4, 5], x => x % 2 == 0) // false`

#### Paramètres

- **array** : La liste à parcourir.
- **callback** : Le prédicat à appeler.

#### Retour

- **every** : `true` si le prédicat à renvoyé `true` pour chaque élément, `false` sinon.

