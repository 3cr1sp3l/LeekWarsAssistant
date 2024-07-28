# getMessages
> Fonctions

Renvoie le tableau des messages de l'entité <b>entity</b>.

#### Paramètres

- **entity** : L'entité dont les messages seront renvoyés.

#### Retour

- **messages** : Le tableau des messages reçus par `entity`.<br>Un message est représenté lui-même sous la forme d'un
tableau de la forme : [<b>auteur</b>, <b>type</b>, <b>paramètres</b>]<br>
Les différents types de messages sont représentés par les constantes :
<ul>
	<li>#MESSAGE_HEAL : demande de soins</li>
	<li>#MESSAGE_ATTACK : demande d'attaquer</li>
	<li>#MESSAGE_BUFF_FORCE : demande de boost force</li>
	<li>...</li>
</ul>

#### Informations supplémentaires

- Il est possible de lire les messages envoyés entre deux autres entités si notre tour de jeu se situe entre l'entité l'entité qui émet et celle qui reçoit le message. Les messages addressés à une entité sont supprimés à la fin de son tour de jeu.
- Les messages envoyés par les entités de type ENTITY_MOB (dans les combats de boss) ne sont pas visibles par les poireaux.