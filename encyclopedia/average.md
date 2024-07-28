# average
> Fonctions

Calcule la moyenne des éléments contenus dans le tableau **array**.<br>
La moyenne est calculée en convertissant chaque élément en nombre réel, en calculant leur somme et enfin en divisant cette somme par la taille du tableau.

#### Paramètres

  - **array** : Tableau dont on veut calculer la moyenne.

#### Retour

  - **averageValue** : (nombre réel) Valeur moyenne.
    - Si le tableau est vide, renvoie `0.0`.

#### Exemples

```
var array = [10, 15.5, 16, 18, 13]
debug("moyenne = " + average(array)) // Affiche 14.5
```
