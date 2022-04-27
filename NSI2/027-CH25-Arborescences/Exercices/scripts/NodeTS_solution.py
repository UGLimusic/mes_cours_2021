import networkx as nx

class NoeudArborescence:
    def __init__(self, valeur):
        self.valeur = valeur
        self.fils = []

    def ajoute_fils(self, fils):
        self.fils.append(fils)

    def prefix(self, liste=None):
        if not liste:
            liste = []
        liste.append(self.valeur)
        for fils in self.fils:
            fils.prefix(liste)
        return liste

    def postfix(self):
        for fils in self.fils:
            fils.postfix()
        print(self.valeur)

    def liste_aretes(self):
        resultat = []
        for noeud in self.fils:
            resultat.append((self.valeur,noeud.valeur))
            resultat.extend(noeud.liste_aretes())
        return resultat


    def dessine(self):
        g = nx.DiGraph()
        g.add_edges_from(self.liste_aretes())
        p = nx.drawing.nx_pydot.to_pydot(g)
        p.write_png('resultat.png')
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

print(racine.prefix())
racine.dessine()
