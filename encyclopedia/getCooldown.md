# getCooldown
> Fonctions

Renvoie le cooldown actuel de la puce **chip** de l'entité **entity**.

Il s'agit du nombre de tours avant lesquels la puce deviendra utilisable, `0` si elle est actuellement utilisable. Pour les puces à cooldown infini comme [[Régénération]], renvoie un nombre supérieur à `MAX_TURNS` après utilisation.

#### Paramètres

- **chip** : La puce dont le cooldown actuel sera renvoyé.
- **entity** : L'entité dont le cooldown sera renvoyé.

#### Retour

- **cooldown** : Le cooldown actuel de la puce **chip**. 
