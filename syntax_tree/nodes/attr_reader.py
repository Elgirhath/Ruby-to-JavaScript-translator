class AttrReader:
    def __init__(self, identifier):
        self.identifier = identifier

    def __str__(self):
        return "Public(" + str(self.identifier) + ")"
        
    def toJavaScript(self):
        return ""