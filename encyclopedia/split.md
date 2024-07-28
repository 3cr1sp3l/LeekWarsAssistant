# split
> Fonctions

Découpe la chaîne **string** sous-chaînes en délimitées par **delimiter**. Pour limiter la découpe à un certain nombre de morceaux, utilisez le paramètre **limit**.

#### Paramètres

- **string** Chaîne à découper.
- **delimiter** Chaîne délimitant le passage d'un élément à un autre.
- **limit** (optionnel) Le nombre maximum de sous-chaînes, par défaut, pas de limite.

#### Retour

- **parts** Tableau contenant les sous-chaînes trouvées.

#### Exemples

`split("456-789-123", "-") // ["456", "789", "123"]`
`split("Hello", "") // ["H", "e", "l", "l", "o"]`
`split("Hello", "zzz") // ["Hello"]`
`split("456-789-123", "-", 2) // ["456", "789-123"]`