from syntax_tree.nodes.method import Method

class Class:
    def __init__(self, name, statement_list):
        self.name = name
        self.statement_list = statement_list
        self.propagate_method_context()

    def __str__(self):
        out = "Class("
        out += "Name: " + str(self.name)
        out += ", StatementList " + str(self.statement_list)
        out += ")"
        return out

    def toJavaScript(self):
        out = "class " + self.name.toJavaScript() + "{\n"
        out += self.statement_list.toJavaScript()
        out += "}\n"
        return out

    def propagate_method_context(self):
        for statement in self.statement_list.children:
            if isinstance(statement, Method):
                statement.context = "class"