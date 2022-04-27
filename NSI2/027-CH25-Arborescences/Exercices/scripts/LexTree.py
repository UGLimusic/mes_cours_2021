class LexTree:

    def __init__(self, value=None, is_end=False):
        self.value = value
        self.is_end = is_end
        self.children = set()


