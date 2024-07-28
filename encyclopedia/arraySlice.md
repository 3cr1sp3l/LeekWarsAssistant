# arraySlice
> Fonctions

Renvoie une sous-liste de **array** contenant tous les éléments à partir de la position **start** jusqu'à la position **end** (exclu).

Si le paramètre d'incrément **stride** est passé, la fonction ne sélectionne que un élément tous les **stride**.

*Exemple* : nouvelle liste contenant les éléments de la position 10 à 20 (exclu).
```
arraySlice(liste, 10, 20)
```

#### Paramètres

- **array** : La liste d'origine.
- **start** : La position de début.
- **end** : La position de fin (exclue).
- **stride** : L'incrément (par défaut `1`).

#### Retour

- **slice** : La sous-liste produite.

#### Exemples

  - Accès d'une plage : renvoie une nouvelle liste contenant les éléments de la position 10 (inclus) à 20 (exclu).
  ```
arraySlice(liste, 10, 20)
  ```
  - Accès d'une plage avec incrément : renvoie les éléments à la position 10, 13, 16, 19.
  ```
arraySlice(liste, 10, 20, 3)
```
  - Incrément négatif :  renvoie les éléments à la position 20, 17, 14, 11
   ```
arraySlice(liste, 20, 10, -3)
```

