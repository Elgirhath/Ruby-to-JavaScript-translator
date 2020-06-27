class Identifier:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        out = "Identifier("
        out += "Name: " + str(self.name)
        out += ")"
        return out

    def toJavaScript(self):
        return self.name