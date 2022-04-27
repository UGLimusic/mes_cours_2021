from random import randint  # Pour disposer de la fonction randint

n = randint(15, 25)  # pour choisir un nombre de jetons au hasard
while n > 0:  # tant qu'il reste des jetons
    choix_ordi = randint(1, min(3, n))  # l'ordi choisit au hasard au moins un jeton
    # et au plus le plus petit nombre entre 3 et n
    print(f"Il reste {n} jetons, l'ordi en prend {choix_ordi}.")  # on affiche
    n -= choix_ordi  # on retire
    if n == 0:  # s'il n'y a plus de jetons
        gagnant = "vous"  # l'humain gagne
    else:  # sinon
        choix_joueur = 0  # on met cette variable à zéro pour entrer dans la boucle
        while not (1 <= choix_joueur <= min(3, n)):  # et tant la variable n'a pas une valeur convenable
            # on demande une valeur à l'humain
            choix_joueur = int(input(f"Il reste {n} jetons, combien voulez-vous en prendre ?"))

        n -= choix_joueur  # on l'enleve
        if n == 0:  # s'il n'y a plus de jetons
            gagnant = "l'ordi"  # l'ordi a gagné
print(f"Le gagnant est : {gagnant}.")  # Il n'y a plus de jetons, on affiche le gagnant
