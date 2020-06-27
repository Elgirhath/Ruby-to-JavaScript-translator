class GenericOperator:
    def __init__(self, symbol, left, right):
        self.symbol = symbol
        self.left = left
        self.right = right
        
    def __str__(self):
        return self.symbol + "(" + str(self.left) + ", " + str(self.right) + ")"

    def toJavaScript(self):
        return self.left.toJavaScript() + " " + self.symbol + " " + self.right.toJavaScript()
        