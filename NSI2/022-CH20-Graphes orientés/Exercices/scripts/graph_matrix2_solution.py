class GraphMatrix2:

    def __init__(self, vertices: list):
        self.size = len(vertices)
        self.vertices = vertices  # ['A','B','C] A est 0, B est 1...
        self.matrix = [[0 for j in range(self.size)] for i in range(self.size)]

    def add_arrow(self, v1: str, v2: str):
        self.matrix[self.vertices.index(v1)][self.vertices.index(v2)] = 1

    def is_predecessor(self, v1: str, v2: str) -> bool:
        return self.matrix[self.vertices.index(v1)][self.vertices.index(v2)] == 1

    def is_successor(self, v2: str, v1: str) -> bool:
        return self.is_predecessor(v1, v2)

    def predecessors(self, v: str) -> list:
        j = self.vertices.index(v)
        return [self.vertices[i] for i in range(self.size) if self.matrix[i][j] == 1]

    def successors(self, v: str) -> list:
        i = self.vertices.index(v)
        return [self.vertices[j] for j in range(self.size) if self.matrix[i][j] == 1]
