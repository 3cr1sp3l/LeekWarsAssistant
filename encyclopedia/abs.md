# abs
> Fonctions

Renvoie la valeur absolue du nombre **number**.

#### Paramètres

- **number** : Le nombre dont la valeur absolue sera calculée.

#### Retour

- **result** : La valeur absolue du nombre.

#### Notes

L'expression `abs(x)` est équivalente à `x > 0 ? x : -x`.

#### Exemples

- Enlever le signe d'un nombre :
```leekscript
var a = -12
var a_sans_signe = abs(a)
debug(a_sans_signe) // 12
```

- Calculer la distance entre deux nombres :
```leekscript
var a = 12
var b = -5
var distance = abs(a - b)
debug(distance) // 17
```

