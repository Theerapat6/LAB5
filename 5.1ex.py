class Node:
	def __init__(self, data):
		self.data = data
		self.nextval = None

class llist:
	def __init__(self):
		self.head = None

	def nodee(self, data):
		node = Node(data)
		node.nextval = self.head
		self.head = node

	def list(self):
		temp = self.head
		while(temp):
			print(temp.data, end="<->")
			temp = temp.nextval

llist = llist()
llist.nodee(4)
llist.nodee(3)
llist.nodee(2)
llist.nodee(1)

llist.list()



