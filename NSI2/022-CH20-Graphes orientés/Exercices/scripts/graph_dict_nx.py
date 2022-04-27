import networkx as nx
import matplotlib.pyplot as plt


class GraphDict:
    def __init__(self, vertices):
        self.succ = dict()
        for v in vertices:
            self.succ[v] = []

    def add_arrow(self, v1, v2):
        self.succ[v1].append(v2)

    def add_vertex(self, v):
        self.succ[v] = []

    def is_predecessor(self, v1, v2):
        return v2 in self.succ[v1]

    def is_successor(self, v2, v1):
        return self.is_predecessor(v1, v2)

    def successors(self, v):
        return self.succ[v]

    def predecessors(self, v):
        return [x for x in self.succ if v in self.succ[x]]

    def vertices(self):
        return list(self.succ)

    def arrows(self) -> list:
        result = []
        for v1 in self.succ:
            for v2 in self.succ[v1]:
                result.append((v1, v2))
        return result

    def draw(self, layout='circular'):
        draw_graph = nx.DiGraph()
        draw_graph.add_edges_from(self.arrows())
        if layout == 'circular':
            positions = nx.circular_layout(draw_graph)
        elif layout == 'fr':
            positions = nx.fruchterman_reingold_layout(draw_graph)
        else:
            positions = nx.random_layout(draw_graph)
        nx.draw(draw_graph, positions, with_labels=True)
        plt.show()
