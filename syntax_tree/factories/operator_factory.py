from syntax_tree.nodes.generic_operator import GenericOperator

class OperatorFactory:
    '''
    Returns Operator object based on Ruby's symbol
    '''

    @staticmethod
    def get(operator, left, right):
        if operator == "&&" or operator == "and":
            return GenericOperator("&&", left, right)
        if operator == "||" or operator == "or":
            return GenericOperator("||", left, right)
        return GenericOperator(operator, left, right)