# length
> Fonctions

Renvoie la longueur de la chaîne **string**.

Les chaînes étant encodées en UTF-16, certains caractères comptent pour 2, comme les emojis (exemple `😊`)

#### Paramètres

- **string** La chaîne dont la longueur sera retournée.

#### Retour

- **length** La longueur de la chaîne **string**.

#### Exemples

`length("") // 0`
`length("a") // 1`
`length("Bonjour") // 7`
`length("😊") // 2`