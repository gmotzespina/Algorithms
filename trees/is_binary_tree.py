class Leaf:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:

    def __init__(self, item=None):
        self.head = item

    def add(self, item, head=None):
        if not head:
            if not self.head:
                self.head = item
                return

            current = self.head
        else:
            current = head

        if item.value > current.value:
            if current.right:
                self.add(item, current.right)
            else:
                current.right = item
        if item.value <= current.value:
            if current.left:
                self.add(item, current.left)
            else:
                current.left = item

    def traverse(self, node=None):

        if not node:
            node = self.head

        if node.left:
            self.traverse(node.left)

        if node.right:
            self.traverse(node.right)

        print(node.value)

tree = Tree(Leaf(4))

tree.add(Leaf(2))
tree.add(Leaf(0))
tree.add(Leaf(3))
tree.add(Leaf(6))
tree.add(Leaf(5))
tree.add(Leaf(7))
tree.traverse()
