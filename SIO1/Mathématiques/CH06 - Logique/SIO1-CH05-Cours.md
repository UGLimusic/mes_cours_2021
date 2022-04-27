	\chapter{Logique propositionnelle}
	## Notion de proposition
		Une proposition est un énoncé qui a un sens et pour lequel on peut dire avec certitude qu'il est vrai ou faux. On dit qu'on peut lui associer une *valeur de vérité*. Cette valeur peut se noter vrai ou faux mais on peut aussi choisir de la noter 0 (pour faux) ou 1 (pour vrai).
 
			-  	« 2+2 = 5» est une proposition fausse.
			-  	« $2+2\equiv 1\ [3]$» est une proposition vraie.

		L'affirmation « Cette affirmation est fausse» est-elle une proposition ?
	## Connecteurs logiques
		L'opérateur de négation se note $\neg$. C'est un opérateur *unaire*, c'est à dire qu'il s'applique à *une* proposition.
		Il est défini par la table de vérité suivante : 
			\hline
			\rowcolor{lightgray}
			$P$ & $\neg P$  
			\hline 
			\rowcolor{white}
			0 & 1  
			\hline
			\rowcolor{white}
			1 & 0 
			\hline 
		$\neg P$ se lit « non P».

	L'opérateur de *conjonction* correspond au \tw{and} de Python, au \tw{And} de Visual Basic, au \tw{\&\&} de C++.
	Il se note $\wedge$, c'est un opérateur *binaire* car il s'applique à deux propositions.
	Il est défini par la table de vérité suivante : 
			\hline
			\rowcolor{lightgray}
			$P$ & $Q$ & $P\wedge Q$ 
			\hline 
			\rowcolor{white}
			0 & 0 & 0 
			\hline
			\rowcolor{white}
			0 & 1 & 0 
			\hline
			\rowcolor{white}
			1 & 0 & 0 
			\hline\rowcolor{white}
			1 & 1 & 1 
			\hline
	$P\wedge Q$ se lit « P et Q» et n'est vrai que si P est vrai et Q aussi.

	L'opérateur de *disjonction* correspond au \tw{or} de Python, au \tw{Or} de Visual Basic, au \tw{||} de C++.
	Il se note $\vee$, c'est un opérateur *binaire*.	Il est défini par la table de vérité suivante : 
			\hline
			\rowcolor{lightgray}
			$P$ & $Q$ & $P\vee Q$ 
			\hline 
			\rowcolor{white}
			0 & 0 & 0 
			\hline
			\rowcolor{white}
			0 & 1 & 1 
			\hline
			\rowcolor{white}
			1 & 0 & 1 
			\hline\rowcolor{white}
			1 & 1 & 1 
			\hline
	$P\vee Q$ se lit « P ou Q» et est vrai dès que P est vrai ou Q est vrai.

	Il se note $\Leftrightarrow$, c'est un opérateur *binaire*.
	Il est défini par la table de vérité suivante : 
			\hline
			\rowcolor{lightgray}
			$P$ & $Q$ & $P\Leftrightarrow Q$ 
			\hline 
			\rowcolor{white}
			0 & 0 & 1 
			\hline
			\rowcolor{white}
			0 & 1 & 0 
			\hline
			\rowcolor{white}
			1 & 0 & 0 
			\hline\rowcolor{white}
			1 & 1 & 1 
			\hline
	$P\Leftrightarrow Q$ se lit « P équivaut à Q» et n'est vrai que si P et Q ont la même valeur de vérité.


	Il se note $\Rightarrow$, c'est un opérateur *binaire*.
	Il est défini par la table de vérité suivante : 
			\hline
			\rowcolor{lightgray}
			$P$ & $Q$ & $P\Rightarrow Q$ 
			\hline 
			\rowcolor{white}
			0 & 0 & 1 
			\hline
			\rowcolor{white}
			0 & 1 & 1 
			\hline
			\rowcolor{white}
			1 & 0 & 0 
			\hline\rowcolor{white}
			1 & 1 & 1 
			\hline
	$P\Rightarrow Q$ se lit « P implique Q».
		-  	Quand P est fausse, $P\Rightarrow Q$ est vraie : « le faux implique n'importe quoi».
		-  	Quand P est vraie, $P\Rightarrow Q$ n'est vraie que si Q est aussi vraie : « le vrai n'implique que le vrai».	

	 On note P et Q les affirmations suivantes :
	P = « Paul aime le foot »
	Q = « Paul aime les maths »
	Représenter les affirmations suivantes sous forme symbolique en utilisant P, Q et des
	connecteurs logiques.
	• A= « Paul aime le foot mais pas les maths »
	• B = « Paul n'aime ni le foot, ni les maths»
	• C = « Paul aime le foot ou il aime les maths et pas le foot »
	• D = « Paul aime les maths et le foot ou il aime les maths mais pas le foot »

	Donner les valeurs de vérité des propositions suivantes :
	• A = $(\pi = 5)\wedge(2 + 3 = 5)$
	• B = $(\pi = 5)\vee( 2 + 3 = 5)$
	• C = $(\pi=3,14)\Rightarrow (5+6=11)$
	• D=  $(\pi=5)\Rightarrow(2 +3=5)$
	• E = $(4 = 5)\Rightarrow A$
	• F=  $(5+5=10)\Leftrightarrow(\pi=11)$

	Donner les valeurs de vérité des propositions suivantes :
	• A = $(11>0)\wedge(3<2)$
	• B = $(11>0)\vee( 3 <2)$
	• C = $(3>6)\vee (6>20)$
	• D=  $(3<2)\Rightarrow(5=5)$
	• E = $(4 \neq 1)\Rightarrow (4=1)$
	• F=  $(4<5)\Leftrightarrow(10+1=11)$


	On peut montrer qu'une proposition composée est vraie en faisant prendre toutes les valeurs de vérités possibles aux propositions qui la compose et en trouvant sa table de vérité :
	
	Montrons que $(P\wedge Q)\Leftrightarrow(Q\wedge P)$ est vraie quelque soient les valeurs de vérité de P et de Q.
	
			\hline
			\rowcolor{lightgray}
			$P$ & $Q$ & $P\wedge Q$ & $Q \wedge P$ & $(P\wedge Q)\Leftrightarrow(Q\wedge P)$ 
			\hline 
			\rowcolor{white}
			0 & 0 & 0 & 0 & 1 
			\hline
			\rowcolor{white}
			0 & 1 & 0 & 0 & 1 
			\hline
			\rowcolor{white}
			1 & 0 & 0 & 0 & 1 
			\hline\rowcolor{white}
			1 & 1 & 1 & 1 & 1 
			\hline

	Vérifier que la table de vérité de $P\Rightarrow Q$ est la même que celle de $\neg(P)\vee Q$.

	Vérifier que la table de vérité de $P\Leftrightarrow Q$ est la même que celle de $(P\Rightarrow Q)\wedge(Q\Rightarrow P)$.


		Notons $xor$ cet opérateur binaire. $P\ xor\ Q$ est vraie si (et seulement si) une et une seule des 2 propositions est vraie.
			-  	Donner la table de vérité de P xor Q.
			-  	Vérifier que c'est la même que $(P\wedge \neg Q)\vee(\neg P\wedge Q)$
			-  	Vérifier que c'est la même que celle de $(P\vee Q)\wedge(\neg(P\wedge Q))$

	
		-  	Montrer que $\neg (P\wedge Q)\Leftrightarrow (\neg P \vee \neg Q)$
		-  	Montrer que $\neg (P\vee Q)\Leftrightarrow (\neg P \wedge \neg Q)$

	Les propositions suivantes sont vraies quelles que soient les valeurs de vérité de P, Q et R.
	On dit que ce sont des *tautologies*.
	
