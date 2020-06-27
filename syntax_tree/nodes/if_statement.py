class If:
    def __init__(self, condition, statement_list, elseif_list, else_statement_list):
        self.condition = condition
        self.statement_list = statement_list
        self.elseif_list = elseif_list
        self.else_statement_list = else_statement_list

    def __str__(self):
        out = "If("
        out += "Condition: " + str(self.condition)
        out += ", StatementList " + str(self.statement_list)
        out += ", ElseIfList: " + str(self.elseif_list)
        out += ", ElseStatementList: " + str(self.else_statement_list)
        out += ")"
        return out