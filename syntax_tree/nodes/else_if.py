class ElseIf:
    def __init__(self, condition, statement_list):
        self.condition = condition
        self.statement_list = statement_list

    def __str__(self):
        out = "ElseIf("
        out += "Condition: " + str(self.condition)
        out += ", StatementList: " + str(self.statement_list)
        out += ")"
        return out