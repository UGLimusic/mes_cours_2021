### Question A-1
La fonction `transform` prend en entrée une chaine de caractères « brute » et
la convertit en liste de 4 entiers, valeur qu'elle renvoie.

### Question A-2
```
Fonction indic(combi, propos)
ARGUMENTS       combi, propos : tableaux d'entiers à une dimension
TYPE RENVOYÉ    tableau d'entiers à une dimension
ROLE            détermine le nombre de chiffres corrects bien placés et mal placés
VARIABLES       i, j, bPlace, mPlace : entiers
                res : tableau d'entiers à une dimension
DébutFonction
    bPlace ← 0
    mPlace ← 0
    Pour i allant de 0 à 3 # parcours du tableau propos
        Pour j allant de 0 à 3 # parcours du tableau combi
            Si propos[i]=combi[j]
                Si i=j
                    bPlace ← bPlace + 1
                Sinon
                    mPlace ← mPlace + 1
               FinSi
            FinSi
        FinPour
    FinPour
    res = [ bPlace, mPlace ]
    Renvoyer res
FinFonction
```

### Question A-3

```
VARIABLES nb_coups, bp, mp  : entiers
          proposition_str   : chaine de caractères
          proposition_lst   : liste
          combi             : liste

nb_coups ← 0
bp ← 0
mp ← 0
combi ← combinaison() # Pas obligé
TantQue bp < 4 et nb_coups < 8
    nb_coups ← nb_coups + 1
    proposition_str ← Saisir("Entrer votre combinaison")
    proposition_lst ← transform(proposition_str)
    bp, mp ← indic(combi, proposition_lst)
    Affiche "Bien placés :", bp
    Affiche "Mal placés:", mp
FinTantQue
Si bp = 4
    Affiche "Gagné en", nb_coups, "coups."
Sinon
    Afficher "Perdu, la solution était", combi
FinSi
```

### Question A-4 (bonus)

```
Fonction genere_combinaison()
VARIABLES   i,j : entiers
            resultat : liste
DébutFonction
    resultat ← liste vide
    Pour i allant de 0 à 3
        h = entier_aleatoire_entre(0, 7)
        TantQue h est dans resultat
            h = entier_aleatoire_entre(0, 7)
        FinTantQue
        resultat.ajouter(h)
    Renvoyer resultat
FinFonction
```