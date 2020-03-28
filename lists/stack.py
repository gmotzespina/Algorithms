class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class Stack:
	def __init__(self):
		self.head = None
		self.stack_length = 1

	def push(self, item):
		self.head.next = item
		self.stack_length += 1

	def pop(self):
		self.items.pop()

	def printStack(self):
		print(self.items)

	def size(self):
		print(self.stack_length)

s = Stack()

s.head = Node(1)

s.push(Node(2))

print(s.head.value)
print(s.head.next.value)
s.size()
