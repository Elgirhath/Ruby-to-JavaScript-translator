class Not:
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return "Not(" + str(self.expression) + ")"

    def toJavaScript(self):
        return "!" + self.expression.toJavaScript()