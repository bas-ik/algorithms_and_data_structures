class MyArray:

    def __init__(self, data=None):
        if (type(data) is list) or (type(data) is tuple):
            self.array = list(data)
            self.elem_count = len(data)

        elif data is None:
            self.array = []
            self.elem_count = 0
        #elif (type(data) is int) or (type(data) is float) or (type(data) is str):
        else:
            self.array = list(data)
            self.elem_count = 1

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
        if self.array is not None:
            for i in self.array:
                if i is not None:
                    string += str(i) + ' '
            return string
        else:
            return None

    def insert(self, index, data):
        elements_count, flag = len(self), 0
        element_count = len([i for i in self.array if i is not None])
        if self.elem_count == 0:
            self.array = [data]
        elif element_count == len(self.array):
            new_data = [None] * elements_count * 2
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
        else:
            flag = 0
            for i in range(elements_count):
                if flag == 1:
                    self.array[i], tmp = tmp, self.array[i]
                if i == index:
                    tmp = self.array[i]
                    self.array[i] = data
                    flag = 1

    def my_append(self, data):
        self.insert(self.elem_count, data)
        self.elem_count += 1

    def pop(self, index):
        elements_count = len(self.array)
        if elements_count == 0:
            raise ValueError("array is empty")
        if (index < 0) and (index >= elements_count):
            raise ValueError("index doesn\'t exist")
        del self.array[index]


if __name__ == '__main__':
    a = MyArray([1, 2, 3])
    # print(a)
    a.my_append(10)
    print(a)
    a.my_append(100)
    print(a)
    # a.insert(5, "Y")
    # print(a)
