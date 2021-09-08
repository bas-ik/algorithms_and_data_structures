from list.MyList import List
"""
TODO code constructor with list
TODO func of inserting
TODO func of deleting
TODO solve optional task 
"""

a = List(1)
b = List(2)
c = List(3)

a.next_node = b
b.next_node = c


if __name__ == "__main__":
    a.insert(2, 10)
    a.print_list()

