# arrayFilter
> Fonctions

Retourne une nouvelle liste contenant toutes les valeurs de la liste source **array** pour lesquels la fonction **callback** a renvoyé une valeur équivalente à `true`.

La fonction **callback** prend de 1 à 3 paramètres dans cet ordre : (*valeur*, *position*, *liste source*).

*Exemple* :
```leekscript
var array = [1, 2, 3, 4, 5]
var result = arrayFilter(array, function(v) {
    return v % 2 == 0
}) // [2, 4]
```

#### Paramètres

- **array** Liste d'origine.
- **callback** Fonction appelée pour chaque élément.

#### Retour

- **newArray** Nouvelle liste filtrée.

#### Note

- En **LeekScript V1**, des valeurs `null` sont laissées à la place des valeurs retirées.
- En **LeekScript <= V3**, si la fonction callback prend un paramètre, c'est la valeur de la liste source qui sera envoyée, si elle prend deux paramètres c'est la clé et la valeur qui seront envoyées.
