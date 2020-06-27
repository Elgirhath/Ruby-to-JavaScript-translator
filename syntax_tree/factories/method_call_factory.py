from syntax_tree.common_methods.puts import PutsMethodCall
from syntax_tree.nodes.method_call import MethodCall

class MethodCallFactory:
    @staticmethod
    def get(method_name, argument_list):
        if method_name == "puts":
            return PutsMethodCall(method_name, argument_list)
        else:
            return MethodCall(method_name, argument_list)