\setcounter{chapter}{1}
\creativecommonsfooter

\chapter{\large Arithmétique[-1em]\fontsize{35pt}{42pt}\selectfont\titlefont Opérations en base 2 et 16}
\introduction{Préparez-vous pour l'opération addition}

## Additions

On pose l'opération à la main : c'est la même chose qu'en base 10.
\subsection*{En base 2}
La seule différence avec la base 10 c'est que deux 1 donnent $(2)_{10}$ donc $(10)_2$, donc un zéro et une retenue de 1.
Quand il y a deux 1 et une retenue de 1 en plus, cela donne $(3)_{10}$ donc $(11)_2$, donc un 1 et une retenue de 1.

 			 &   &   &  & $_1$ & $_1$ &  &  &  
			 & 1 & 1 & 0 & 1 & 0 & 1 & 0 & 1 
			+ &  &  &  & 1 & 1 & 1 & 0 & 0 
			\hline
			 =& 1 & 1 &  1& 1 & 0 & 0 & 0 & 1 

\subsection*{En base 16}

C'est encore la même chose. Il faut bien se souvenir de la valeur de A, B, C, D, E et F.
Ajouter 8 et 3 ne provoque pas de retenue puisque $8+3=11$ et que $11$ est $B$ en base 16.
Dès que l'addition de 2 chiffres dépasse 15, il y aura une retenue : par exemple 9 et A donnent $(19)_{10}$, donc $(13)_{16}$. Ainsi on note 3 et une retenue de 1.

	&  & $_1$ &  &  
	& 2 & 4 & 9 & 8 
	+ & 1 & 7 & A & 3 
	\hline
=	& 3 & C & 3 & B 

## Multiplications par 2 en binaire

		-  	Multiplier un nombre écrit en binaire par 2 revient à décaler la virgule d'un cran vers la droite (ou ajouter un zéro à droite si le nombre est entier).
		-  	Diviser un nombre écrit en binaire par 2 revient à décaler la virgule d'un cran vers la gauche.

		-  	$(1\ 0101)_2\times (2)_{10}=(10\ 1010)_2$
		-  	$(11,01)_2\times (16)_{10}=(11\ 0100)_2$
		-  	$(1\ 1101)_2\div (2)_{10}=(1110,1)_2$
		-  	$(101)_2\div (32)_{10}=(0,0010\ 1)_2$

	Rappelons-nous que $(2)_{10}=(10)_2$, et que plus généralement $2^n$ s'écrit en binaire comme « un 1 suivi de $n$ zéros\fg.

\exostart

	Ajouter $(1101\ 1011)_2$ et $(0011\ 0110)_2$ en posant l'opération.

	On pose  $a=(1001)_2$, $b=(0010\ 1000)_2$ et $c=(0001\ 0111)_2$.

Calculer $a +b+c$ en posant les opérations (on peut faire des étapes ou bien tout calculer en une fois).


	On reprend les données de l'exercice précédent.	Calculer $a\times 4+b\div 8 +c$.

	Calculer à la main $(AF3)_{16}+(8AD)_{16}$.

	Calculer à la main $(123)_{16}+(456)_{16}+(789)_{16}$ en posant une seule opérations si possible.


