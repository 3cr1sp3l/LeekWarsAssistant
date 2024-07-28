# arrayMap
> Fonctions

Retourne un nouveau tableau contenant pour chaque valeur du tableau source **array**, la valeur retournée par la fonction **callback**. 

La fonction **callback** prend de 1 à 3 paramètres dans cet ordre : (*valeur*, *position*, *tableau source*).

#### Paramètres

- **array** : Tableau d'origine.
- **callback** : Fonction appelée pour chaque élément.

#### Retour

- **newArray** : Nouveau tableau.


#### Notes

- En **LeekScript <= 3**, si la fonction **callback** prend un paramètre, c'est la valeur du tableau source qui sera envoyée, si elle prend deux paramètres c'est la clé et la valeur qui seront envoyées.