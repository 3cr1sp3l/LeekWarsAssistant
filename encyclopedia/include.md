# include
> Fonctions

Inclut l'IA localisée au chemin **ai** dans l'IA courante.

Attention, la fonction include doit être appelée uniquement dans le bloc principal, et son paramètre doit être une chaîne écrite directement dans le code.

- Pour inclure une IA dans un **dossier différent** :
```
include("dossier/autre/fonctions.leek")
```

- Pour remonter dans un **dossier parent** :
```
include("../strategie/attaque.leek")
```

- Pour partir du **dossier racine** :
```
include("/principal/item.leek")
```

#### Paramètres

- **ai** : Le chemin de l'IA à inclure.

#### Synonymes

import, require