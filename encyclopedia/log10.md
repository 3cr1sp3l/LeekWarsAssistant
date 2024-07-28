# log10
> Fonctions

Calcule le logarithme en base 10 du nombre **number**.

#### Paramètres

- **number** Un nombre compris dans l'intervalle ]0; +∞[.

#### Retour

- **log10**
  - Si **number** > 0, le logarithme en base 10 de **number**.
  - Si **number** <= 0, renvoie `NaN`.

#### Exemples

`log10(1) // 0`
`log10(10) // 1`
`log10(1000000) // 6`