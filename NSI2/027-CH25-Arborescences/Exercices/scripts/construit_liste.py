from time import process_time_ns

liste_mots = []  # on part d'une liste vide
nb_lettres_liste = 0
with open('dico.txt', 'rt', encoding='utf8') as fichier:  # on ouvre le fichier
    ligne = fichier.readline()  # on lit une ligne
    while ligne:
        liste_mots.append(ligne[:-1])  # On enlève le dernier caractere, c'est un \n
        nb_lettres_liste += len(ligne[:-1])
        ligne = fichier.readline()


