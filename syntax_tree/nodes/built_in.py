class BuiltIn:
    def __init__(self, object):
        self.object = object

    def __str__(self):
        return str(self.object)
        
    def toJavaScript(self):
        if isinstance(self.object, str):
            return "\"" + str(self.object) + "\""
            
        return str(self.object)