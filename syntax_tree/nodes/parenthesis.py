class Parenthesis:
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return "(" + self.expression.toJavaScript() + ")"

    def toJavaScript(self):
        return str(self)