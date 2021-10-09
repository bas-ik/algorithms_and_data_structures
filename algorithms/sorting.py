class Sorting:
    # def __init__(self, data: list):
    #     self.data = data

    @staticmethod
    def _insertion_sort(data, start, end):
        """
        sorting part of array from start to end
        :param data: array that will be sorted
        :param start: start of sorting (inclusive)
        :param end: end of sorting (inclusive)
        """
        for i in range(1 + start, end + 1):
            tmp = data[i]
            j = i - 1
            while (j >= start) and (data[j] > tmp):
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = tmp

    # @staticmethod
    # def _reverse_run(data, start, end):
    #     for i in range(len(data) // 2):
    #         data[start], data[end] = data[end], data[start]
    #         start += 1
    #         end -= 1
    #
    # @staticmethod
    # def _get_minrun(data, min_run, start):  # returns length of run
    #     if start + min_run > len(data):
    #         Sorting._insertion_sort(data, start, len(data) - 1)
    #         print("last sorted array", data[start:start + min_run])
    #         return start + min_run
    #     if data[start] <= data[start + 1]:
    #         increase = True
    #     else:
    #         increase = False
    #     length = 1
    #     i = start
    #     if increase:
    #         while i < len(data) and data[i] <= data[i + 1]:
    #             length += 1
    #             i += 1
    #             print("increase", length)
    #         if length < min_run:
    #             Sorting._insertion_sort(data, length + 1, min_run)
    #             print("sorted array", data[start:start + min_run])
    #             return min_run
    #         print("sorted array", data[start:start + length])
    #         return length
    #     else:
    #         while i < len(data) and data[i] > data[i + 1]:
    #             length += 1
    #             i += 1
    #             print("decrease", length)
    #         if length < min_run:
    #             Sorting._reverse_run(data, start, start + length)
    #             Sorting._insertion_sort(data, length + 1, length + min_run)
    #             print("sorted array", data[start:start + min_run])
    #             print("all array", data[:])
    #             return min_run
    #         else:
    #             Sorting._reverse_run(data, start, start + length)
    #         # Sorting._insertion_sort(data, start, start + length)
    #         # print("3")
    #         print("sorted array", data[start:start + length])
    #         print("all array", data[:])
    #         return length
    #
    # @staticmethod
    # def _get_minruns(data, min_run):
    #     length = 0
    #     while length < len(data):
    #         length += Sorting._get_minrun(data, min_run, length)

    # @staticmethod
    # def _calculate_minrun(n):
    #     r = 0
    #     while n >= 64:
    #         r |= n & 1
    #         n >>= 1
    #     return n + r
    #
    # @staticmethod
    # def _merge(data, ):
    #     pass
    #
    # @staticmethod
    # def _divide_and_sort(data, n, min_run):
    #     for start in range(0, n, min_run):
    #         end = min(start + min_run - 1, n - 1)  # нужно чтобы не выйти за массив
    #         Sorting._insertion_sort(data, start, end)

    @staticmethod
    def sorting_subarrayes(data, minrun):
        length, start = 0, 0
        data_len = len(data)
        while length < data_len - 1:
            if data[length] < data[length + 1]:
                length += 1
            else:
                if length - start < minrun - 1:
                    Sorting._insertion_sort(data, start, min(start + minrun - 1,  data_len - 1))
                    length = start + minrun - 1
                print(data[start:length + 1])
                length += 1
                start = length
        print(data)

    @staticmethod
    def sort(data):
        # n = len(data)
        # min_run = Sorting._calculate_minrun(n)
        min_run = 3
        # Sorting._get_minruns(data, min_run)
        a = [3, 4, 5, 6, 0, 2, 8, 1, -5, -6]
        Sorting.sorting_subarrayes(a, minrun=4)
