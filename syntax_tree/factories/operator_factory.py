from syntax_tree.nodes.operators.add_operator import AddOperator
from syntax_tree.nodes.operators.subtract_operator import SubtractOperator
from syntax_tree.nodes.operators.multiply_operator import MultiplyOperator
from syntax_tree.nodes.operators.divide_operator import DivideOperator
from syntax_tree.nodes.operators.assign_operator import AssignOperator
from syntax_tree.nodes.operators.equals_operator import EqualsOperator
from syntax_tree.nodes.operators.less_than_operator import LessThanOperator
from syntax_tree.nodes.operators.greater_than_operator import GreaterThanOperator
from syntax_tree.nodes.operators.less_or_equal_operator import LessOrEqualOperator
from syntax_tree.nodes.operators.greater_or_equal_operator import GreaterOrEqualOperator

class OperatorFactory:
    '''
    Returns Operator object based on Ruby's symbol
    '''

    @staticmethod
    def get(operator, left, right):
        if operator == '+':
            return AddOperator(left, right)
        if operator == '-':
            return SubtractOperator(left, right)
        if operator == '*':
            return MultiplyOperator(left, right)
        if operator == '/':
            return DivideOperator(left, right)
        if operator == '=':
            return AssignOperator(left, right)
        if operator == '==':
            return EqualsOperator(left, right)
        if operator == '<':
            return LessThanOperator(left, right)
        if operator == '>':
            return GreaterThanOperator(left, right)
        if operator == '<=':
            return LessOrEqualOperator(left, right)
        if operator == '>=':
            return GreaterOrEqualOperator(left, right)