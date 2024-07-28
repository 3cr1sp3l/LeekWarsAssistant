# atan2
> Fonctions

Convertit les coordonnées cartésiennes (<b>x</b>, <b>y</b>) en coordonnées polaires (<b>r</b>, <b>theta</b>). Cette fonction retourne l'angle <b>theta</b> entre -[[PI]] et [[PI]] en utilisant les signes des arguments.

#### Paramètres

- **y** Coordonnée en y.
- **x** Coordonnée en x.

#### Retour

- **result** L'angle <b>theta</b> en coordonnées polaires du point (x, y).

#### Note

Attention, les arguments sont bien dans l'ordre **Y** puis **X**, ce qui est un peu contre-intuitif.

#### Exemples

`atan2(1, 1) // PI / 4`
`atan2(-1, 1) // -PI / 4`
`atan2(1, -1) // 3 * PI / 4`
`atan2(-1, -1) // -3 * PI / 4`
