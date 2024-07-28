# number
> Fonctions

Convertit une valeur en nombre. Si la valeur est une chaîne, la fonction number va essayer de la convertir en nombre, si la valeur est déjà un nombre, la fonction renvoie le nombre, et pour tout autre type, elle renvoie 0.

#### Paramètres

- **value** La valeur à convertir en nombre.

#### Retour

- **number** Le nombre converti.

#### Exemples

`number("12345") // 12345`
`number("3.14159") // 3.14159`
`number("bonjour") // 0`

#### Voir aussi

- [[string]]