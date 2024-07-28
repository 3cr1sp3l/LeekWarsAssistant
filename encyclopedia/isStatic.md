# isStatic
> Fonctions

Renvoie si l'entité **entity** est statique ou non. Une entité statique ne peut pas se déplacer ou être déplacée.

C'est notamment le cas des [[Tourelles]] d'équipe.

*Exemple* :
```
if (isStatic(entity)) {
	debug("Cette entité ne peut pas être déplacée")
}
```

#### Paramètres

- **entity** : L'id de l'entité à tester.

#### Retour

- **static** : `true` si **entity** est statique, `false` sinon.
