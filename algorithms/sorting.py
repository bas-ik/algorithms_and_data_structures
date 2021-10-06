class Sorting:
    # def __init__(self, data: list):
    #     self.data = data
    @staticmethod
    def _insertion_sort(data):                  # сортировка вставками
        for i in range(1, len(data)):
            tmp = data[i]
            j = i - 1
            while (j >= 0) and (data[j] > tmp):
                data[j+1] = data[j]
                j -= 1
            data[j+1] = tmp

    @staticmethod
    def _calculate_minrun(n):
        r = 0
        while n >= 64:
            r |= n & 1
            n >>= 1
        return n + r

    @staticmethod
    def sort(data):
        Sorting._insertion_sort(data)
        print(data)
