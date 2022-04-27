class NoeudArborescence:
    def __init__(self, valeur):
        self.valeur = valeur
        self.fils = []

    def ajoute_fils(self, fils):
        self.fils.append(fils)

    def prefix(self):
        pass

    def postfix(self):
        pass


# Création de l'arbre
noeud = []
for i in range(12):
    noeud.append(NoeudArborescence(i))
noeud[0].ajoute_fils(noeud[1])
noeud[0].ajoute_fils(noeud[2])
noeud[0].ajoute_fils(noeud[3])
noeud[1].ajoute_fils(noeud[4])
noeud[1].ajoute_fils(noeud[5])
noeud[2].ajoute_fils(noeud[6])
noeud[3].ajoute_fils(noeud[7])
noeud[7].ajoute_fils(noeud[8])
noeud[8].ajoute_fils(noeud[9])
noeud[8].ajoute_fils(noeud[10])
noeud[8].ajoute_fils(noeud[11])
racine = noeud[0]

# Tests
racine.postfix()
racine.prefix()
