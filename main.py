"""
TODO code constructor with list
TODO func of deleting. fix deleting first element
TODO solve optional task
"""

"""
поводы доебаться до Айдана
1) insert or set?
2) del 0 element
"""

from list.List import List

if __name__ == "__main__":
    a = List([1, 2, 3])
    a.insert(2, 100)
    a.insert(3, 125)
    print(a)
    a.pop(0)
    a.pop(3)
    print(a)
