# getSummoner
> Fonctions

Renvoie l'entité qui a invoqué l'entité **entity**, s'il s'agit d'une invocation.

#### Paramètres

- **entity** : L'id de l'entité dont l'invocateur sera renvoyé.

#### Retour

- **summoner** : L'id de l'entité qui a invoqué **entity**.
    - `-1` si **entity** n'est pas une invocation
	- `null` si **entity** n'est pas l'identifiant d'une entité du combat


