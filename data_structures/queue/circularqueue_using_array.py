class queue():
	"""docstring for queue"""
	def __init__(self, size=5):
		self.size = size
		self.front = self.rear = -1
		self.array = size*[None]

	def push(self,value):
		if((self.rear==self.size-1 and self.front==0) or (self.rear+1==self.front)):
			print("\nqueue is full.")
			return 0

		elif(self.rear==-1):
			self.rear=self.front=0
			self.array[self.rear]=value

		elif self.rear==self.size-1 and self.front>0:
			self.rear=0
			self.array[self.rear]=value

		else:
			self.rear+=1
			self.array[self.rear]=value

		print("\n",value, " is added in queue")
		print("\n front: ",self.front)
		print("\n rear: ",self.rear)

	def pop(self):
		if(self.front==-1):
			print("\nqueue is empty")
			return 0
		print(self.array[self.front], " is poped")
		if self.front==self.rear:
			self.front = self.rear = -1

		elif self.front==self.size-1 and self.rear>=0:
			self.front=0

		else:
			self.front+=1

		print("\n front: ",self.front)
		print("\n rear: ",self.rear)




qu=queue(5)
qu.push(1)
qu.push(2)
qu.push(3)
qu.pop()
qu.push(4)
qu.push(5)
qu.push(6)
qu.pop()
qu.pop()
qu.pop()
qu.push(7)
qu.pop()
qu.pop()
qu.pop()
qu.push(4)
qu.push(5)
qu.push(6)
qu.pop()
qu.pop()








