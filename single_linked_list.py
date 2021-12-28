from node import node

class SingledLinkedList:
	def __init__(self):
		self.head=None
		self.length=0
	"""insert element to end of list"""
	def insertEnd(self,val):
		next=node(val)
		if not self.head:
			self.head=next
		else:
			temp=self.head
			while temp.next:
				temp=temp.next
			temp.next=next
		self.length+=1
	"""insert element to start of list"""
	def insertStart(self,val):
		next=node(val)
		if not self.head:
			self.head=next
		else:
			temp=self.head
			self.head=next
			self.head.next=temp
		self.length+=1
	"""checks if list contains a certain element"""
	def has(self,val):
		temp=self.head
		while temp:
			if temp.val==val:
				return True
			temp=temp.next
		return False
	"""remove element at index"""
	def removeAtIndex(self,index):
		temp=self.head
		if index>=self.length:
			raise Exception("Index outside of bounds")
		if index==0:
				self.head=self.head.next
		for i in range(0,index-1):
			temp=temp.next
		if self.length-1==index:
			temp.next=None
		else:
			temp.next=temp.next.next
	"""checks if list is empty"""
	def isEmpty(self):
		return self.head==None
	"""returns the length of list"""
	def __len__(self):
		return self.length
	"""return the list as a string"""
	def __str__(self):
		StringList="[ "
		temp=self.head
		while temp:
			StringList+=f"{str(temp.val)} ,"
			temp=temp.next
		StringList+="]"
		return StringList