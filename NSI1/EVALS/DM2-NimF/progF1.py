from random import randint

n = randint(20, 30)
val_max = n - 1
gagnant = "humain"
while n > 0:
    choix_ordi = randint(1, val_max)
    print(f"Il y a {n} jetons et l'ordi en prend {choix_ordi}")
    n -= choix_ordi
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
