from node import node
class Queue:
	def __init__(self):
		self.head=None
		self.size=0
	"""checks if queue is empty"""
	def isEmpty(self):
		return self.head==None
	"""add element to start of queue"""
	def enqueue(self,val):
		self.head=node(val,self.head)
		self.size+=1
	"""removes element from front of queue and returns it"""
	def dequeue(self):
		if self.isEmpty():
			raise Exception("queue has not elements to remove")
		element=self.head.val
		self.head=self.head.next
		self.size-=1
		return element
	"""return the first element in the queue"""
	def peek(self):
		if self.isEmpty():
			raise Exception("queue has not elements to remove")
		return self.head.val
	"""returns the size of tht queue"""
	def __len__(self):
		return self.size






