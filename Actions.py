__doc__ = "This file defines a set of Actions corresponding to the leafs in Composite Pattern"

class HelloAction:

    def __init__(self):
        self.label = "Say Hello"

    def execute(self):
        print("")
        print (">> Hello world!")


class GoodbyeAction:

    def __init__(self):
        self.label = "Say Goodbye"

    def execute(self):
        print("")
        print (">> Goodbye world!")


class SumAction:

    def __init__(self):
        self.label = "(a+b)"

    def execute(self):
        a = int(input("Insert first operand:"))
        b = int(input("Insert second operand:"))
        print("")
        print (">> {} + {} = {}".format(a, b, a + b))

class SubAction:

    def __init__(self):
        self.label = "(a-b)"

    def execute(self):
        a = int(input("Insert first operand:"))
        b = int(input("Insert second operand:"))
        print("")
        print (">> {} - {} = {}".format(a, b, a - b))

class PrintVersionAction:

    def __init__(self, label):
        self.label = label

    def execute(self):
        print("")
        print (">> Menu built with Composite Pattern. v1.0")