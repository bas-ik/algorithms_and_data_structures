from list.List import List


class Stack:

    def __init__(self, data):
        self._stack = List(data[::-1])
        self.last_elem = self._stack.get(0)

    def __str__(self):  # 3->2->5
        string = str(self._stack)[:-6]  # slice is required not to print "->None"
        values = string.split('->')
        string = ""
        for i in [str(i) + "->" for i in values[::-1]]:
            string += i
        return string[:-2]

    def pop(self):
        self._stack.remove(0)
        self.last_elem = self._stack.get(1)

    def pushback(self, data):
        self._stack.insert(0, data)
        self.last_elem = self._stack.get(0)

    def get(self, index):
        return self._stack.get(index)
