from syntax_tree.nodes.method import Method

class Constructor(Method):
    def toJavaScript(self):
        out = "constructor("

        for i, argument in enumerate(self.argument_list.children):
            if i != 0:
                out += ", "
            out += argument.toJavaScript()

        out += ") {\n"
        out += self.statement_list.toJavaScript()
        out += "\n}\n"

        return out