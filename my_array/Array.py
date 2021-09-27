class MyArray:

    def __init__(self, data):
        if (type(data) is list) or (type(data) is tuple):
            self.array = list(data)
        elif (type(data) is int) or (type(data) is float):
            self.array = list(data)
        else:
            raise TypeError("expected list (tuple) or int (float) variables")

    def get(self, index):
        elements_count = len(self.array)
        if (index < 0) and (index >= elements_count):
            raise ValueError("index doesn\'t exist")
        return self.array[index]

    def set(self, index, data):
        elements_count = len(self.array)
        if (index < 0) and (index >= elements_count):
            raise ValueError("index doesn\'t exist")
        self.array[index] = data

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
        for i in range(elements_count + 1):
            if i != index:
                if flag == 0:
                    new_data[i] = self.array[i]
                if flag == 1:
                    new_data[i] = self.array[i - 1]
            else:
                new_data[i] = data
                flag = 1
        if elements_count + 1 == index:
            new_data[-1] = data
        self.array = new_data

    def pop(self, index):
        elements_count = len(self.array)
        if elements_count == 0:
            raise ValueError("array is empty")
        if (index < 0) and (index >= elements_count):
            raise ValueError("index doesn\'t exist")
        del self.array[index]
