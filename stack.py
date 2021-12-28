from node import node
class Stack:
	def __init__(self):
		self.head=None
		self.size=0
	"""checks if stack is empty"""
	def isEmpty(self):
		return self.head==None
	"""adds element to the top of stack"""
	def push(self,val):
		if self.isEmpty():
			self.head=node(val)
		else:
			self.head=node(val,self.head)
	"""removes element from top of stack and returns it"""
	def pop(self):
		if self.isEmpty():
			raise Exception("Stack is empty")
		else:
			val=self.head.val
			self.head=self.head.next
			self.size-=1
		return val
	"""returns the top of the stack"""
	def top(self):
		if self.isEmpty():
			raise Exception("Stack is empty")
		return self.head.val
	"""return the length of the stack"""
	def __len__(self):
		return self.size