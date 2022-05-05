---
title: Corrigé de l'évaluation du 29 avril 2022
author: NSI2
geometry:
- margin = 1cm
fontsize: 10pt
mainfont: Fira Sans Light
mainfontoptions:
- Numbers=Lowercase
- Numbers=Proportional
monofont: Fira Mono
mathfont: Fira Math Light
linestretch: 1.2
papersize: a4
---

# Exercice 1

_Absolument rien de dur dans cet exercice !_

## Partie A : Réseau

1. Le terme *architecture* fait référence au matériel. Lors d'une communication, les données sont découpées en _paquets_
   .

   Le terme qui désigne l'ensemble des règles de communication utilisées pour réaliser un service particulier sur le
   réseau
   est _protocole_.

2. L'élément A joue le rôle de _passerelle_ entre un réseau local et le réseau global : c'est un _routeur_.
   B et C sont quant à eux des _switch_.
3. Le poste 3 est sur le réseau local, 192.168.11.0, donc la ligne peut être :

   | **Matériel** | **Adresse IP**    | **Masque** | **Passerelle** | 
      |----------|---------------|--------|------------|
   | Poste 3  | 192.168.11.xx | 255.255.255.0 | 192.168.11.1 |

   où xx est n'importe quel nombre compris entre 2 et 9 inclus, et 22 et 253 inclus.

   22 semble être le choix logique.

## Partie B : Routage réseaux

1. Les réseaux _directement connectés_ à R1 sont ceux qui sont à distance nulle. Leurs IP sont
    - 10.0.0.0
    - 172.16.0.0
    - 192.168.0.0

2. Il suffit de repérer à quels réseaux les adresses IP appartiennent :

   | **Adresse IP destination** | **Interface Machine ou Port** |
       |-------------------------------|---------------------------| 
   | 192.168.1.55            | 192.168.0.1                   |  
   | 172.18.10.10            | 172.15.0.1                    |

3. Il s'agit bien du protocole RIP puisqu'on a aucune information sur les débits des connexions.

   | **Routeur** | **Métrique** | **Route** |
   |-------------| --- | --- | --- |
   | R2 | 0 | R1 - R2 |
   | R3 | 0 | R1 - R3 |
   | R4 | 1 | R1 - R2 - R4 |
   | R5 | 1 | R1 - R3 - R4 |
   | R6 | 1 | R1 - R3 - R6 |
   | R7 | 2 | R1 - R2 - R4 - R7 |

   Pour la ligne de R7 on aurait tout aussi bien pu indiquer R1 - R3 - R6 - R7.

# Exercice 2

1. La liaison n'est pas valide car dans cette liste figure `["Luchon", "Muret"]`, qui n'est pas une _liaison directe_.
2. Voici la liste :

  ```python
liaisonJoueur1 = [["Tarbes", "St Gaudens"],
                  ["Toulouse", "Castres"],
                  ["Toulouse", "Castelnaudary"],
                  ["Castres", "Mezamet"],
                  ["Castelnaudary", "Carcassonne"]]                                
   ```

3. a) Voici l'assert :

  ```python 
        assert listeLiaisons, "la liste est vide"
  ```

b) `construireDict(listeLiaison)` renvoie

  ```python
        {
    'Toulouse': ['Muret', 'Montauban'],
    'Gaillac': ['St Sulpice'],
    'Muret': ['Pamiers']
}
  ```

Ce n'est pas la bonne valeur, car il manque des clés.

En fait, telle que la fonction est programmée, les villes figurant en deuxième position ne sont jamais mises en clé.

c) On peut procéder de plusieurs manières.

On peut rendre le code symétrique en rajoutant ce bloc en ligne 16 :

  ```python
    if not villeB in Dict.keys():
    Dict[villeB] = [villeA]
else:
    destinationsB = Dict[villeB]
    if not villeA in destinationsB:
        destinationsB.append(villeA)
  ```

Toutefois, une solution bien plus courte et élégante consiste à remplacer la ligne 7 par :

  ```python
  for liaison in listeLiaisons + [[y, x] for [x, y] in listeLiaisons]:
  ```

Ce qui « symétrise » la liste sur laquelle on itère.

# Exercice 3

1. Le langage utilisé est le SQL (_Simple Query Language_).
2. `ATOMES` a pour attributs

- Z : INT
- nom : VARCHAR
- Sym : VARCHAR
- L : INT
- C : INT
- masse_atom : DECIMAL

  `VALENCE` a pour attributs

- Col : INTEGER
- Couche : TEXT

  Les attributs Z, nom et Sym peuvent jouer le rôle de clé primaire car chacun de ces attributs identifie de manière
  unique un élément.
  C peut être une clé étrangère faisant réference à Col, clé primaire de `VALENCE`.

  On a le schéma suivant :

```sql
ATOMES
(Z INT, nom VARCHAR , Sym VARCHAR , L INT, 
       -----                               

       C INT, masse_atom DEC )
       ~~~~~

VALENCE(COL INT, Couche TEXT)
        -------
```

3. On a la table suivante pour la requête a)

| nom       |
|-----------|
| aluminium |
| argon     | 
| chlore    |
|  magnesium|
|sodium|
|phosphore|
|soufre| 
|silice| 

et celle-ci pour la requête b)

|c|
|---|
| 1 |
| ...|
|18| 

(toutes les valeurs de 1 à 18 sont présentes).

4.
```sql
SELECT  nom,masse_atom FROM ATOMES;

SELECT Sym FROM ATOMES
JOIN VALENCE ON ATOMES.C = VALENCE.col
WHERE VALENCE.couche = "s";
```

5. 
```sql
UPDATE ATOMES
SET masse_atom = 39.948
WHERE Sym = "Ar";
```

