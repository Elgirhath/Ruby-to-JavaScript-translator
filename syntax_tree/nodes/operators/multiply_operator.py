from syntax_tree.nodes.operators.operator import Operator

class MultiplyOperator(Operator):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    def toJavaScript(self):
        return self.left.toJavaScript() + " * " + self.right.toJavaScript()