class Node:
        def __init__(self, value):
            self.value = value
            self.next = None


class List:

        def __init__(self, node):
            self.head = node

        def push(self, node):
            auxNode = self.traverse()
            auxNode.next = node

        def pushCycle(self, node, pointer):
            auxNode = self.traverse()
            auxNode.next = node
            targetNode = self.goTo(pointer-1)
            node.next = targetNode

        def appendAt(self, index, node):
            rootNode = self.goTo(index-1)
            node.next = rootNode.next
            rootNode.next = node

        def goTo(self, index):
            auxNode = self.head
            for i in range(index):
                if auxNode.next:
                    auxNode = auxNode.next

            return auxNode

        def traverse(self):
            visitedNodes = []
            auxNode = self.head
            while auxNode.next and auxNode.next.value not in visitedNodes: 
                visitedNodes.append(auxNode.value)
                auxNode = auxNode.next
                
            return auxNode

        def printList(self):
            visitedNodes = set()
            auxNode = self.head
            print(auxNode.value)
            while auxNode.next and auxNode.next.value not in visitedNodes: 
                visitedNodes.add(auxNode.value)
                auxNode = auxNode.next
                print(auxNode.value)

        # This way of checking if a list is cyclic has a time of O(n) + O(c)
        # So it would be O(n + c) = O(n)
        # Its good but it requires memory to store the set
        # Instead we could have 2 separate pointers traversing the list,
        # one faster than the other one, initializing one pointer ahead of the other
        # if the faster pointer is ever behind the slow pointer, then the list is
        # cyclic, and there is no need for that extra memory. 
        def isCyclic(self):
            visitedNodes = set()
            auxNode = self.head
            while auxNode.next: 
                visitedNodes.add(auxNode.value)
                auxNode = auxNode.next
                if auxNode.value in visitedNodes: 
                    return True

            return False

list = List(Node(1))

list.push(Node(3))

list.push(Node(5))

list.push(Node(6))

list.appendAt(2, Node(4))

list.appendAt(1, Node(2))

# list.pushCycle(Node(7), 1)

list.printList()

print(list.isCyclic())


