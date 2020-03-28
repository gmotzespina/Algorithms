def fun1():
    iterable = [1, 2, 4, 5]
    string = 'test'
    for num in iterable:
        print(num)

class Node():

    def __init__(self):
        self.nums = [1,2,4]

    def print_nums(self):
        for num in self.nums:
            print(num)


node = Node()

node.print_nums()
