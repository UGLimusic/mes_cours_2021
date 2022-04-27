
\setcounter{chapter}{2}

\chapter{\large Arithmétique[-1em]\fontsize{35pt}{42pt}\selectfont\titlefont Écriture des « réels»}
\introduction{Tout cela est-il bien réel ?}

## Écriture décimale et arrondi
On sait que tout nombre réel admet une écriture décimale :
	-  	«  un et demi » s'écrit 1,500000\ldots\ et on enlève les zéros inutiles, cela fait 1,5.
	-  	« trois septièmes » s'écrit $0,4285714285714285714285714\ldots$ et pour insister sur le fait que le motif 428571
			se répète indéfiniment on écrit $0,\underline{428571}$.
	-  	$\pi$ a une écriture décimale qui commence par $3,14159265359$ mais son écriture décimale comporte une infinité de chiffres
	*sans
	qu'aucun motif ne se répète*.

On est souvent amenés à *arrondir* les nombres réels : soit le nombre n'est « pas très grand» et on ne veut garder que quelques chiffres
après la virgule, soit il est « plutôt grand» et on ne veut garder que quelques chiffres significatifs :


On veut arrondir $\frac{3}{7}$ à $10^{-3}$ près, c'est-à-dire à 3 chiffres après la virgule.
						Il y a trois possibilités :
							-  	**Arrondi par défaut** : On « coupe» après le troisième chiffre :
									$$\frac{3}{7}\approx 0,428\quad\textrm{à }10^{-3}\textrm{ près par défaut.}$$
							-  	**Arrondi par excès** : On « coupe» après le troisième chiffre et on ajoute $10^{-3}$,
									c'est-à-dire un *millième* :
																$$\frac{3}{7}\approx 0,429\quad\textrm{à }10^{-3}\textrm{ près par excès.}$$
							-  	**Arrondi au plus près** : On regarde le chiffre immédiatement après le troisième (celui qui correspond
									 à $10^{-4}$). Si c'est 0,1,2,3 ou 4, on prend l'arrondi par défaut, si c'est 5,6,7,8 ou 9, on prend l'arrondi
									par excès.
									$$\frac{3}{7}\approx 0,429\quad\textrm{à }10^{-3}\textrm{ au plus proche.}$$

	Utiliser la méthode 1 pour déterminer
		-  	L'arrondi de $\frac{13}{11}$ à $10^{-2}$ près par défaut
		-  	L'arrondi de $\sqrt{2}$ à $10^{-4}$ près par excès.
		-  	L'arrondi de $\frac{149}{999}$ à $10^{-3}$ au plus près.
On veut arrondir 273692,291 à $10^{4}$, c'est à dire à la dizaine de milliers.
Là encore il y a trois possibilités. On commence par remarquer que le chiffre correspondant à $10^4$ est le 7.
	-  	**Arrondi par défaut** : On remplace tous les chiffres à droite du 7 par des zéros. La partie décimale disparaît.
	$$ 273692,291\approx 270000\quad\textrm{à }10^{4}\textrm{ près par défaut.}$$
	-   	**Arrondi par défaut** : On prend l'arrondi par défaut et on ajoute $10^4$.
		$$ 273692,291\approx 280000\quad\textrm{à }10^{4}\textrm{ près par excès.}$$
	-  	**Arrondi au plus près** : On regarde le chiffre immédiatement après celui de $10^4$ (celui qui correspond
									 à $10^{3}$). Si c'est 0,1,2,3 ou 4, on prend l'arrondi par défaut, si c'est 5,6,7,8 ou 9, on prend l'arrondi
									par excès.
			$$ 273692,291\approx 270000\quad\textrm{à }10^{4}\textrm{ au plus proche.}$$

	Utiliser la méthode 2 pour déterminer
		-  	L'arrondi de $38564526$ à $10^3$ près par défaut
		-  	L'arrondi de $281 564 526$ à $10^8$ près par excès.
		-  	L'arrondi de $9524$ à $10^{3}$ au plus près.

## Écriture dyadique et arrondi

### Écriture dyadique
Lorsqu'on écrit un nombre décimal tel que $3,719$, on a l'égalité suivante:
$$3,719=3\times 10^0+7\times 10^{-1}+1\times 10^{-2}+9\times 10^{-3}$$

Il est possible de faire la même chose en base 2 : on ajoute des puissances de 2 d'exposants négatifs.

