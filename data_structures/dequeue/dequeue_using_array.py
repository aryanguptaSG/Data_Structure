class dequeue():
	"""docstring for dequeue"""
	def __init__(self, size=5):
		self.size = size
		self.front = self.rear = -1
		self.array = size*[None]

	def pushfront(self,value):
		if(self.front-1==self.rear):
			print("dequeue is full")
			return 0;
		elif(self.front ==-1):
			self.front=self.size-1
		else:
			self.front-=1
			self.array[self.front]=value
		print(value," is added in dequeue")
		print("front is : ",self.front)

	def pushback(self,value):
		if(self.rear+1==self.front or self.rear==self.size-1):
			print("dequeue is full")
			return 0;
		else:
			self.rear+=1
			self.array[self.rear]=value
			print(value," is added in dequeue")
			print("rear is : ",self.rear)

		



dequ = dequeue()
dequ.pushback(10)
dequ.pushback(10)
dequ.pushback(10)
dequ.pushback(10)
dequ.pushback(10)
dequ.pushback(10)
dequ.pushback(10)




