# string
> Fonctions

Convertit une valeur **value** en chaîne de caractères.

- Si la valeur est null, `null` est renvoyée.
- Si la valeur est un booléen, `"true"` et `"false"` sont respectivement renvoyées pour les valeurs `true` et `false`.
- Si la valeur est déjà une chaîne, elle est renvoyée.
- Si la valeur est nombre x, `"x"` est renvoyé.
- Si la valeur est un tableau, une chaîne sous la forme `[clé1 : valeur1, clé2 : valeur2, ...]` est renvoyée.
- Si la valeur est un objet, une chaîne sous la forme `Classe { champ1 : valeur1, champ2 : valeur2, ... }` est renvoyée.


#### Paramètres

- **value** La valeur à convertir en chaîne de caractères.

#### Retour

- **string** La chaîne convertie.

#### Exemples

`string(12345) // "12345"`
`string([1, 2, 3]) // "[1, 2, 3]"`
`string("hello") // "hello"`
`string(2 > 1) // "true"`

#### Voir aussi

- [[number]] : convertir une chaîne en nombre.

#### Synonymes

- toString