entier = int(input("Entrez un nombre :"))

resultat = ""
while entier != 0:
    resultat = str(entier % 2) + resultat
    entier //= 2
print(resultat)
