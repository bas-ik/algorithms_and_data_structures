from list.List import List


class Queue:
    def __init__(self, data):
        self.queue = List(data)
        self.count = 1

    def add(self, data):
        self.queue.insert(self.count, data)
        self.count += 1

    def read(self):
        if self.count == 0:
            raise ValueError("out of range")
        el = self.queue
        self.queue.head = self.queue.head.next_node
        return el

        