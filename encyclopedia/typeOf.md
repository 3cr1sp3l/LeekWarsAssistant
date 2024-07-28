# typeOf
> Fonctions

Renvoie le type de la valeur **value**, parmis les types :
  - [[TYPE_NULL]] pour une valeur `null`.
  - [[TYPE_BOOLEAN]] pour un booléen, `true` ou `false`.
  - [[TYPE_NUMBER]] pour un nombre, exemple : `12`, `-0.15`.
  - [[TYPE_STRING]] pour une chaîne de caractères, exemple : `"salut"`.
  - [[TYPE_ARRAY]] pour un tableau, exemple : `[1, 2, 3]`.
  - [[TYPE_MAP]] pour un tableau associatif, exemple : `[a: 5, b: true]`.
  - [[TYPE_OBJECT]] pour un objet, exemple : `{a: 5, b: true}`.
  - [[TYPE_CLASS]] pour une classe, exemple : `class A { }`.
  - [[TYPE_FUNCTION]] pour une fonction, exemple : `function() {}`.

#### Paramètres

  - **value** : La valeur dont le type sera retourné.

#### Retour

  - **type** : (nombre) Le type de **value**.
