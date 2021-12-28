from binary_tree import BinaryTree
class BST:
	def __init__(self,val=None):
		self.val=val
		self.left=None
		self.right=None

	def isEmpty(self):
		return self.val==None
	def insert(self,val):
		if self.isEmpty():
			self.val=val
		else:
			if val<self.val:
				if self.left:
					self.left.insert(val)
				else:
					self.left=BST(val)
			else:
				if self.right:
					self.right.insert(val)
				else:
					self.right=BST(val)
	
	def getRoot(self):
		return self.val

	def printInOrder(self):
		if self.left:
			self.left.printInOrder()
		print(self.getRoot())
		if self.right:
			self.right.printInOrder()
	def printPreOrder():
		print(self.getRoot())
		if self.left:
			self.left.printPreOrder()
		if self.right:
			self.right.printPreOrder()
	def printPostOrder():
		if self.left:
			self.left.printPostOrder()
		if self.right:
			self.right.printPostOrder()
		print(self.getRoot())