$(P\wedge Q) \Leftrightarrow(Q\wedge P)$ 		\hspace{4cm}	\=commutativité de $\wedge$  
$(P\vee Q) \Leftrightarrow(Q\vee P)$ 						 	\>commutativité de $\vee$  
$((P\vee Q)\vee R) \Leftrightarrow(P\vee(Q\vee R))$ 			\>associativité de $\vee$  
$((P\wedge Q)\wedge R) \Leftrightarrow(P\wedge(Q\wedge R))$ 	\>associativité de $\wedge$  
$(P\wedge (Q\vee R))\Leftrightarrow((P\wedge Q)\vee(P\wedge R))$ \>distributivité de $\wedge$ sur $\vee$ 
$(P\vee (Q\wedge R))\Leftrightarrow((P\vee Q)\wedge(P\vee R))$ \>distributivité de $\vee$ sur $\wedge$ 
$(P\Rightarrow Q)\Leftrightarrow(\neg P \vee Q)$
$\neg (P\wedge Q)\Leftrightarrow (\neg P \vee \neg Q)$ \> loi de De Morgan
$\neg (P\vee Q)\Leftrightarrow (\neg P \wedge \neg Q)$ \> loi de De Morgan

	
	-  	« Il viendra mardi et il apportera son PC ou bien il viendra mercredi et il apportera son PC»
	se simplifie en :	« Il viendra mardi ou mercredi et il apportera son PC».
	-  	« On n'a pas :  Jean est gentil ou Jean est drôle» peut se réécrire :
			« Jean n'est pas gentil et Jean n'est pas drôle».	

	Simplifier « On n'a pas : Pierre habite Saint Brieuc et Pierre est brun».


