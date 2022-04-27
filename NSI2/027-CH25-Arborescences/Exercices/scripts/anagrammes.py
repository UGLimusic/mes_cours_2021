def anagramme(chaine: str) -> set:
    if len(chaine) == 1:
        return {chaine}
    else:
        resultat = set()
        sous_chaines = f(chaine)
        for element in sous_chaines:
            plus = {element[1] + x for x in anagramme(element[0])}
            resultat = resultat.union(plus)

        return resultat


def scrabble(chaine: str) -> set:
    resultat = set()
    for i in range(len(chaine)):
        resultat = resultat.union(anagramme(chaine[:i]))
    return resultat


def f(s):
    r = []
    for i in range(len(s)):
        ss = ''
        for j in range(len(s)):
            if j != i:
                ss += s[j]
        r.append((ss, s[i]))
    return r
