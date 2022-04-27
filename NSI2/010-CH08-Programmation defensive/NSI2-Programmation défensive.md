\chapter{\large programmation[-1em]\fontsize{35pt}{42pt}\selectfont\titlefont Initiation à laprogrammation défensive}
\introduction{Attrapez-les toutes !}

La *programmation défensive* est un ensemble de règles pour concevoir des programmes assurés de fonctionner dans le pire des cas.
Les principales sont
	-  	ne pas faire confiance aux données entrées par les utilisateurs;
	-  	gérer les exceptions avec `#!python try` / `#!python except`;
	-  	écrire des tests avec `#!python assert`;
	-  	ne pas chercher à réinventer la roue : utiliser des modules qui ont fait leurs preuves.	


## Gestion des exceptions
### L'utilisateur et ses facéties
On a malheureusement déjà vu ceci :
```python
def inverse(x : float) -> float :
	return 1 / x
```
L'utilisateur évalue `#!python inverse(0)` et obtient :

{\color{red}\tw{Traceback (most recent call last):
\hspace{2em}File "fonction1.py", line 4, in <module>
\hspace{4em}inverse(0)
\hspace{2em}File "fonction1.py", line 2, in inverse
\hspace{4em}return 1 / x
ZeroDivisionError: division by zero}}


Le message d'erreur peut se lire ainsi : Il y a une erreur quand on appelle `#!python inverse(0)` car lorsqu'on doit renvoyer `#!python 1/x` cela provoque une erreur de type `#!python ZeroDivisionError`.

De la même manière lorsque l'utilisateur évalue `#!python inverse('chaussette')` il obtient :

{\color{red}\tw{Traceback (most recent call last):
		\hspace{2em}File "fonction1.py", line 4, in <module>
		\hspace{4em}inverse(0)
		\hspace{2em}File "fonction1.py", line 2, in inverse
		\hspace{4em}return 1 / x
TypeError: unsupported operand type(s) for /: 'int' and 'str'}}

Effectivement l'opérateur `#!python /` ne peut pas diviser un `#!python int` par un `#!python str`.

`#!python ZeroDivisionError` et `#!python TypeError` sont deux représentants de ce qu'on appelle des *exceptions*. On dit qu'*une exception est levée* (*an exception is raised* en Anglais) lorsque l'interpréteur Python rencontre un problème qu'il ne peut résoudre ou bien que le programme lui même indique que ce doit être le cas. Les exceptions les plus courantes sont ces deux premières ainsi que 
	-  	`#!python NameError` pour une variable non définie;
	-  	`#!python IndexError` pour un indice de liste trop grand;
	-  	`#!python KeyError` pour une clé de dictionnaire inexistante;

