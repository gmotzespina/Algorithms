class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, item = None):
        self.head = item
        if item:
            self.stack_length = 1

    def push(self, item):
        if self.head == None:
            self.head = item

        pointer = self.head
        while pointer.next != None:
            pointer = pointer.next
        pointer.next = item
        self.stack_length += 1

    def pop(self):
        self.items.pop()

    def printStack(self):
        aux = self.head
        while aux:
            if aux.next:
                print(aux.value, end='->')
            else:
                print(aux.value)
            aux = aux.next

    def size(self):
        print(self.stack_length)


def findMthToLast(head, mth_element):
    first_pointer = head
    second_pointer = head

    for i in range(mth_element):
        if second_pointer:
            second_pointer = second_pointer.next
        else:
            return None

    while second_pointer != None:
        second_pointer = second_pointer.next
        first_pointer = first_pointer.next

    print('{} elements value is: {}'.format(mth_element, first_pointer.value))
    return first_pointer

stack = Stack(Node(1))

stack.push(Node(2))
stack.push(Node(9))
stack.push(Node(8))
stack.push(Node(4))
stack.push(Node(11))

stack.size()

stack.printStack()
el_num = 7 
element = findMthToLast(stack.head, el_num)
if not element:
    print('There is no {} element. The list is shorter'.format(el_num))
