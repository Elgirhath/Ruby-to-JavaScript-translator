class List:
    def __init__(self, expression_list):
        self.expression_list = expression_list

    def __str__(self):
        out = "List("
        out += "ExpressionList " + str(self.expression_list)
        out += ")"
        return out

    def toJavaScript(self):
        out = "["
        out += self.expression_list.toJavaScript(", ")
        out += "]"
        return out