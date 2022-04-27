__author__ = 'UGLi'

import os  # os.path.getsize()
import gzip


def taille_compressee(*args):
    """
    Retourne la taille du (des) fichier(s) lorsqu'il(s) est (sont) compressé(s) avec gzip
    :param args:    Un ou plusieurs fichiers :
                    taille_compresse(fichier) ou bien
                    taille_compresse(fichier1,fichier2)
    :return: int
    """
    archive = gzip.open('archive.gz', mode='wb')
    contenu = bytes()
    for nomFichier in args:
        fichier = open(nomFichier, mode='rb')
        contenu += fichier.read()
        fichier.close()
    archive.write(contenu)
    archive.close()
    taille = os.path.getsize('archive.gz')
    os.remove('archive.gz')
    return taille


def distance(langue1, langue2):
    """
    Renvoie la distance de similarité entre 2 fichiers
    :param langue1: un fichier
    :param langue2: un autre
    :return: un float de [0;1]
    """
    a = taille_compressee(langue1)
    b = taille_compressee(langue2)
    ab = taille_compressee(langue1, langue2)
    ba = taille_compressee(langue2, langue1)
    return min(1 - (a + b - ab) / max(a, b), 1 - (a + b - ba) / max(a, b))
    return 1 - (a + b - ab) / max(a, b)


def calcule_distances(liste):
    """
    Calcule les distances entre les éléments de la liste :
    calcule d(A,B) mais pas d(B,A)
    ne calcule pas d(A,A)
    :param liste:
    :return:
    """
    resultat = list()
    for i in range(len(liste) - 1):
        for j in range(i + 1, len(liste)):
            resultat.append((liste[i], liste[j], distance(liste[i], liste[j])))
    return resultat


print(distance('francais','anglais'))
print(distance('anglais','francais'))
