# a = 'asdfsdfsdfsdfs'
# b = 'asd'
# a = 'devsc' 
# b = 'devscdf'
a = 'dscsdadvdvdf'
b = 'dfasdfew'
len_a = len(a)
len_b = len(b)
if len_a < len_b:
	tmp = a
	a = b
	b = tmp
	tmp = len_a
	len_a = len_b
	len_b = tmp

flag = False
for ind_a in range(len_a):
	ind_b = 0
	while True:
		if ind_b == len_b:
			flag = True
			break
		if ind_a == len_a:
			break
		if a[ind_a] == b[ind_b]:
			ind_a += 1
			ind_b += 1
		else:
			break
	if flag == True:
		break
if flag == True:
	print(1)
else:
	print(0)


