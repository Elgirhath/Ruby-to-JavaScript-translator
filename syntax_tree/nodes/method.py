class Method:
    def __init__(self, name, argument_list, statement_list):
        self.name = name
        self.argument_list = argument_list
        self.statement_list = statement_list

    def __str__(self):
        out = "Method("
        out += "Name: " + str(self.name)
        out += ", ArgumentList: " + str(self.argument_list)
        out += ", StatementList: " + str(self.statement_list)
        out += ")"
        return out

    def toJavaScript(self):
        out = "function " + self.name + "("
        for i, argument in enumerate(self.argument_list.children):
            if i != 0:
                out += ", "
            out += argument.toJavaScript()

        out += ") {\n"
        out += self.statement_list.toJavaScript()
        out += "\n}\n"

        return out