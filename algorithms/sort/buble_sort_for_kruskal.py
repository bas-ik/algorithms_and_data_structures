from edge.Edge import Edge


class Sort:
    @staticmethod
    def bubbleSort(edges_list: list[Edge]):
        n = len(edges_list)

        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if edges_list[j] is not None and edges_list[j + 1] is not None and edges_list[j].weight > edges_list[
                    j + 1].weight:
                    edges_list[j], edges_list[j + 1] = edges_list[j + 1], edges_list[j]
