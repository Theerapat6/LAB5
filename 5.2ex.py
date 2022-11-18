class Node:
	def __init__(self, node):
		self.node = node
		self.left = None
		self.right = None

def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.node, end=" ")
		inorder(root.right)

def ins(nodee, node):

	if nodee is None:
		return Node(node)
	if node < nodee.node:
		nodee.left = ins(nodee.left, node)
	else:
		nodee.right = ins(nodee.right, node)
	return nodee

def delete(root, node):

	if root is None:
		return root
	if node < root.node:
		root.left = delete(root.left, node)
		return root
	elif(node > root.node):
		root.right = delete(root.right, node)
		return root
	if root.left is None and root.right is None:
		return None
	if root.left is None:
		temp = root.right
		root = None
		return temp
	elif root.right is None:
		temp = root.left
		root = None
		return temp

	nodee = root
	numm = root.right

	while numm.left != None:
		nodee = numm
		numm = numm.left
	if nodee != root:
		nodee.left = numm.right
	else:
		nodee.right = numm.right
	root.node = numm.node
	return root

rr = None
rr = ins(rr, 50)
rr = ins(rr, 25)
rr = ins(rr, 75)
rr = ins(rr, 30)
rr = ins(rr, 60)
rr = ins(rr, 40)

inorder(rr)
print("\n")

print("\nDelete 30")
root = delete(rr, 30)
inorder(rr)
print("\n")

print("\nDelete 75")
rr = delete(rr, 75)
inorder(rr)
print("\n")

print("\nDelete 40")
rr = delete(rr, 40)
inorder(rr)

