from list.List import List


class Stack:

    def __str__(self):
        string = str(self._stack)
        values = string.split('->')
        string = ""
        for i in [str(i) + "->" for i in values[::-1]]:
            string += i
        return string[:-2]

    def __init__(self, data):
        if type(data) is list:
            self._stack = List(data[::-1])
            self.count = len(data)
        else:
            self._stack = List(data)
            self.count = 1
        self.last_elem = self._stack.get(0)


    def pop(self):
        if self.last_elem is not None:
            element = self.last_elem
            self._stack.remove(0)
            self.last_elem = self._stack.get(0)
            self.count -= 1
            return element
        else:
            return None

    def pushback(self, data):
        # if self._stack.get(0) is None:
        #     self._stack.set(0, data)
        # else:
        self._stack.insert(0, data)
        self.last_elem = self._stack.get(0)
        self.count += 1

    def get(self, index):
        return self._stack.get(index)

    def get_data(self):
        return self.last_elem.data
