class Node:

    def __init__(self, val, node = None):
        self.val = val
        self.next = node 

class List:

    def __init__(self, node):
        self.head = node

    def append(self, node):
        last_node = self.traverse()
        last_node.next = node

    def traverse(self):
        aux = self.head
        while aux.next:
            aux = aux.next

        return aux

    def print_list(self):
        aux = self.head
        print(aux.val)
        while aux.next:
            aux = aux.next
            print(aux.val)


my_list = List(Node(1))
    

second_node = Node(2)

my_list.append(second_node)

my_list.append(Node([1, 3, 4]))

my_list.print_list()



