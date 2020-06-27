class Return:
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return "Return(" + str(self.expression) + ")"