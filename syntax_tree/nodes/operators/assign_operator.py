from syntax_tree.nodes.operators.operator import Operator

class AssignOperator(Operator):
    def __init__(self, left, right):
        self.left = left
        self.right = right