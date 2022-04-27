class NodeTS:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, other):
        self.children.append(other)


