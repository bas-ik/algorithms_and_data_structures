from list.ListElement import _ListElement


class List:
    def __initialize_element(self, data):
        self.head = _ListElement(data)

    def __initialize_array(self, data):
        self.head = _ListElement(data[0])
        tmp = self.head
        for i in data[1:]:
            tmp.next_node = _ListElement(i)
            tmp = tmp.next_node

    def __init__(self, data):
        if type(data) is list:
            print("it's list")
            self.__initialize_array(data)
        elif (type(data) is float) or (type(data) is int):
            self.__initialize_element(data)
            print("it's float/int variable")
        else:
            raise TypeError('expected array (list) or float (int) variable')

    def __len__(self):
        if self.head is None:
            return 0
        reference, list_len = self.head, 0
        while reference.next_node is not None:
            reference = reference.next_node
            list_len += 1
        return list_len + 1

    def __str__(self):
        reference, string = self.head, ""
        while reference is not None:
            string += str(reference.data) + '->'
            reference = reference.next_node
        string += "None"
        return string

    def append(self, data):
        """
        insert value at the end of the list

        :param data: data to insert into the end of the list
        :return: None
        """
        reference = self.head
        while reference.next_node is not None:
            reference = reference.next_node
        reference.next_node = _ListElement(data)

    def insert(self, index, data):
        """
        insert a element to the list

        :param index: the index where the element needs to be inserted
        :param data: data to insert into the list
        :return: the head of the list
        """
        number, reference = 0, self.head
        while (reference is not None) and (number != index):
            reference = reference.next_node
            number += 1
        if reference is None:
            raise ValueError('index doesn\'t exist')
        reference.data, tmp = data, reference.data
        while reference.next_node is not None:
            reference = reference.next_node
            reference.data, tmp = tmp, reference.data
        last_elem = _ListElement(tmp)
        reference.next_node = last_elem
