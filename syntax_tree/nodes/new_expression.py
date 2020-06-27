class New:
    def __init__(self, class_name):
        self.class_name = class_name

    def __str__(self):
        return "New(" + self.class_name + ")"

    def toJavaScript(self):
        return "new " + self.class_name