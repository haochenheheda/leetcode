lst = list(raw_input().strip().split())
x = int(raw_input().strip())


flag = False
c = list(range(4))
for i in c:
	c_i = [c_ for c_ in c if c_ != i]
	for j in c_i:
		c_j = [c_ for c_ in c_i if c_ != j]
		for m in c_j:
			c_m = [c_ for c_ in c_j if c_ != m]
			for n in c_m:
				for op1 in ['+','-','*','/']:
					for op2 in ['+','-','*','/']:
						for op3 in ['+','-','*','/']:
							if eval(lst[i] + op1 + lst[j] + op2 + lst[m] + op3 + lst[n]) == x:
								flag = True
								break

if flag == True:
	print(1)
else:
	print(0)

