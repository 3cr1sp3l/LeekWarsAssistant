# indexOf
> Fonctions

Détermine la position de la première occurrence de la chaîne **search** dans la chaîne **string**.

#### Paramètres

- **string** La chaîne où la recherche sera effectuée.
- **search** La chaîne à rechercher.
- **start** La position de début de recherche, par défaut le début de la chaîne (**0**).

#### Retour

- **index** La position de la première occurrence de **search** dans **string**, -1 si la chaîne n'a pas été trouvée.

#### Exemples

`indexOf("Bonjour", "jour") // 3`
`indexOf("Bonjour", "zzz") // -1`
`indexOf("Bonjour tout le monde", "on", 0) // 1`
`indexOf("Bonjour tout le monde", "on", 10) // 17`
