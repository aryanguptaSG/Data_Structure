class queue():
	"""docstring for queue"""
	def __init__(self, size=5):
		self.size=size
		self.rear=-1
		self.front=0
		self.arr=size*[None]

	def push(self,value):
		if(self.rear==self.size-1):
			print("queue is full")
			return 0
		else:
			self.rear+=1
			self.arr[self.rear]=value
			print(value, " is added is queue")
			print("front ",self.front)
			print("rear ",self.rear)

	def pop(self):
		if(self.front>self.rear):
			print("queue is empty")
			return 0
		else:
			print(self.arr[self.front], " is poped")
			self.front+=1
			print("front ",self.front)
			print("rear ",self.rear)

	def display(self):
		for i in range(self.front,self.rear+1):
			print(self.arr[i],"\n")


		
list = queue(10)
list.push(5)
list.push(6)
list.push(7)
list.push(54)
list.push(53)
list.push(52)
list.display()
list.pop()
list.pop()
list.pop()
list.display()
list.pop()
list.pop()
list.pop()
list.pop()
list.push(54)
list.push(53)
list.push(52)


