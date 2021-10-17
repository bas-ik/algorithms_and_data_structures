from list.ListElement import ListElement


class List:
    def __initialize_element(self, data):
        """
        method to initialize List by variable
        :param data: float (int) value
        :return: the "head" of List
        """
        self._head = ListElement(data)

    def __initialize_array(self, data):
        """
        private method to initialize List by my_array
        :param data: list of int (float) variables
        :return: the "head" of list
        """
        if len(data) == 0:
            self._head = ListElement(None)
        else:
            self._head = ListElement(data[0])
            tmp = self._head
            for i in data[1:]:
                tmp.next_node = ListElement(i)
                tmp = tmp.next_node

    def __initialize_str(self, data):
        self._head = ListElement(data)

    def __initialize_something(self, data):
        self._head = ListElement(data)

    def __init__(self, data):
        """
        constructor: initialize List

        :param data: my_array (list) or float (int) variable
        """
        if type(data) is list:
            self.__initialize_array(data)
        elif (type(data) is float) or (type(data) is int):
            self.__initialize_element(data)
        elif type(data) is str:
            self.__initialize_str(data)
        else:
            self.__initialize_something(data)

    def __len__(self):
        """
        find the len of List
        :return: int value, that containing the len of List
        """
        if self._head is None:
            return 0
        reference, list_len = self._head, 0
        while reference.next_node is not None:
            reference = reference.next_node
            list_len += 1
        return list_len + 1

    def __str__(self):
        """
        converts a List to a string. Method is used for printing List

        :return: string containing data of all List element
        """
        reference, string = self._head, ""
        while reference is not None:
            string += str(reference.data) + '->'
            reference = reference.next_node
        return string[:-2]

    def get(self, index):
        """
        :return value by index

        :param index: index of return's element
        :return: ListElement object
        """
        number, reference = 0, self._head
        while (reference is not None) and (number != index):
            reference = reference.next_node
            number += 1
        if number != index:
            raise ValueError("index doesn\'t exist!")
        return reference

    def append(self, data):
        """
        insert value at the end of the list

        :param data: data to insert into the end of the list
        :return: None
        """
        reference = self._head
        while reference.next_node is not None:
            reference = reference.next_node
        reference.next_node = ListElement(data)

    def insert(self, index, data):
        """
        insert a element to the List

        :param index: the index where the element needs to be inserted
        :param data: data to insert into the list
        :return: the head of the List
        """
        if index == 0:
            tmp = self._head
            self._head = ListElement(data)
            self._head.next_node = tmp
        else:
            number, reference = 0, self._head
            while (reference is not None) and (number != index - 1):
                reference = reference.next_node
                number += 1
            if number != index - 1:
                raise ValueError('index doesn\'t exist')
            tmp = reference.next_node
            reference.next_node = ListElement(data)
            reference.next_node.next_node = tmp
            # reference.data, tmp = data, reference.data
            # while reference.next_node is not None:
            #     reference = reference.next_node
            #     reference.data, tmp = tmp, reference.data
            # last_elem = ListElement(tmp)
            # reference.next_node = last_elem

    def remove(self, index):
        """
        del element from List by index

        :param index: index of del element
        """
        if self._head is None:
            raise ValueError("List is empty")
        if index == 0:
            self._head = self._head.next_node
        else:
            number, reference = 0, self._head
            while (reference is not None) and (number != index - 1):
                reference = reference.next_node
                number += 1
            if number != index - 1:
                raise ValueError('index doesn\'t exist')
            del_elem = reference.next_node
            reference.next_node = del_elem.next_node
            del del_elem

    def set(self, index, data):
        if index == 0:
            self._head.data = data
        else:
            number, reference = 0, self._head
            while (reference is not None) and (number != index):
                reference = reference.next_node
                number += 1
            if number != index:
                raise ValueError('index doesn\'t exist')
            reference.data = data

    def pop(self):
        """
        del last element
        :return:
        """
        self.remove(len(self) - 1)
