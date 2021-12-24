

class DisjointSetElement:

    def __init__(self, vertex: str, parent=None):
        if type(parent) is not DisjointSetElement and parent is not None:
            raise TypeError("parent must be DisjointSetElement")
        self.parent = parent
        self.vertex = vertex
        self.rank = 0

    def get_representative(self):
        el = self
        while el.parent is not None:
            el = el.parent

        return el

    def union(self, right_set):
        if type(right_set) is not DisjointSetElement:
            raise TypeError("anotherSet must be DisjointSetElement")

        left_repr = self.get_representative()
        right_repr = right_set.get_representative()

        if left_repr.rank > right_repr.rank:
            right_repr.parent = left_repr
        elif left_repr.rank < right_repr.rank:
            left_repr.parent = right_repr
        else:
            right_repr.rank += 1
            left_repr.parent = right_repr





def test_DSE():
    element1 = DisjointSetElement("A", None)
    element2 = DisjointSetElement("B", element1)
    element3 = DisjointSetElement("C", element2)
    element4 = DisjointSetElement("D", element2)

    assert element1.get_representative() == element1
    assert element2.get_representative() == element1
    assert element3.get_representative() == element1
    assert element4.get_representative() == element1

    # test 2
    element1 = DisjointSetElement("A", None)
    element2 = DisjointSetElement("B", element1)
    element3 = DisjointSetElement("C", None)
    element4 = DisjointSetElement("D", element3)

    element1.union(element4)

    assert element1.get_representative() == element3
    assert element2.get_representative() == element3
    assert element3.get_representative() == element3
    assert element4.get_representative() == element3
    print("success")


def test_sort():
    a = Graph()
    a.add_edge('A', 'B', 10)
    a.add_edge('A', 'C', 5)
    a.add_edge('A', 'L', 4)
    a.add_edge('A', 'Q', 14)
    a.add_edge('A', 'E', 3)
    a.add_edge('B', 'C', 20)
    a.add_edge('B', 'C', 1)
    Sort.bubbleSort(a.edges_list.array)
    print(a.edges_list)


if __name__ == '__main__':
    a = Graph()
    a.read_file()
    result = a.kruskal()
