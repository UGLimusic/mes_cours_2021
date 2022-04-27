\chapter*{Matrices}
## Notion de matrice

Une matrice $A$ peut être vue comme « un tableau de nombres».
Supposons qu'elle comporte n lignes et p colonnes (n et p sont des entiers plus grands que 1), on la note ainsi
    a_{11}      & a_{12}&\cdots & a_{1p}  
    a_{21}  & a_{22}& \cdots & a_{2p}       
    \vdots 	& \vdots & \ddots & \vdots  
    a_{n1}  & a_{n2}    & \cdots & a_{np}
L'élément qui se situe à la i\eme ligne et à la j\eme colonne est noté $a_{ij}$. On l'appelle également *coefficient*.

**Attention** : les indices des lignes et des colonnes commencent à 1 (et non à zéro comme dans la plupart des langages informatiques).

Pour résumer l'écriture précédente on écrit 
$$A=(a_{ij})_{\substack{1\leqslant i\leqslant n1\leqslant j\leqslant p}}$$

On dit aussi que $A$ est une matrice $n\times p$. Si $n=p$ on dit que $A$ est une *matrice carrée d'ordre $n$*.

					    1      & 2 & 4  
					    -3  & 5 & 0
						    2,4      & 7 & 4 & -1  
						    -3  & 5 & 10,1 & 1 
						    0,01 & 3 & 12 & 100
							    4      & 2 
							    2  &8
							
	

						    -4      & 7,6 & 4 & -1 & 12  
						    8 & -3  & 5,7 & 101 & 1 
						    12 & 0,01 & 3 & 12 & 1
						
Donne les valeurs de $e_{12}$, $e_{21}$, $e_{35}$ et $e_{24}$.

Le script Python suivant permet de générer une matrice $n\times p$ avec des coefficients entiers aléatoires compris entre -100 et 100.