## Calcul des prédicats

	
	Le symbole $\forall$ se lit « pour tout» et s'appelle *quantificateur universel*.
	Le symbole $\exists$ se lit « il existe» et s'appelle *quantificateur existentiel*.
	
	Une *variable* est un symbole qui peut prendre plusieurs valeurs.
	
	Un *prédicat* est un énoncé sans valeur de vérité qui contient au moins une variable, et qui devient une proposition en ajoutant un ou des quantificateurs.

		-  	« $x<1$» est un prédicat comportant une variable $x$.
		-  	$\exists x\in R,\ x<1$ est une proposition. Cette proposition est vraie : il existe un nombre réel strictement plus petit que 1 (et même une infinité) : 0 par exemple.
		-  	$\forall x\in\R,\ x<1$ est une autre proposition... fausse ! Tout nombre réel n'est pas strictement plus petit que 1 : 2 par exemple.

	Dans un prédicat à plusieurs variables, quand plusieurs quantificateurs de la même catégorie se suivent, on peut les échanger librement.
	On *ne peut pas* échanger un quantificateur $\exists$ et un quantificateur $\forall$.

		-  	$\forall x\in\R,\ \forall y\in\R,\ \exists z \in\R, x+y<z$ est une proposition vraie : pour tous réels x et y on peut prendre z égal à $x+y+1$.
				On peut échanger les quantificateurs universels : $\forall y\in\R,\ \forall x\in\R,\ \exists z \in\R, x+y<z$ est équivalent à la proposition précédente.
		-  	$\forall x\in\R,\ \exists y \in\R, x<y$ est une proposition vraie mais on ne peut pas échanger les quantificateurs : on obtient :
				$\exists y\in\R,\ \forall x \in\R, x<y$ est fausse : cela voudrait dire qu'il existe un réel $y$ plus grand que tous les autres !

	On obtient la négation d'une proposition quantifiée en changeant les $\exists$ en $\forall$, les $\forall$ en $\exists$ et en changeant le prédicat final par sa négation.

	On considère la propriété P : $$\forall n\in\N,\ \exists k\in\N,\ n=2k$$
	Sa négation est $\neg P$ :  $$\exists n\in\N,\ \forall k\in\N,\ n\neq 2k$$
	P est fausse puisqu'elle affirme que tout entier naturel est divisible par 2 ! Sa négation est vraie : elle affirme qu'il existe un entier naturel qui n'est pas divisible par 2 (3 par exemple).

		-  	Pour prouver qu'une proposition quantifiée par $\forall$ est fausse, il suffit de donner un *contre exemple*.
		-  	Pour prouver qu'une proposition quantifiée par $\exists x...$ est vraie, on peut déterminer la valeur de $x$ qui convient.
		-  	Pour prouver qu'une proposition quantifiée par $\forall$ est vraie on a souvent recours à un raisonnement ou au calcul littéral.
		-  	De même pour prouver qu'une proposition quantifiée par $\exists x...$ est fausse.

		-  	Montrons que $\forall x \in \R,\ \exists y\in \R,\ 3y+1=x$ :
				Soit $x\in\R$ alors $3y+1=x\Leftrightarrow y=\frac{1}{3}(x-1)$. Donc  $\frac{1}{3}(x-1)$ convient.
		-  	Montrons que $\forall x\in\R,\ \exists y\in\R,\ x=y^2$ est fausse :
		 		Prenons $x=-1$. Il n'existe aucun $y\in\R$ tel que $x=y^2$. En effet d'après la règle des signes, $y^2$ est obligatoirement positif.

	Vrai ou faux ? Justifier.
		-  	$\forall n \in \N,\ \forall p \in \N,\ p-n \equiv 0\ [2]$
		-  	$\forall n \in \N,\ \exists p \in \N,\ p-n \equiv 0\ [2]$
		-  	$\exists n \in \N,\ \exists p \in \N,\ p-n \equiv 0\ [2]$
		-  	$\exists n \in \N,\ \forall p \in \N,\ p-n \equiv 0\ [2]$

	Donner les négations des propositions suivantes et dire laquelle est vraie : la proposition ou sa négation.
		-  	$\exists x\in\R,\ 3x=2$
		-  	$\forall x\in\R,\ x=x+1$
		-  	$\forall x\in\R,\ \forall y\in\R, x\leqslant y$
		-  	$\exists x\in\R,\ \forall y\in\R,\ x^2=y$
		-  	$\forall x\in\R,\ \exists y\in\R,\ x^2=y$	

