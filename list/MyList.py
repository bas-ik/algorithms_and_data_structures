class List:
    def __init__(self, data: float):
        self.data = data
        self.next_node = None

    def __str__(self):
        return str(self.data)

    def print_list(self):
        """print list from current element to end"""
        reference = self
        while reference is not None:
            print(reference.data)
            reference = reference.next_node

    # def create_list(self, data: list):
    #
    #     for i in data:

