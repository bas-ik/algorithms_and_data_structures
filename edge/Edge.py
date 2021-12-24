class Edge:
    def __init__(self, vertex1: str, vertex2: str, weight: int):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight

    def __str__(self):
        return f"({self.vertex1}, {self.vertex2}) with weight = {self.weight} \n"

    def __repr__(self):
        return self.__str__()
