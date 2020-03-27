class listnode():
	def __init__(self,x,p,c):
		self.x = x
		self.p = p
		self.c = c

	def a(self,c):
		self.c = c
	def b(self,p):
		self.p = p

class list_(object):
	def __init__(self):
		super(list_, self).__init__()
		self.head = listnode(None,None,None)
		self.tail = listnode(None,None,None)
		self.head.a(self.tail)
		self.tail.b(self.head)
		self.pointer = self.head

	def append(self,x):
		x = listnode(x,self.pointer,self.pointer.c)
		self.pointer.c.b(x)
		self.pointer.a(x)
		self.pointer = x

	def find(self,k):
		pointer = self.tail.p
		if pointer.x == None:
			return None
		for _ in range(k-1):
			pointer = pointer.p
			if pointer.x == None:
				return None
		return pointer.x


lst = list_()
for i in range(1,8):
	lst.append(i)

x = int(raw_input().strip())
print(lst.find(x))



		
