from syntax_tree.nodes.generic_operator import GenericOperator

class OperatorFactory:
    '''
    Returns Operator object based on Ruby's symbol
    '''

    @staticmethod
    def get(operator, left, right):
        return GenericOperator(operator, left, right)