\pythonfile{mat_alea.py}

	-  Écris complètement la matrice suivante : $M=(m_{ij})_{\substack{1\leqslant i\leqslant 31\leqslant j\leqslant 5}}$ où $m_{ij}=i$ si i=j et 0 sinon.
	-  	Écris complètement la matrice suivante : $M=(m_{ij})_{\substack{1\leqslant i\leqslant 41\leqslant j\leqslant 5}}$ où $m_{ij}=0$ si i<j et 1 sinon.
	-  	Écris complètement la matrice suivante : $M=(m_{ij})_{\substack{1\leqslant i\leqslant 31\leqslant j\leqslant 3}}$ où $m_{ij}=1$ si $i+j$ est pair et 0 sinon.
	-  bonus : écris des programmes Python qui génèrent ces matrices.

	-  	Une matrice dont tous les coefficients sont nuls est dite *nulle* (c'est « un tableau de zéros»);
	-  	la matrice *carrée d'ordre $n$* dont tous les éléments sont nuls sauf ceux de la *diagonale* (c'est-à-dire ceux qui s'écrivent $a_{ii})$ qui valent 1 s'appelle *la matrice identité d'ordre $n$* et se note $I_n$.

La matrice identité $I_3$ est
1&0&0
0&1&0
0&0&1

## Opérations sur les matrices

Soient $A$ et $B$ deux matrices $n\times p$, on note $A+B$ la matrice $n\times p$ obtenu en ajoutant les coefficients correspondants de $A$ et de $B$ :

    a_{11}      & \cdots & a_{1p}  
 
    \vdots 	& \ddots & \vdots  
    a_{n1}      & \cdots & a_{np}
    b_{11}      & \cdots & b_{1p}  
   
    \vdots 	& \ddots & \vdots  
    b_{n1}      & \cdots & b_{np}
    a_{11} +b_{11}     & \cdots & a_{1p}+b_{1p}  
  
    \vdots 	& \ddots & \vdots  
    a_{n1}+n_{n1}      & \cdots & a_{np}+b_{np}

				3&1
				4&7
				-2&8
				2&5
				1&-3
				-5&9
5&65&4-7&17
**Attention :** on ne peut ajouter deux matrices que si elles ont les mêmes dimensions (c'est-à-dire même nombre de lignes et même nombre de colonnes).
Soient $A$ une matrice $n\times p$ et $k$ un nombre réel, on note $kA$ la matrice $n\times p$ obtenue en multipliant chaque coefficient de $A$ par $k$ :

    a_{11}      & \cdots & a_{1p}    
    \vdots 	& \ddots & \vdots  
    a_{n1}      & \cdots & a_{np}
    k\times a_{11}      & \cdots & k\times a_{1p}       
    \vdots 	& \ddots & \vdots  
   k\times a_{n1}      & \cdots &k\times a_{np}
$$

				8&3&1
				4&7&2
				-2&1&8
				40&15&5
				20&35&10
				-10&5&40


La propriété suivante énonce quelques résultats utiles pour calculer.
Soient $A$, $B$ et $C$ trois matrices de mêmes dimensions et $k$ et $k'$ 2 réels.
	-  	$A+B = B+A$
	-  	$(A+B)+C = A+(B+C)$
	-  	$k(A+B) = kA + kB$
	-  	$(k+k')A = kA+k'A$

1&23&-4
11&10-9&7
-3&-25&-5

Montrer que $B-2A+3C$ est une matrice nulle.


Soient $A$ une matrice $n\times p$ et $B$ une matrice $p\times q$ (le nombre de colonnes de la 1\ere est égal au nombre de lignes de la 2\eme) alors il est possible de définir la matrice $C=A\times B$, produit de $A$ par $B$.
C'est une matrice $n\times q$ dont les coefficients sont ainsi :
    b_{11}   &\cdots   &\color{orange@color}b_{1j}& \cdots & a_{1q}  
    \vdots 	& \ddots &\color{orange@color}\cdots&\dots & \vdots  
    b_{k1} & \cdots & \color{orange@color}b_{kj}&\cdots & b_{kq}
        \vdots 	& \cdots &\color{orange@color}\cdots&\ddots & \vdots  
    b_{p1}    &\cdots  &\color{orange@color}b_{pj} & \cdots &b_{pq}

    a_{11}   &\cdots   &\cdots& \cdots & a_{1p}  
    \vdots 	& \ddots &\cdots&\dots & \vdots  
\color{vertfonce@color}    a_{i1} & \color{vertfonce@color}\cdots &\color{vertfonce@color} a_{ik}&\color{vertfonce@color}\cdots & \color{vertfonce@color}a_{ip}
        \vdots 	& \cdots &\cdots&\ddots & \vdots  
    a_{n1}    &\cdots  & \cdots & \cdots &a_{np}
    c_{11}   &\cdots   &\cdots& \cdots & c_{1q}  
    \vdots 	& \ddots &\cdots&\dots & \vdots  
   \vdots & \cdots & \color{red}c_{ij}&\cdots & \vdots
        \vdots 	& \cdots &\cdots&\ddots & \vdots  
    c_{n1}    &\cdots  & \cdots & \cdots &c_{nq}
{\LARGE$$ {\color{red}c_{ij}} = {\color{vertfonce@color}a_{i1}}\times {\color{orange@color}b_{1j}}+ {\color{vertfonce@color}a_{i2}}\times {\color{orange@color}b_{2j}}+\ldots+ {\color{vertfonce@color}a_{ip}}\times {\color{orange@color}b_{pj}}$$}


1&3 & -2 5 &-3&4
-5 & 1 & 0 & 22& 1 & -1 & -83 &4 & 0 & 9
 -5 & 1 & \color{orange@color}0 & 22& 1 & \color{orange@color}-1 & -83 &4 & \color{orange@color}0 & 9
1&3 & -2 \color{vertfonce@color}5 &\color{vertfonce@color}-3&\color{vertfonce@color}4
-5&-4&-3&-40-19&18&\color{red}3&70
Par exemple, pour calculer $c_{33}$, on fait ${\color{vertfonce@color}5}\times {\color{orange@color}0}+ {\color{vertfonce@color}(-3)}\times {\color{orange@color}(-1)}+ {\color{vertfonce@color}4}\times {\color{orange@color}0}={\color{red}3} $.

**Attention :** 
	-  	on ne peut multiplier $A$ par $B$ que si le nombre de colonnes de $A$ est égal au nombre de lignes de $B$;
	-  	ce n'est pas parce qu'on peut calculer $A\times B$ qu'on peut calculer $B\times A$ : les matrices de l'exemple précédent ne permettent pas de calculer $B\times A$ car le nombre de colonnes de $B$ n'est pas égal au nombre de lignes de $A$:
	\newpage
	 	1&3 & -2 \color{vertfonce@color}5 &\color{vertfonce@color}-3&\color{vertfonce@color}4
		 -5 & 1 & \color{orange@color}0 & 22& 1 & \color{orange@color}-1 & -83 &4 & \color{orange@color}0 & 9
	-  pour pouvoir calculer $A\times B$ et $B\times A$ il faut que ces deux matrices soient carrées d'ordre $n$ et *en général* on n'a pas $A\times B=B\times A$.

	1&23&0
	5&20&3
	
	Calculer $AB$ et $BA$.
	
		-4&6-3&5
		8&-105&-7


$A$, $B$ et $C$ sont des matrices.
Lorsque les opérations sont possibles (bonnes dimensions des matrices) on a :
	-  	$A(BC)=(AB)C$;
	-  	$(A+B)C=AC+BC$;
	-  	$A(B+C)=AB+AC$.
Soit $k$ un nombre réel alors on a également $A\times kB=kAB$.

Si $A$ est *carrée d'ordre* $n$ on a
	-  	$AI_n=I_nA=A$ où $I_n$ est la matrice identité d'ordre $n$.
	-  	$A\times 0=0\times A=0$ en notant 0 la matrice carrée d'ordre $n$ nulle.

## Exemple concret d'utilisation

Imaginons une école qui forme des ingénieurs en informatique, avec seulement 3 matières.
Trois élèves de première année ont obtenu les résultats suivants :

**Résultats pour le premier trimestre**[1em]

\hline
 & Maths & Physique & Info
\hline
Adam & 12 & 8 & 16
\hline
Bertrand & 18 & 14 & 12
\hline
Charles & 5 & 20 & 15
\hline

**Résultats pour le deuxième trimestre**[1em]

\hline
 & Maths & Physique & Info
\hline
Adam & 10 & 10 & 14
\hline
Bertrand & 18 & 12 & 14
\hline
Charles & 7 & 14 & 17
\hline

Ces deux tableaux peuvent s'écrire matriciellement 
12 & 8 & 16 
18 & 14 & 12 
5 & 20 & 15 
10 & 10 & 14 
18 & 12 & 14 
7 & 14 & 17 

Pour calculer les moyennes mensuelles des élèves « en une fois» on peut définir $M=0,5(S_1+S_2)$: 

12 & 8 & 16 
18 & 14 & 12 
5 & 20 & 15 
10 & 10 & 14 
18 & 12 & 14 
7 & 14 & 17 

22 & 18 & 30 
36 & 16 & 26 
12 & 34 & 32 

11 & 9 & 15 
18 & 8 & 13 
6 & 17 & 16 

Le coefficient des mathématiques est 1, celui de la physique est 2 et celui de l'informatique est 5.
Pour passer en deuxième année, il faut un total de points supérieur ou égal à 120.

125

Les points des élèves sont donnés par la matrice $$P=MC$$
11 & 9 & 15 
18 & 8 & 13 
6 & 17 & 16 
125

104109120

Ainsi seul Charles est admis à passer en 2\eme année.

## Matrices inversibles et systèmes

Soit $A$ une matrice **carrée d'ordre $n$**. S'il existe une matrice $B$ d'ordre $n$ telle que 
$$AB = I_n\qquad\text{ou}\qquad BA=I_n$$

alors automatiquement les deux égalités sont vérifiées, $B$ est nécessairement *unique* et on dit alors que $B$ *est l'inverse de $A$*. De manière symétrique $A$ est également l'inverse de $B$ si bien qu'on dit que $A$ et $B$ sont inverses l'une de l'autre.

On note ceci $A=B^{-1}$ ou, ce qui revient au même, $B=A^{-1}$.

-1&2-2&3
3&-22&-1
3&-22&-1
-1&2-2&3
 1&00&1
3 & -2&1
-2&2&-1
1&-1&1
1& 1&0
1&2&1
0&1&2

1 & 2 2 & 4 


\newcolumntype{C}{>{{}}c<{{}}} % for columns with binary operators
\renewcommand\vv{\multicolumn{1}{c}{\vdots}}
On considère un *système de $n$ équations à $n$ inconnues* :

$$\left\{
\setlength{\arraycolsep}{0pt}
a_{11} & + & a_{12} & + & \cdots & + & a_{1n} & = & b_1 
a_{21} & + & a_{22} & + & \cdots & + & a_{2n} & = & b_2 
\vv    &   & \vv    &   &        &   & \vv    &   & \vdots
a_{n1} & + & a_{n2} & + & \cdots & + & a_{nn} & = & b_n 

On connaît tous les nombres $a_{ij}$ et tous les $b_i$, et on veut trouver les valeurs des inconnues $x_i$.

Ce système peut se réécrire de manière matricielle :

    a_{11}      & a_{12}&\cdots & a_{1n}  
    a_{21}  & a_{22}& \cdots & a_{2n}       
    \vdots 	& \vdots & \ddots & \vdots  
    a_{n1}  & a_{n2}    & \cdots & a_{nn}
    x_{1}        
    x_2      
    \vdots  
    x_n
    b_{1}        
    b_2      
    \vdots  
    b_n

Ou encore :
$$AX=B$$

Si la matrice $A$ est inversible (en pratique ce sera toujours le cas parce qu'on nous donnera sa matrice inverse ou bien parce qu'on l'aura déterminée à l'aide de la calculatrice) alors, on peut reprendre l'égalité précédente et écrire : $A^{-1}AX=A^{-1}B$, ce qui donne $I_nX=A^{-1}B$. En définitive on a $$X = A^{-1}B$$

Ainsi pour trouver les valeurs des inconnues $x_i$, on effectue simplement le produit matriciel $A^{-1}B$ : chacune de ses lignes nous donne la valeur du $x_i$ correspondant.

Pour savoir comment utiliser la calculatrice, regarder ici :
	-  	modèles CASIO : \url{https://youtu.be/yjvQx13Vhlk}
	-  	modèles Texas Instrument : \url{https://youtu.be/rxDxBnIwaGo}

On considère le système suivant : \systeme{2x+5y+2z=1,
5x-3y-2z=2,
-x+2y+z=-3}

Il peut se réécrire de manière matricielle :

2 & 5 & 2 
5 & -3 & -2
-1 & 2 & 1
x  y  z
1  2  -3

Appelons $A$ la matrice carrée du membre de gauche. On détermine que $A$ est inversible avec la calculatrice et que son inverse est 
1 & -1 & -4 
-3 & 4 & 14
7 & -9 & -31
On a donc

x  y  z
1 & -1 & -4 
-3 & 4 & 14
7 & -9 & -31
1  2  -3
C'est à dire, en effectuant le produit dans le membre de droite 

x  y  z
11-3782

On a donc résolu le système : \systeme{x=11,y=-37,z=82}
	-  Résous le système suivant : \systeme{x+2y = 15,-3x+3y = -6}
