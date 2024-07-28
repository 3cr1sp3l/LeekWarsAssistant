# codePointAt
> Fonctions

Renvoie le codepoint unicode (32 bits, nombre entier) situé à la position **index** (ou 0 par défaut) dans la chaîne **string**.

*Exemple* : `codePointAt('salut', 1) // 97 (caractère 'a')`

#### Paramètres

- **string** : La chaîne.
- **index** : L'index du codepoint, par défaut `0`.

#### Retour

- **codePoint** : Le codepoint unicode.

#### Exemples

- `codePointAt('🐨') // 128040`

#### Voir aussi

- [[charAt]]