chaine = input("Entrez un entier positif :")
longueur = len(chaine)
somme = 0
for i in range(longueur):
    chiffre = int(chaine[i])
    somme = somme + chiffre
print(somme)