On pourra trouver la liste de toutes les exceptions \link{https://docs.python.org/fr/3.8/library/exceptions.html}{ici}.

	Une exception est un objet de Python servant à représenter une erreur.

### Syntaxe de la gestion des exceptions
Ne pas faire confiance à l'utilisateur c'est prévoir ces exceptions. La syntaxe Python est simple :
	-  	la partie du code susceptible de lever une exception est mise dans un bloc `#!python try`;
	-  	si une exception est levée on la gère avec un bloc `#!python except`.

{{py('fonction1.py')}}

Dans l'exemple ci-dessus les erreurs de type et de division par zéro sont gérées par un message d'affichage et le renvoi de la valeur zéro (zéro n'est l'inverse d'aucun nombre).

	La gestion des erreurs permet d'éviter que le programme s'arrête brusquement mais elle n'élimine pas les erreurs, elle fait en sorte de les signaler à l'utilisateur du programme (ou du module). C'est donc à lui de rectifier ce qui produit l'erreur.

	Quand on gère les exceptions, on doit toujours le faire en précisant le type de l'exception qui a été levée. Le programme suivant fonctionne mais n'est pas recommandé car lorsqu'une exception a lieu, on ne sait pas laquelle.
\inputminted{python}{scripts/fonction2.py}


## Tests unitaires

Un (ou des) test(s) unitaire(s) sert à vérifier qu'une partie d'un programme (une *unité*) fonctionne comme on l'a prévu.

Lorsqu'on écrit une partie d'un programme destinée à effectuer une tâche particulière, il est préférable d'écrire quelques tests *avant même d'écrire le programme*.
Les tests doivent être pensés pour aborder le cas général ainsi que les cas particuliers. Cette démarche aide à clarifier les idées pour programmer correctement.

### Utilisation de `#!python assert`

Le mot-clé `#!python assert` sert à vérifier qu'une *assertion* (un test de condition) est vraie. Si c'est le cas le programme continue, sinon une exception du type `#!python AssertionError` est levée. Ainsi on peut la gérer avec une structure `#!python try` / `#!python except` comme vu précédemment.

{{py('assert1.py')}}
### Un exemple

On veut coder une fonction `#!python sort` (qui signifie *trier* en Anglais) qui 
	-  	en entrée prend une liste d'`#!python int`;
	-  	en sortie renvoie une liste qui contient les mêmes valeurs que la liste d'entrée, mais triées dans l'ordre croissant.	

La stratégie conseillée est d'écrire les tests d'abord :

{{py('assert2.py')}}

Le premier test vérifie qu'il n'y a pas d'erreur avec une liste vide (cas particulier qui peut arriver). Le deuxième vérifie qu'il y a effectivement tri, le troisième vérifie que `#!python sort` fonctionne sur une liste avec doublons.

	En mathématiques, on sait que « quelques exemples ne peuvent servir à prouver une généralité\fg. De la même manière quelques tests ne constituent pas une *preuve absolue* qu'un programme fonctionne correctement.

## Utiliser des modules déjà écrits

C'est ce que l'on veut dire par « ne pas chercher à réinventer la roue» : quand on doit écrire un programme, il est plus que probable que les fonctionnalités qu'on veut implémenter l'aient déjà été par quelqu'un d'autre, que la communauté l'utilise et en est satisfaite. Si c'est le cas, autant l'utiliser, à moins que
	-  	vous-même ne soyez pas satisfaits des performances du module (trop lent, trop gourmand en mémoire);
	-  	une situation technique particulière fait que vous ne pouvez pas l'utiliser dans votre projet;
	-  	vous êtes élève/étudiant et votre professeur\cdot e	vous a donné cet exercice/projet pour vous former.
\exostart
	On veut coder une fonction `#!python age` qui demande à l'utilisateur majeur d'entrer son âge, on attend donc qu'il entre un entier entre 18 et 120.
		-  	la fonction ne prend rien en entrée;
		-  	elle renvoie un `#!python int` compris entre 18 et 120, et tant que l'utilisateur n'entre pas un âge valide elle lui demande d'entrer son âge.
	Programmer cette fonction de manière défensive (gérer les exceptions).

	On veut coder une fonction `#!python is_sorted` qui 
		-  	en entrée prend une liste d'`#!python int` éventuellement vide;
		-  	renvoie `#!python True` si elle est triée par ordre croissant (ou vide ou bien avec un seul élément) et `#!python False` dans le cas contraire.	
	Écrire un ensemble de tests pertinents pour cette fonction.

	Reprendre le module `#!python fractions_custom` du chapitre précédent et gérer toutes les exceptions :
		-  	l'utilisateur crée n'importe quoi;
		-  	l'utilisateur divise par zéro.
	On pourra utiliser la fonction `#!python isinstance()` qui
		-  	prend en entrée une variable et un type de variable;
		-  	renvoie `#!python True` si la variable est bien ce ce type et `#!python False` sinon.
				Par exemple `#!python isinstance(2,str)` renvoie `#!python False`.
	On veut créer une fonction `#!python merge` (qui veut dire *fusionner* en Anglais) qui
		-  	prend en entrée 2 listes d'entiers triées par ordre croissant éventuellement vides;
		-  	renvoie une liste composée des valeurs des 2 listes, triées par ordre croissant.
				Par exemple `#!python merge([1, 3, 8], [4, 5, 10])` doit renvoyer `#!python [1, 3, 4, 5, 8, 10]`	.
		-  	Écrire des tests pertinents pour cette fonction.
		-  	**Compliqué :** programmer cette fonction. Le plus simple est de la programmer de manière récursive. On peut la programmer de manière impérative mais c'est plus long et sans doute plus compliqué.

Reprendre le module `#!python kb_mouse` du chapitre précédent et gérer les exceptions.
