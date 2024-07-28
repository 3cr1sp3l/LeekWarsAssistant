# arrayClear
> Fonctions

Vide la liste **array** de tous ses éléments.

*Exemple* :
```
var liste = [1, 2, 3, 4]
arrayClear(liste)
debug(liste) // []
```

#### Paramètres

- **array** : La liste à vider.

#### Plus d'informations

Pour la plupart des cas, le code `liste = []` est équivalent à `arrayClear(liste)`. Cependant, si vous utilisez des champs `final` dans une classe, il est impossible d'utiliser `=` et donc `= []` sur ces derniers. `arrayClear` sera dans ce cas la seule façon de vider une liste facilement.

#### Synonymes

- clear, empty, vider