---
title: Protocoles de routage

date: 3 mars 2022 
Author: NSI2 
transition: convex 
theme : moon
...

# Situation

---

Lors d'une communication *via* un réseau, nous allons distinguer 3 éléments :

- une machine appelée *client* doit envoyer une information à une autre machine ;
- cette deuxième machine s'appelle un *serveur*.

---

Les termes *client* et *serveur* sont très larges et peuvent en fait

- désigner une *machine* aussi bien qu'une *application* s'exécutant sur cette machine ;
- alterner au cours du temps (le client devient serveur et vice-versa).

--- 

On a vu en classe de première que lors de la communication l'information est découpée en de multiples paquets de petite
taille.

Ces paquets doivent arriver à destination.

---

Le troisième élément de la communication sont les *routeurs*.

Ce sont eux qui acheminent les paquets au sein du réseau.

---

Ils peuvent être de deux types :

- *routeurs d'accès* lorsqu'ils sont en *bordure de réseau*, c'est-à-dire qu'ils sont directement interfacés avec un
  réseau
  *local* ;

- *internes* sinon.

---

Voici un schéma qui montre la *topologie* d'un réseau, c'est-à-dire son architecture.

---

![un exemple de réseau](img/topo1.svg){width=100%}

---

## Explications sur les paires sous-réseau / masque

---

Une *paire sous-réseau / masque* est composée

- de l'adresse IP du réseau, notée sur 4 octets, soit 32 bits ;
- du nombre de bits qui correspondent à la partie fixe des IP du réseau.

---

Par exemple, le réseau local du client est 192.168.1.0/24 ce qui veut dire que :

- l'adresse IP du réseau est 192.168.1.0 ;
- les 24 bits (dans le sens de la lecture) sont fixes.

--- 

Puisque qu'une adresse IP est codée sur 32 octets, cela veut dire que seuls les 8 derniers bits (c'est-à-dire le dernier
octet) peuvent varier.

L'ensemble des IP de ce réseau est donc

- 192.168.1.0 : l'IP du réseau même ;
- 192.168.1.x : l'IP des machines du réseau, avec $1\leqslant x\leqslant 254$ (soit 254 machines au total) ;
- 192.168.1.255 : l'IP du réseau dédiée à la diffusion en masse (*broadcast*).

---

### Exemple détaillé

Une machine a pour IP 172.24.245.25.

On sait que son réseau est de la forme x.x.x.x / 16.

On aimerait retrouver :

- l'adresse IP du réseau ;
- l'adresse de broadcast du réseau.

---

Le « / 16 » indique que les 16 premiers bits sont fixes, les autres pouvant varier.

- En binaire, cela nous donne un *masque réseau* de 16 uns suivi de 16 zéros;
- Cela fait <br>

1111 1111 1111 1111 0000 0000 0000 0000 ;

- Sous format IP, on obtient un masque réseau de 

255.255.0.0 ;

---

Pour trouver l'adresse du réseau, on doit faire un « et bit à bit » entre l'adresse IP de la machine et le masque
réseau.

Donc, *a priori* il faut écrire 172.24.245.25 en binaire.

Mais en fait vu le masque, les 2 premiers octets ne changent pas et les 2 derniers seront nuls

L'adresse du réseau est donc 174.25.0.0.

---

Le fait que le masque soit 255.255.0.0 autorise $2^{16}$ adresses IP au sein du réseau.

De 174.25.0.0 à 174.25.255.255.

Cette dernière IP est dédiée au *broadcast*.


---

## Un réseau en détail

---

Le réseau comprenant R1 et R3 a pour adresse 10.0.1.0/30 : il ne reste donc que 2 bits libres pour adresser les
machines, soit 4 possibilités.

---

Si on enlève l'adresse réseau 10.0.1.0 et l'adresse *broadcast* 10.0.1.3 il reste 2 IP, une pour chaque routeur.

---

Ainsi par exemple

- R1 peut avoir l'IP 10.0.1.1 ;
- R3 aura dans ce cas l'IP 10.0.1.2 ;
- ou l'inverse.

---


R1 est un routeur *externe* :

- il a aussi une IP dans le réseau local du client et réalise ainsi une *passerelle* ;
- c'est cette IP que le client utilise pour envoyer des informations à l'extérieur de son réseau local.

---

R3 est un routeur *interne* :

- il a 3 IP différentes sur les 3 réseaux auxquels il est connecté.

---

# Routage des paquets

---

Lorsqu'un paquet doit transiter du client au serveur

- il doit obligatoirement passer la passerelle R1 ;
- là encore il n'y a pas le choix, il passera par R3.

---

Mais ensuite ?

Comment la route à emprunter est-elle déterminée ?

Est-ce la même tout le temps ?

---

En fait, chaque routeur possède une *table de routage* qui associe les IP de destination à des routeurs particuliers.

---

Ces tables ne sont pas fixes.

