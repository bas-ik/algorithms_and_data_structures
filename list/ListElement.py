class ListElement:
    def __init__(self, data):
        """
        initializing the list element

        :param data: data to initialize a list element
        """
        self.data = data
        self.next_node = None

    def __str__(self):
        return str(self.data)

