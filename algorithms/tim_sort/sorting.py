from stack.Stack import Stack
from algorithms.tim_sort.run import Run


class Sorting:
    _GALOP_SIZE = 7

    def __init__(self, data: list):
        self.data = data

    @staticmethod
    def reverse(data, start_index, finish_index):
        n = (finish_index - start_index) // 2
        for i in range(n + 1):
            data[start_index + i], data[finish_index - i] = data[finish_index - i], data[start_index + i]

    @staticmethod
    def _insertion_sort(data, start_index, finish_index):
        a = finish_index - start_index + 1
        for i in range(1, a):
            key = data[start_index + i]
            j = i - 1

            while (j >= 0) and (data[start_index + j] > key):
                data[start_index + j + 1] = data[start_index + j]
                j -= 1
            data[start_index + j + 1] = key

    @staticmethod
    def _get_minrun(length):
        r = 0
        while length >= 64:
            r |= length & 1
            length >>= 1

        return length + r

    @staticmethod
    def next_run(data, index, minrun):
        distinction = len(data) - index
        if distinction <= 0:
            return None, None, index
        if distinction == 1:
            return index, 1, index
        start_index = index

        value1 = data[index]
        index += 1
        value2 = data[index]
        index += 1
        size = 2

        invert = value1 < value2

        if invert:
            last = value2
            while (index < len(data)
                   and last < data[index]):
                last = data[index]
                index += 1
                size += 1
            Sorting.reverse(data, start_index, index - 1)
        else:
            last = value2
            while (index < len(data)
                   and last >= data[index]):
                last = data[index]
                index += 1
                size += 1
        if size < minrun:
            while True:
                if index < len(data):
                    index += 1
                else:
                    break
                if size < minrun:
                    size += 1
                else:
                    break

            if not index - 1 == len(data):
                size -= 1
        index = start_index + size
        Sorting._insertion_sort(data, start_index, start_index + size - 1)
        return start_index, size, index

    @staticmethod
    def merge(data, begin_index1, size1, begin_index2, size2):
        if begin_index1 > begin_index2:
            begin_index1, begin_index2 = begin_index2, begin_index1
            size1, size2 = size2, size1

        # temp_ar = [data[i] for i in range(start_index1, start_index1 + size1)]
        tmp_data = []
        for i in range(begin_index1, begin_index1 + size1):
            tmp_data.append(data[i])

        current1 = 0
        current2 = begin_index2

        last_from_left = False
        count = 0

        until = begin_index2 + size2 - 1
        current_data = begin_index1
        while current_data <= until:

            if current1 == size1:
                if last_from_left:
                    last_from_left = False
                    count = 0
                data[current_data] = data[current2]
                current2 += 1
            elif current2 == begin_index2 + size2:
                if not last_from_left:
                    last_from_left = True
                    count = 0
                data[current_data] = tmp_data[current1]
                current1 += 1
            else:
                if tmp_data[current1] > data[current2]:
                    if last_from_left:
                        last_from_left = False
                        count = 0
                    data[current_data] = data[current2]
                    current2 += 1
                else:
                    if not last_from_left:
                        last_from_left = True
                        count = 0
                    data[current_data] = tmp_data[current1 + 1]
                    current1 += 1
            count += 1

            if count != Sorting._GALOP_SIZE:
                current_data += 1
                continue

            current_data += 1
            if last_from_left:
                if current2 == begin_index2 + size2:
                    count = 0
                    # current_ar -= 1
                    continue

                current_data, current1 = Sorting.galop(data, tmp_data, current_data, current1, data[current2])

            else:
                if current1 == size1:
                    count = 0
                    # current_ar -= 1
                    continue

                current_data, current2 = Sorting.galop(data, data, current_data, current2, tmp_data[current1])
            last_from_left = not last_from_left
            count = 0
            current_data += 1
        return begin_index1, size1 + size2

    @staticmethod
    def sort(data):
        minrun = Sorting._get_minrun(len(data))
        index = 0
        run = Run()
        flag = True
        count = 0
        while True:
            run.start_index, run.size, index = Sorting.next_run(data, index, minrun)
            if run.size is None or run.start_index is None:
                break
            if flag:
                runs = Stack(run)
                flag = False
            else:
                runs.pushback(run)
                print(runs)
            count += 1
            if count == 10: break

        while runs.count >= 3:
            x = runs.pop().data
            y = runs.pop().data
            z = runs.pop().data

            if z.size > x.size + y.size and y.size > x.size:
                runs.pushback(z)
                runs.pushback(y)
                runs.pushback(x)

                break

            if z.size >= x.size + y.size:
                new_run = Run()
                if z.size > x.size:
                    runs.pushback(x)

                    new_run.start_index, new_run.size = Sorting.merge(data, z.start_index, z.size, y.start_index,
                                                                      y.size)
                else:
                    runs.pushback(z)
                    new_run.start_index, new_run.size = Sorting.merge(data, x.start_index, x.size, y.start_index,
                                                                      y.size)
                runs.pushback(new_run)
            else:
                new_run = Run()
                new_run.start_index, new_run.size = Sorting.merge(data, y.start_index, y.size, x.start_index, x.size)
                runs.pushback(new_run)

                runs.pushback(z)

        while runs.count >= 2:
            x = runs.pop().data
            y = runs.pop().data

            new_run = Run()
            new_run.start_index, new_run.size = Sorting.merge(data, x.start_index, x.size, y.start_index, y.size)
            runs.pushback(new_run)

    @staticmethod
    def galop(data, source, current_data, src_index, compared_elem):
        start_index = src_index

        i = 0
        while src_index < len(source) and source[src_index] < compared_elem:
            i += 1
            src_index += 1 << i

        if i == 0:
            current_data -= 1
            return current_data, src_index

        src_index -= 1 << i

        for i in range(start_index, src_index - start_index + 1):
            data[current_data] = source[i]
            current_data += 1

        current_data += src_index - start_index
        src_index += 1
        return current_data, src_index
