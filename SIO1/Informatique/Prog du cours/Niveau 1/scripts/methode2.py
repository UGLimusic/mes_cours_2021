entier = int(input("Entre un entier :"))
print('Je commence par trouver la plus grande puissance de 2 inférieure à', entier)
i = 0
while 2 ** i <= entier:
    print(entier, "<", 2 ** i)
    i += 1
i -= 1

print("J'ai trouvé",2** i)
reponse = ""
while entier > 0:
    print("Je compare ", entier, "avec", 2 ** i)
    if entier >= 2 ** i:
        print("C'est plus grand ou égal")
        reponse += "1"
        entier -= 2 ** i
    else:
        print("C'est plus petit")
        reponse += "0"
    i -= 1
    print("J'ai construit", reponse, "il me reste", entier)
print("En définitive j'ai trouvé", reponse)
