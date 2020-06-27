from syntax_tree.nodes.parenthesis import Parenthesis

class MethodCall:
    def __init__(self, method_name, argument_list):
        self.method_name = method_name
        self.argument_list = argument_list

    def __str__(self):
        out = "MethodCall("
        out += "Method: " + str(self.method_name)
        out += ", Arguments: " + str(self.argument_list)
        out += ")"
        return out

    def toJavaScript(self):
        return self.method_name + "(" + self.argument_list.toJavaScript(", ") + ")"