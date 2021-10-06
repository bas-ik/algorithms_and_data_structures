class Sorting:
    # def __init__(self, data: list):
    #     self.data = data
    @staticmethod
    def _insertion_sort(data, start, end):                  # сортировка вставками
        for i in range(1 + start, end + 1):
            tmp = data[i]
            j = i - 1
            while (j >= start) and (data[j] > tmp):
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
    def _divide_and_sort(data, n, min_run):
        for start in range(0, n, min_run):
            end = min(start + min_run - 1, n - 1)   # нужно чтобы не выйти за массив
            Sorting._insertion_sort(data, start, end)

    @staticmethod
    def sort(data):
        n = len(data)
        min_run = Sorting._calculate_minrun(n)
        Sorting._divide_and_sort(data, n, min_run)


