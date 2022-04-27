from random import randint


def construis_liste(n: int) -> list:
    resultat = [1, 1]
    valeur = resultat[-1] + resultat[-2]
    while valeur < n:
        resultat.append(valeur)
        valeur = resultat[-1] + resultat[-2]
    return resultat


n = randint(20, 30)
perdants = construis_liste(n)
val_max = n - 1
gagnant = "humain"
while n > 0:
    trouve = False
    while trouve is False:
        choix_ordi = randint(1, val_max//2)
        if n - choix_ordi not in perdants:
            trouve = True
    print(f"Il y a {n} jetons et l'ordi en prend {choix_ordi}")
    n-= choix_ordi
    if n == 0:
        gagnant = "ordi"
    else:
        val_max = 2 * choix_ordi
        choix_humain = 0
        while not 1 <= choix_humain <= val_max:
            choix_humain = int(input(f"Il reste {n} jetons, combien de jetons prenez-vous (min 1, max {val_max}) :"))
        n -= choix_humain
        val_max = 2 * choix_humain
print(f"Le gagnant est l'{gagnant}.")
