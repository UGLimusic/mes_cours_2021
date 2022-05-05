---
title: Corrigé du CCF sur l'ISSN
author: NSI2
geometry:
- margin = 2cm
fontsize: 12pt
mainfont: Fira Sans Light
mainfontoptions:
- Numbers=Lowercase
- Numbers=Proportional
monofont: Fira Mono
mathfont: Fira Math Light
linestretch: 1.2
papersize: a4
---


### Question A-1

On effectue le calcul :

$8\times 0+7\times 3+6\times 9+5\times 8+4\times 1+3\times 1+2\times 6 = 134$.

Donc $N=134$. 

Alors $r=134\mod 11 = 2$ et la clé est $11-2=9$.

Donc ce numéro est valide.

Pour compléter l'ISSN 0373-800 on fait pareil :

$8\times 0+7\times 3+6\times 7+5\times 3+4\times 8+3\times 0+2\times 0 = 110$.

Donc $N=110$. 

Alors $r=110\mod 11 = 0$ et la clé est $0$.

Donc ce numéro ISSN complété est 0373-8000.

### Question A-2

On n'a réécrit que la partie utile de l'algorithme :

```
Début
    N ← 0
    m ← 8
    Pour i allant de 0 à 6
        N ← N + m * int(code7[i])
        m ← m - 1
    FinPour
    Renvoyer N
Fin
```

Voici la traduction en Python :

```python
def calcN(code7: str) -> int:
    N = 0 # on initialise N à 0
    m = 8 # on commence par multiplier par 8
    for i in range(7):  # pour parcourir code7
        N += m * int(code7[i])  # on rajoute la bonne valeur
        m -=1 # m "descend"
    return N # on renvoie le résultat
```


### Question A-3

On écrit l'algorithme en Python
```python
def calcCle(N: int) -> str:
    r = N % 11 # on calcule le reste
    if not r:
        return '0'  # comme dit, s'il vaut 0 on renvoie '0'
    elif r == 1:
        return 'X' # Sinon s'il vaut 1 on renvoie 'X'
    else:
        return str(11 - r) # Sinon cela
```
### Question A-4

De même

```python
def ISSNok(code8: str) -> bool:
    code7 = code8[:7] # On ne prend que les chiffres sans la clé
    cle = code8[7] # on stocke la clé
    N = calcN(code7) # on calcule N pour les 7 premiers chiffres
    if cle == calcCle(N):   # on vérifie si la clé calculée correspond
        return True  # si oui c'est bien
    else:
        return False # sinon ce n'est pas bien
```

### Question A-5

De même
```python
def bonus(code8:str) -> None:
    code6= code8[1:7] # On ne garde que les 6 chiffres, sans les extrémités 
    for i in range(10):  # i va parcourir toutes les valeurs de 0 à 9
        code_variant = str(i)+code6 # on forme un code de 7 chiffres commençant par i
        print(f"Pour {code_variant} on trouve une  \
        clé de {calcCle(calcN(code_variant))}.")  # on affiche la clé du code obtenu
```
