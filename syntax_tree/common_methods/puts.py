from syntax_tree.nodes.method_call import MethodCall

class PutsMethodCall(MethodCall):
    def toJavaScript(self):
        return "console.log(" + self.argument_list.toJavaScript(", ") + ")"