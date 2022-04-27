class GraphMatrix:

    def __init__(self, size: int):
        self.matrix = [[0 for j in range(size)] for i in range(size)]
        self.size = size

    def add_arrow(self, i: int, j: int):
        self.matrix[i][j] = 1

    def is_prececessor(self, i: int, j: int) -> bool:
        return self.matrix[i][j] == 1

    def is_successor(self, j: int, i: int) -> bool:
        return self.is_prececessor(i, j)

    def predecessors(self, j: int) -> list:
        return [i for i in range(self.size) if self.matrix[i][j] == 1]

    def successors(self, i: int) -> list:
        return [j for j in range(self.size) if self.matrix[i][j] == 1]
