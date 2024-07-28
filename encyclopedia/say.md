# say
> Fonctions

Fait déclarer la phrase **message** à votre entité.

Cette fonction coûte **1PT** <img height=16 src="https://leekwars.com/image/charac/tp.png">.

La longueur du message est limitée à **100**, le surplus sera coupé.
Pour limiter la surcharge de blabla, une limite de **2** say() par tour est en place.

*Exemple* : saluer son adversaire :
```leekscript
say("Salut à toi, " + getName(getNearestEnemy() + " !")
```

#### Paramètres

- **message** : Message qu'annonçera votre entité dans l'arène.

#### Voir aussi

- [[listen]] : écouter les `say()` des autres.