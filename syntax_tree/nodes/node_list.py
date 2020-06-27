class NodeList:
    def __init__(self, children):
        self.children = children

    def __str__(self):
        out = "["

        for child in self.children:
            if self.children.index(child) != 0:
                out += ", "
            out += str(child)
        out += "]"
        return out