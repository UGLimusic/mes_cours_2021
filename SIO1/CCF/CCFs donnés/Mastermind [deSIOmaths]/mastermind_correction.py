from random import randint


def indic(combi: list[int], propos: list[int]) -> [int, int]:
    b_place, m_place = 0, 0
    for i in range(4):
        for j in range(4):
            if propos[i] == combi[j]:
                if i == j:
                    b_place += 1
                else:
                    m_place += 1
    return [b_place, m_place]


def tirage() -> list[int]:
    resultat = list()
    for i in range(4):
        h = randint(0, 7)
        while h in resultat:
            h = randint(0, 7)
        resultat.append(h)
    return resultat


def transform(propos: str) -> list[int]:
    resultat = list()
    for i in range(4):
        resultat.append(int(propos[i]))
    return resultat


combi = tirage()
nb_coups = 0
bp, mp = 0, 0
print(combi)
while not (bp == 4 or nb_coups == 8):
    nb_coups += 1
    propos_joueur = transform(input("Entrer la proposition"))
    bp, mp = indic(combi, propos_joueur)
    print(f"{bp} nombres bien placés, {mp} nombres mal placés.")

if bp == 4:
    print(f"Gagné en {nb_coups} coups.")
else:
    print(f"perdu, la combi était {combi}")
