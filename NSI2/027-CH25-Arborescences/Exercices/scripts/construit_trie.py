from time import process_time_ns
from trie import *



def contenu(t: Trie, mot=None, liste=None) -> list:
    mot = mot or ""
    liste = liste or []
    print(len(liste))
    if t.valeur:
        mot += t.valeur
    if t.fin:
        liste.append(mot)
    for u in t.fils.values():
        liste2 = contenu(u, mot, liste)
        for m in liste2:
            if m not in liste:
                liste.append(m)
    return liste


liste_mots = Trie()

nb_mots = 0
with open('dico.txt', 'rt', encoding='utf8') as fichier:  # on ouvre le fichier
    ligne = fichier.readline()  # on lit une ligne
    while ligne:
        liste_mots.ajoute_mot(ligne[:-1])  # On enlève le dernier caractere, c'est un \n
        nb_mots += 1
        ligne = fichier.readline()

print(liste_mots.commence("ASTE"))
