from random import randint


def A_joue(n: int) -> int:
    """
    permet à l'ordi de gagner dans 75% des cas
    n est le nomb re de jetons resstants
    en sortie : le nombre qu'il reste après que l'ordi a joué
    """

    if n % 4 == 0:
        return n - 3
    elif n % 4 == 3:
        return n - 2
    else:
        return n - 1


def B_joue(n: int) -> int:
    """ fait jouer l'humain :
    en entrée prend le nombre de jetons restants
    en sortie renvoie le nombre qu'il reste après que l'humain a joué
    """
    enleve = 0
    while not (1 <= enleve <= 3 and enleve <= n):
        enleve = int(input("Combien de jetons prends-tu ? "))
    return n - enleve


n = randint(15, 25)

gagnant = None
while n > 0:
    print("Il y a", n, "jetons, c'est au tour de A.")
    n = A_joue(n)
    print("A a joué, il reste", n, "jetons.")
    if n == 0:
        gagnant = "B"
    if not gagnant:
        n = B_joue(n)
        print("Tu as joué, il reste", n, "jetons.")
        if n == 0:
            gagnant = "A"
print("Le gagnant est", gagnant)
