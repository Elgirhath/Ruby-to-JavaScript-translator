class BuiltIn:
    def __init__(self, object):
        self.object = object

    def __str__(self):
        return str(self.object)
        
    def toJavaScript(self):
        if isinstance(self.object, str):
            return "\"" + str(self.object) + "\""
        elif isinstance(self.object, bool):
            return "true" if str(self.object) else "false"
            
        return str(self.object)