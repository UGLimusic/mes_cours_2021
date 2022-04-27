import networkx as nx
import matplotlib.pyplot as plt
from random import randint, choice


class GraphDict:
    def __init__(self, vertices):
        self.neighb = dict()
        for v in vertices:
            self.neighb[v] = []
        self.colors = dict()

    def add_edge(self, v1, v2):
        self.neighb[v1].append(v2)
        self.neighb[v2].append(v1)

    def add_vertex(self, v):
        self.neighb[v] = []

    def neighbors(self, v):
        return self.neighb[v]

    def vertices(self):
        return list(self.neighb)

    def set_color(self, v, col):
        self.colors[v] = col

    def get_color(self, v):
        if v in self.colors:
            return self.colors[v]
        return None

    def edges(self):
        result = []
        for v1 in self.neighb:
            for v2 in self.neighb[v1]:
                if (v2, v1) not in result:
                    result.append((v1, v2))
        return result

    def draw(self, layout='circular'):
        draw_graph = nx.Graph()
        draw_graph.add_edges_from(self.edges())
        if layout == 'circular':
            positions = nx.circular_layout(draw_graph)
        elif layout == 'fr':
            positions = nx.fruchterman_reingold_layout(draw_graph)
        else:
            positions = nx.random_layout(draw_graph)
        color_map = []
        for node in draw_graph:
            if node in self.colors:
                color_map.append(self.colors[node])
            else:
                color_map.append('blue')

        nx.draw(draw_graph, positions, node_color=color_map, with_labels=True)

        plt.show()


n = 10
color_list = ['gray', 'blue', 'red', 'green', 'yellow', 'pink']




G = GraphDict([i for i in range(n)])
for i in range(n):
    for j in range(n):
        if i != j and randint(0, n // 2) == 0:
            G.add_edge(i, j)

G.draw()
print(G.vertices())
print(G.edges())
G.set_color(1, 'yellow')
G.draw()

