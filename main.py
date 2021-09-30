from list.List import List
from my_array.Array import MyArray
from stack.Stack import Stack
from algorithms.infix_to_postfix.Infix_to_postfix import InfixToPostfix as ITP

if __name__ == "__main__":
    a = List([10, 20, 30, 40])
    print(a)
    a.append(10)
    print(a)
    a.pop()
    print(a)

    b = MyArray([1, 2, 3])
    print(b)
    b.insert(2, 333)
    b.insert(2, 111)
    print(b)
    b.pop(1)
    print(b)

    c = Stack([1, 2, 3])
    print(c)    # последний элемент стека -- самый правый

    algorithm = ITP("10 + sin(20) - cos(30 * 4) ^ 5")
    algorithm.start()   # запуск перевода
