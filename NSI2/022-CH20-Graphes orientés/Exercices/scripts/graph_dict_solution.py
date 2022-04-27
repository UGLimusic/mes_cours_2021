class GraphDict:
    def __init__(self, vertices):
        self.succ = dict()  # dict vide des successeurs.
        for v in vertices:  # pour chaque sommet
            self.succ[v] = []  # ses successeurs c'est la liste vide

    def add_arrow(self, v1, v2):
        self.succ[v1].append(v2) # ajoute v2 à la liste des succ de v1

    def add_vertex(self, v):
        self.succ[v] = [] # trop facile.

    def is_predecessor(self, v1, v2):
        return v2 in self.succ[v1]

    def is_successor(self, v2, v1):
        return self.is_predecessor(v1, v2)

    def successors(self, v):
        return self.succ[v]

    def predecessors(self, v):
        # self.succ est un dict : sommet : [liste sommets successeurs]
        # for x in self.succ : [sommet]
        # for x in self.values : [[liste sommets successeurs] ]
        return [x for x in self.succ if v in self.succ[x]]

    def vertices(self):
        return list(self.succ)
