class Stack():
    def __init__(self, size=5):
        self.Max_size = size
        self.arr = size * [None]
        self.top = -1

    def push(self, value):
        if self.top < self.Max_size - 1:
            self.top += 1
            self.arr[self.top] = value

        else:
            print()
            print("\nStack Overflow!")

    def pop(self):
        if self.top == -1:
            print("\nStack Underflow!")
        else:
            value = self.arr[self.top]
            self.top -= 1
            # print("Pop Sucessful!\n")
            return value

    def __str__(self):
        length = self.top
        s = ""
        for i in range(length, -1, -1):
            s = s + str(self.arr[i]) + "\n"
        return s

expression = input()
output = ""
st = Stack(20)
for i in expression:
	if i in "({[+-/*":
		st.push(i)
		# print(st)
	elif i in ")]}":
		if i==")":
			while(True):
				if st.arr[st.top]=="(":
					st.pop()
					break
				else:
					operatior = st.pop()
					output+=operatior
					# print(output)
		elif i=="}":
			while(True):
				if st.arr[st.top]=="{":
					st.pop()
					break
				else:
					operatior = st.pop()
					output+=operatior
					# print(output)

		elif i=="]":
			while(True):
				if st.arr[st.top]=="[":
					st.pop()
					break
				else:
					operatior = st.pop()
					output+=operatior
					# print(output)

	else:
		output+=i
		# print(output)

for i in range(0,st.top+1):
	operatior = st.pop()
	output+=operatior
	# print(output)



print("Postfix of expression is : ",output)













