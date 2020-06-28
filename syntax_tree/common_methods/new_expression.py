from syntax_tree.nodes.method_call import MethodCall

class New(MethodCall):
    def __str__(self):
        return "New(Class name: " + self.method_name + ", Arguments: " + str(self.argument_list) + ")"

    def toJavaScript(self):
        return "new " + self.method_name + "(" + self.argument_list.toJavaScript(", ") + ")"