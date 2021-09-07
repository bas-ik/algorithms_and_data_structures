from list.MyList import List

a = List(1)
b = List(2)
c = List(3)

a.next_node = b
b.next_node = c


if __name__ == "__main__":
    b.print_list()

