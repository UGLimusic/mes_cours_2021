nombre_binaire = input("Entrez un nombre en binaire :")
valeur = 0
n = len(nombre_binaire)
for i in range(n):
    if nombre_binaire[i] == '1':
        valeur += 2**(n-1-i)
print("Cela vaut",valeur)
