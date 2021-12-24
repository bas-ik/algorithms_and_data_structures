from disjointset.DisjointSetElement import DisjointSetElement
from my_array.Array import MyArray
from edge.Edge import Edge
from algorithms.sort.buble_sort_for_kruskal import Sort


class Graph:
    def __init__(self):
        self.edges_list = MyArray()
        self.vertex_list = MyArray()

    def add_edge(self, vertex1: str, vertex2: str, weight: int):
        self.edges_list.my_append(Edge(vertex1, vertex2, weight))
        self.vertex_list.my_append(vertex1)
        self.vertex_list.my_append(vertex2)

    def __str__(self):
        ans = ""
        for i in self.edges_list.array:
            ans += str(i) + "\n"
        return ans

    @staticmethod
    def bubble_sort_str(arr):
        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] is not None and arr[j + 1] is not None and arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    def read_file(self):
        line = " "
        with open('edges.txt') as f:
            while line != '':
                line = f.readline()

                p = line.split(sep=" ")
                if len(p) == 3:
                    c, b, v = p[0], p[1], p[2]
                    self.add_edge(c, b, int(v))

    def kruskal(self):
        ans = 0
        result = MyArray()

        self.dsu = MyArray()
        for i in self.vertex_list.array:
            if i is not None:
                self.dsu.my_append(DisjointSetElement(i))

        Sort.bubbleSort(self.edges_list.array)

        for i in self.edges_list.array:
            if i is None:
                continue

            if type(i) is not Edge:
                raise TypeError("Wrong type for edge")

            dsu_el1 = self.find_in_dsu(i.vertex1)
            dsu_el2 = self.find_in_dsu(i.vertex2)

            repr1 = dsu_el1.get_representative()
            repr2 = dsu_el2.get_representative()

            if repr1 == repr2:
                continue

            result.my_append(str(i.vertex1) + " " + str(i.vertex2) + "\n")
            ans += i.weight
            dsu_el1.union(dsu_el2)

        Graph.bubble_sort_str(result.array)
        print("result: ")
        print(result, end="")
        print(f"length: {ans}")
        return result, ans

    def find_in_dsu(self, vertex):
        for i in self.dsu.array:
            if i is not None:
                if i.vertex == vertex:
                    return i

        raise RuntimeError("vertex not found")


if __name__ == '__main__':
    a = Graph()
    a.read_file()
    result = a.kruskal()
