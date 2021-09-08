class List:
    def __init__(self, data: float):
        """
        initializing the list element

        :param data: data to initialize a list element
        """
        self.data = data
        self.next_node = None

    def __str__(self):
        return str(self.data)

    def len(self) -> int:
        """
        find the length of the list

        :return: the len of the list
        """
        if self is None:
            return 0
        reference, list_len= self, 0
        while reference.next_node is not None:
            reference = reference.next_node
            list_len += 1
        return list_len+1

    def print_list(self) -> None:
        """
        print list's elements from current element to end

        :return: None
        """
        reference = self
        while reference is not None:
            print(reference.data, end='->')
            reference = reference.next_node
        print('None')

    def append(self, data):
        """
        insert value at the end of the list

        :param data: data to insert into the end of the list
        :return: None
        """
        reference = self
        while reference.next_node is not None:
            reference = reference.next_node
        reference.next_node = List(data)

    def insert(self, index, data):
        """
        insert a element to the list

        :param index: the index where the element needs to be inserted
        :param data: data to insert into the list
        :return: the head of the list
        """
        number, reference = 0, self
        while (reference is not None) and (number != index):
            reference = reference.next_node
            number += 1
        if reference is None:
            raise ValueError('index doesn\'t exist')
        reference.data, tmp = data, reference.data
        while reference.next_node is not None:
            reference = reference.next_node
            reference.data, tmp = tmp, reference.data
        last_elem = List(tmp)
        reference.next_node = last_elem

    def pop(self, index: int):
        # if index == 0:
        #     self = self.next_node
        #     return
        number, reference = 0, self
        while reference.next_node is not None and number != index - 1:
            reference = reference.next_node
            number += 1
        if number != index - 1:
            raise ValueError('index doesn\'t exist')
        del_elem = reference.next_node
        reference.next_node = del_elem.next_node
        del del_elem
