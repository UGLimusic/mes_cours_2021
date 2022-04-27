from random import randint

n = int(input("Entrez le nombre de lignes : "))
p = int(input("Entrez le nombre de colonnes : "))

matrice = []  # une matrice est une liste de lignes

for i in range(n):  # il y a n lignes
    ligne = []  # on construit une ligne vide
    for j in range(p):  # il y a p colonnes
        ligne.append(randint(-100, 100))  # on remplit la ligne aléatoirement
    matrice.append(ligne)  # on ajoute la ligne à la liste de lignes