On considère le nombre $n=(1010,011)_2$. Quelle est son écriture décimale ?
	-  	Sa partie entière est $(1010)_2$, ce qui vaut 10.
	-  	Sa partie décimale est
	$(0,011)_2$ \= $=2^{-2}+2^{-3}$
				\>  $=0,25+0,125$
				\>	$=0,375$
Ainsi $$n=10,375$$
	Utiliser la méthode précédente pour déterminer les écriture décimales de
		-  	$(0,101)_2$
		-  	$(11,01)_2$
		-  	$(1111,1111)_2$

On veut l'écriture du nombre $5,75$ en base 2. Pour la partie entière, c'est simple : $$5=(101)_2$$
Pour la partie décimale, on remarque que
0,75 \= 0,5+0,25
	\> 	$\frac{1}{2}$ +$\frac{1}{4}$
	\>	$=2^{-1}+2^{-2}$
Ainsi $$0,75 = (0,11)_2$$
Finalement $$5,75=(101,11)_2$$
	Utiliser la méthode précédente pour déterminer les écriture dyadiques de
		-  	$3,25$
		-  	$12,625$
		-  	$7,8125$

Un nombre décimal n'a pas généralement une écriture dyadique « qui se termine».
Par exemple 0,1 (qui est pourtant le nombre décimal le plus simple auquel on puisse penser) s'écrit
$$0,1 = (0,\ 0001\ 1001\ 1001\ \underline{1001} ...)_2$$

### Arrondi

Pour arrondir un nombre en base 2, on fait pareil qu'en base 10 :


	-  	Arrondissons $n=(1101\ 1010)_2$ à $2^4$ au plus proche :
			L'arrondi par défaut est $(1101\ 0000)_2$ mais comme le bit juste à droite du bit de $2^4$ est un 1, il faut rajouter $2^4$ à
			notre valeur arrondie, pour avoir la valeur par excès qui, elle, est plus proche :
 			 &   &   & $_1$ &  &  &  &  &  
			 & 1 & 1 & 0 & 1 & 0 & 0 & 0 & 0 
			+ & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 
			\hline
			 =& 1 & 1 &  1& 0 & 0 & 0 & 0 & 0 

			Ainsi $n\approx (1110\ 0000)_2$ à $2^4$ au plus proche.
	-  	Pour les nombres dyadiques, c'est la même chose. Arrondissons $m=(11,\ 0011\ 1001)_2$ à $2^{-5}$ au plus proche :
			Le bit de $2^{-6}$ est un 0, donc la bonne valeur arrondie est par défaut :
				$$m\approx(11,\ 0011\ 1)_2\textrm{ à }2^{-5}\textrm{ au plus proche.}$$

Quand on nous demande d'arrondir sans préciser, on convient que c'est au plus proche.

	Utiliser la méthode précédente pour déterminer
		-  	L'arrondi de $(1101\,1010)_2$ à $2^3$ près par défaut.
		-  	L'arrondi de $(1,1110\,101)_2$ à $2^{-3}$ près par excès.
		-  	L'arrondi de $(0,001)$ à $2^{-1}$ au plus proche.


\exostart

		-  	$(101,1)_2$
		-  	$(1,011)_2$
		-  	$(0,1111\ 111)_2$ en remarquant que c'est « $(111\ 1111)_2$ divisé par $2^7$.
	Écrire en base 2 les nombres suivants :
		-  	3,5
		-  	7,75
		-  	27,625

		-  	Quel est l'arrondi de $(10,011)_2$ à $(0,1)_2$ près ?
		-  	Quel est l'arrondi de $(1 1011)_2$ à $(100)_2$ près ?
		-  	Quel est l'arrondi de $(0,0010 11)_2$ à $(0,0001)_2$ près ?



		-  	Quel est l'arrondi de $(11,0101)_2$ à $2^{-2}$ près ?
		-  	Quel est l'arrondi de $(1011 1011)_2$ à 32 près près ?


	On aimerait trouver l'écriture dyadique (illimitée) de $\dfrac{1}{3}$.
	On note donc $$\dfrac{1}{3}=(0,a_1a_2a_3\ldots)_2$$
	où $a_i$ vaut 1 ou 0.
		-  	Expliquer pourquoi $a_1$ vaut *nécessairement 0*.
		-  	On note $x=\frac{1}{3}$. Montrer que $x$ vérifie $4x=1+x$.
		-  	Quelle est l'écriture dyadique de $4x$ ?
		-  	Quelle est celle de $1+x$ ?
		-  	En écrivant que ces 2 écritures représentent le même nombre, en déduire que $$\dfrac{1}{3}=(0,0101\ 0101\ldots )_2$$
