class Operator:
    def __str__(self):
        return type(self).__name__ + "(" + str(self.left) + ", " + str(self.right) + ")"