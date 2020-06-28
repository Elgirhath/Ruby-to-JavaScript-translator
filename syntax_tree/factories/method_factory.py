from syntax_tree.nodes.constructor import Constructor
from syntax_tree.nodes.method import Method

class MethodFactory:
    @staticmethod
    def get(method_name, argument_list, statement_list):
        if method_name == "initialize":
            return Constructor(method_name, argument_list, statement_list)
        else:
            return Method(method_name, argument_list, statement_list)