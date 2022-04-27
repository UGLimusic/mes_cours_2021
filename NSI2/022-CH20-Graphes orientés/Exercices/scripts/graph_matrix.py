class GraphMatrix:

    def __init__(self, size: int):
        self.size = None  # TODO
        self.matrix = None  # TODO
        pass

    def add_arrow(self, i: int, j: int):
        """Adds an arrow from i to j"""
        pass  # TODO

    def is_predecessor(self, i: int, j: int) -> bool:
        """returns True if i is predecessor of j"""
        pass  # TODO

    def is_successor(self, j: int, i: int) -> bool:
        """returns True if j is a successor on i"""
        pass  # TODO

    def predecessors(self, j: int) -> list:
        """returns the list of all predecessors of j"""
        pass  # TODO

    def successors(self, i: int) -> list:
        """returns the list of all successors of i"""
        pass  # TODO
