from list.MyList import List
"""
TODO code constructor with list
TODO func of deleting. fix deleting first element 
TODO solve optional task 
"""

a = List(1)
b = List(2)
c = List(3)

x = List(10)

a.next_node = b
b.next_node = c


if __name__ == "__main__":
    a.append(100)
    a.print_list()
    a.pop(0)
    a.print_list()
    # print(c.data)