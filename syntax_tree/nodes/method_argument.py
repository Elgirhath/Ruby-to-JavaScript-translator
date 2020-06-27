class MethodArgument:
    def __init__(self, name, default_value):
        self.name = name
        self.default_value = default_value

    def __str__(self):
        out = "MethodArgument("
        out += "Name: " + str(self.name)
        out += ", DefaultValue: " + str(self.default_value)
        out += ")"
        return out

    def toJavaScript(self):
        out = self.name.toJavaScript()
        if self.default_value:
            out += " = " + self.default_value.toJavaScript()

        return out