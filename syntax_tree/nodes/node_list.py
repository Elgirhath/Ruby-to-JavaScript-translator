class NodeList:
    def __init__(self, children):
        self.children = children

    def __str__(self):
        out = "NodeList(["

        for child in self.children:
            if self.children.index(child) != 0:
                out += ", "
            out += str(child)
        out += "])"
        return out

    def toJavaScript(self, separator = "\n"):
        out = ""
        for i, child in enumerate(self.children):
            if i != 0:
                out += separator

            out += child.toJavaScript()
        
        return out