class ListAccessOperator:
    def __init__(self, identifier, index_expression):
        self.identifier = identifier
        self.index_expression = index_expression
        
    def __str__(self):
        return str(self.identifier) + "[" + str(self.index_expression) + "]"

    def toJavaScript(self):
        return self.identifier.toJavaScript() + "[" + self.index_expression.toJavaScript() + "]"