---
title: Sécurisation des communications
subtitle: principes
date : 25 avril 2022
theme: white
transition: fade
---

# Vocabulaire

---

- **chiffrer** : utiliser un algorithme pour transformer un message en un autre, incompréhensible sans clé/algorithme ;
- **déchiffrer** : utiliser un algorithme et/ou un clé pour transformer un message incompréhensible en un autre,
  compréhensible ;
- **cryptographie** : science du chiffrement/déchiffrement ;
- **décryptage** : retrouver un message original *sans clé ni algorithme* ;

---

# Chiffrement symétrique

---

![Alice et Bob disposent de la clé](img/sym00.svg)

---

![Alice veut envoyer un message à Bob](img/sym01.svg)

---

![elle le chiffre avec la clé](img/sym02.svg)

---

![elle transmet ](img/sym03.svg)

---

![Bob récupère et déchiffre avec la clé](img/sym04.svg)

---

- Problème : comment faire pour transmettre la clé publique en toute sécurité ?

- Avantage : algorithmes rapides en général.

---

# Chiffrement asymétrique

---

![Alice veut envoyer un message à Bob, qui dispose de ses clés publiques et privées](img/asym00.svg)

---

![Bob donne sa clé publique à Alice (à tout le monde, en fait)](img/asym01.svg)

---

![Alice s'en sert pour chiffrer son message](img/asym02.svg)

---

![Elle transmet](img/asym03.svg)

---

![Bob utilise sa clé privée pour déchiffrer](img/asym04.svg)


---

- Avantage : Pas de problème de transmission de clé comme avec le chiffrement symétrique ;
- Inconvénient : Algorithmes souvent plus lents (environ 1000 fois) que pour le chiffrement symétrique.

---

# Fonctions de hachage

---

L'ensemble des fichiers est gigantesque mais « creux » :

- 1 ko = 8000 bits : il y a $2^{8000}$ fichiers de taille 1ko ;
- cela fait de l'ordre de $10^{2408}$ fichiers ;
- parmi tout ceux-là, seuls un nombre restreint sont de « vrais » fichiers.

---

Une fonction de hachage transforme un fichier (de volume arbitraire) en signature de taille fixe, beaucoup plus petite
avec les caractéristiques suivantes :

- il est impossible de reconstituer le fichier à partir de l'empreinte ;
- en pratique, des fichiers différents ont des empreintes distinctes ;
- si on change un bit du fichier de départ, l'empreinte change du tout au tout.

---

# Signature numérique

---

![Alice dispose de ses clé privées et publiques et veut signer un fichier](img/sign00.svg)

---

![elle fabrique une empreinte du fichier avec une fonction de hachage connue et chiffre l'empreinte (signature)](img/sign01.svg)

---

![elle transmet fichier,empreinte,signature et clé publique](img/sign02.svg)

---

![Bob crée aussi l'empreinte du fichier reçu et vérifie que c'est la même : le fichier n'a pas été modifié entre temps](img/sign03.svg)

---

![Il déchiffre la signature et vérifie qu'il obtient l'empreinte : c'est bien Alice, seule détentrice de la clé privée, qui lui a envoyé le fichier](img/sign04.svg)

---

# HTTPS

---

![le serveur dispose d’un certificat X509 signé par une autorité de
certification et une paire de clefs privée et publique](img/https00.svg)

---

![le navigateur demande et récupère le certificat du serveur avec sa
clef publique.](img/https01.svg)

---

![Le navigateur vérifie la signature du certificat attestant de sa validité. Ceci
peut se faire *via* une autorité de certification en ligne ou
localement avec des certificats préchargés dans le navigateur.](img/https02.svg)

---

![Le navigateur crée une clé de chiffrement symétrique et la chiffre avec la clé publique du serveur](img/https03.svg)

---

![le serveur récupère et déchiffre](img/https04.svg)

---

![la session HTTP chiffrée symétriquement peut commencer](img/https05.svg)