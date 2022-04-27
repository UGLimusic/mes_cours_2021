class Trie:
    nb_nodes = 0

    @classmethod
    def construit_arbre_anagrammes(cls, chaine):
        root = Trie()

    def __init__(self, valeur=None, fin=False):
        self.valeur = valeur
        self.fin = fin
        self.fils = dict()
        Trie.nb_nodes += 1

    def ajoute_mot(self, mot: str) -> None:
        if len(mot) == 1:
            if mot not in self.fils:
                self.fils[mot] = Trie(mot, True)
            else:
                self.fils[mot].fin = True
        else:
            lettre = mot[0]
            if lettre not in self.fils:
                self.fils[lettre] = Trie(lettre)
            self.fils[lettre].ajoute_mot(mot[1:])

    def contient(self, mot: str) -> bool:
        if len(mot) == 1:
            return mot in self.fils and self.fils[mot].fin
        else:
            lettre = mot[0]
            if lettre not in self.fils:
                return False
            else:
                return self.fils[lettre].contient(mot[1:])

    def __contains__(self, item):
        return self.contient(item)

    def contenu(self, mot=None, liste=None) -> list:
        mot = mot or ""
        liste = liste or []
        if self.valeur:
            mot += self.valeur
        if self.fin:
            liste.append(mot)
        for u in self.fils.values():
            liste2 = u.contenu(mot, liste)
            for m in liste2:
                if m not in liste:
                    liste.append(m)
        return liste

    def commence(self, debut):
        debut2 = debut
        courant = self
        while debut:
            if debut[0] not in courant.fils:
                return []
            courant = courant.fils[debut[0]]
            debut = debut[1:]
        return courant.contenu(debut2[:-1])
