
class Stack:
	def __init__(self,max_size):
		self.max_size=max_size
		self.length = 0
		self.stack=[None]*max_size
	"""ends item to end of stack"""
	def push(self,item):
		if self.length<self.max_size:
			self.stack[self.length]=item
			self.length+=1
			print(f"{str(item)} Added to stack")
		else:
			raise Exception("Stack is full stack")
	"""Check if stack has any items"""
	def isEmpty(self):
		return self.length==0
	"""Return how many items in stack"""
	def __len__(self):
		return self.length
	"""removes last item in stack and returns it"""
	def pop(self):
		if self.isEmpty():
			raise Exception("Stack is empty stack")
		pop,self.stack[self.length-1]=self.stack[self.length-1],None
		self.length-=1
		return pop
	"""returns the top item in stack"""
	def top(self):
		if self.isEmpty():
			raise Exception("Stack is empty stack")
		return stack[self.length-1]
	"""return the current stack"""
	def __str__(self):
		if self.isEmpty(): return "Empty Stack"
		return f"stack: {self.stack[0:self.length]}"

