from list.List import List


class Stack:

    def __init__(self, data):
        self.stack = List(data)

    def __str__(self):
        return str(self.stack)[:-6]     # slice is required not to print "->None"

    def pop(self):
        self.stack.pop()

    def pushback(self, data):
        self.stack.append(data)

