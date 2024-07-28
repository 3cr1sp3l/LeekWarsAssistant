# replace
> Fonctions

Remplace toutes les occurrences de **search** par **replace** dans la chaîne **string**.

#### Paramètres

- **string** Chaîne dans laquelle les remplacements sont effectués.
- **search** Sous-chaîne à remplacer.
- **replace** Chaîne de remplacement.

#### Retour

- **string** La chaîne résultat, avec les remplacements.

#### Exemples

`replace("Banana", "n", "t") // "Batata"`
`replace("a,b,c,d,e,f", ",", "+") // "a+b+c+d+e+f"`
`replace("Bonjour tout le monde", "Bonjour", "Bonsoir") // "Bonsoir tout le monde"`