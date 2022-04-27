class GraphNO:
    def __init__(self, vertices):
        self.neighb = dict()  # dict vide des successeurs.
        for v in vertices:  # pour chaque sommet
            self.neighb[v] = []  # ses successeurs c'est la liste vide

    def add_edge(self, v1, v2):
        self.neighb[v1].append(v2)  # ajoute v2 à la liste des succ de v1
        self.neighb[v2].append(v1)

    def add_vertex(self, v):
        self.neighb[v] = []  # trop facile.

    def is_neighbor(self, v2, v1):
        return v2 in self.neighb[v1]  # ou v1 in self.succ[v2]

    def neighbors(self, v):
        return self.neighb[v]



    def vertices(self):
        return list(self.neighb)
