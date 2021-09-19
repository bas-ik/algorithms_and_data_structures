

class MyArray:

    def __init__(self, data):
        if (type(data) is list) or (type(data) is tuple):
            self.array = list(data)
        elif (type(data) is int) or (type(data) is float):
            self.array = list(data)
        else:
            raise TypeError("expected list (tuple) or int (float) variables")

    def __len__(self):
        elements_count = 0
        for _ in self.array:
            elements_count += 1
        return elements_count

    def __str__(self):
        string = ""
        for i in self.array:
            string += str(i) + " "
        return string

    def insert(self, index, data):
        elements_count, flag = len(self), 0
        new_data = [None] * (elements_count + 1)
        for i in range(elements_count):
            if i != index:
                if flag == 0:
                    new_data[i] = self.array[i]
                if flag == 1:
                    new_data[i + 1] = self.array[i]
            else:
                new_data[i] = data