*A priori* tous les routeurs ont le même statut (il n'y a pas de routeur privilégié).

---

Les méthodes qui permettent de gérer ces tables de routage sont appelés des *protocoles de routage*.

---

# Le protocole RIP

*(Routing Information Protocol)*

---

## Principe

À intervalles de temps réguliers, chaque routeur envoie à ses voisins

- les adresses de ses propres voisins ;
- les adresses qu'il a reçues par d'autres routeurs.

---

Pour chaque adresse, il indique également combien de sauts sont nécessaires pour l'atteindre, c'est-à-dire par combien
de routeurs (y compris lui-même) il faut passer.

---

Lorsqu'un routeur reçoit les informations d'un routeur voisin, 4 cas peuvent survenir :

---

1. Une route vers un nouveau sous-réseau lui est présentée : il l'ajoute à sa table de routage.
2. Une route vers un sous-réseau déjà connu lui est présentée, mais plus courte que la précédente. Dans ce cas
   l'ancienne est remplacée par celle-ci.
3. Une nouvelle route plus longue lui est transmise : il l'ignore.
4. Une route existante, passant par le même voisin, mais plus longue que celle de la table de routage lui est présentée.
   Cela veut dire qu'un problème est survenu sur l'ancienne route. Celle-ci est donc effacée et remplacée par la plus
   longue.

---

Pour éviter les boucles, les distances doivent être au maximum de 15 (sinon elles sont ignorées).

RIP fonctionne donc sur des réseaux de taille modeste.

---

## Exemple

---

Reprenons le réseau précédent et intéressons-nous uniquement aux routeurs R1 et R3.

### Étape 1 : initialisation

---

Au début de la mise en service du réseau voici la table de routage de R1 :

|   destination    |  passerelle  |  interface  |  distance   |
|:----------------:|:------------:|:-----------:|:-----------:|
|   10.0.1.0/30    |      	       |    eth0     |      1      |
|  192.168.1.0/24  |      	       |    wlan0    |      1      |

---

Elle indique que le sous-réseau local 192.168.1.0/24 est immédiatement accessible *via* l'interface *WiFi* wlan0 depuis
ce propre routeur R1. Elle est donc à distance 1 de R1.

De même l'autre sous-réseau est accessible *via* un port *Ethernet*
du routeur nommé eth0 et est également à distance 1 de R1.

---

Voici celle de R3 :

| destination | passerelle | interface | distance |
|:-----------:|:----------:|:---------:|:--------:|
| 10.1.1.0/30 |            |   eth1    |    1     |
| 10.1.2.0/30 |            |   eth2    |    1     |
| 10.1.3.0/30 |            |   eth3    |    1     |
| 10.1.4.0/30 |            |   eth0    |    1     |

---

C'est la même chose : R3 est initialisé avec ses voisins directs.

Les noms des interfaces sont relatifs à R3.

R1 et R3 sont reliés par *Ethernet* sur le port eth0 de R1 et eth1 de R3. Ces ports peuvent avoir le même nom ou pas,
peu importe, car ces noms n'existent que relativement au routeur concerné.

---

### Étape 2 : première itération de RIP

Chaque routeur envoie ses informations à ses voisins. La table de R1 change :

---

|  destination   | passerelle | interface | distance |
|:--------------:|:----------:|:---------:|:--------:|
|  10.0.1.0/30   |            |   eth0    |    1     |
| 192.168.1.0/24 |            |   wlan0   |    1     |
|  10.0.2.0/30   |  10.1.1.2  |   eth0    |    2     |
|  10.0.3.0/30   |  10.1.1.2  |   eth0    |    2     |
|  10.0.4.0/30   |  10.1.1.2  |   eth0    |    2     |

---

R1 sait maintenant qu'il peut atteindre les machines du sous-réseau 10.1.2.0/30 *via* la passerelle 10.1.1.2 (IP de R2)
sur le sous-réseau 10.1.1.0/30.

L'interface est eth0 et la distance est 2.

---

La table de R3 change aussi :

---

|  destination   | passerelle | interface | distance |
|:--------------:|:----------:|:---------:|:--------:|
|  10.1.1.0/30   |            |   eth1    |    1     |
| 192.168.1.0/24 |  10.1.1.1  |   eth1    |    2     |
|  10.1.2.0/30   |            |   eth2    |    1     |
|  10.1.3.0/30   |            |   eth3    |    1     |
|  10.1.4.0/30   |            |   eth0    |    1     |
|  10.1.7.0/30   |  10.1.4.2  |   eth0    |    2     |

---

### Étape 3 : convergence après quelques itérations

Dans notre cas, après 2 autres itérations, les informations se stabilisent.

On dit qu'il y a *convergence*.

Chaque routeur connaît le chemin à emprunter pour accéder à n'importe quel sous-réseau.

---

Table de R1 « stabilisée »

---

|  destination   | passerelle | interface | distance |
|:--------------:|:----------:|:---------:|:--------:|
|  10.0.1.0/30   |    	       |   eth0    |    1     |
| 192.168.1.0/24 |            |   wlan0   |    1     |
|  10.0.2.0/30   |  10.1.1.2  |   eth0    |    2     |
|  10.0.3.0/30   |  10.1.1.2  |   eth0    |    2     |
|  10.0.4.0/30   |  10.1.1.2  |   eth0    |    2     |
|  10.0.5.0/30   |  10.1.1.2  |   eth0    |    3     |
|  10.0.6.0/30   |  10.1.1.2  |   eth0    |    3     |
|  10.0.7.0/30   |  10.1.1.2  |   eth0    |    3     |
| 192.162.6.0/30 |  10.1.1.2  |   eth0    |    4     |

---

Le protocole RIP fait suivre des routes minimisant le nombre de sauts.

Cela peut être une très mauvaise idée !

---

![Problème avec RIP](img/rip_nase.png){width=70%}

---

Il faut prendre en compte le débit des interconnexions.

C'est ce que fait le protocole OSPF.

---

# Protocole OSPF

*Open Shortest Path First*

---


