n = 5
a = [2,7,3,4,9]
m = 3
q = [1,25,11]

sorted_index = [i for i,v in sorted(enumerate(q),key=lambda x:x[1])]
res_list = [0] * m
sum_ = 0
ind = 0
for res,a_ in enumerate(a):
	sum_ += a_
	while True:
		if ind >= m:
			break
		if sum_ >= q[sorted_index[ind]]:
			res_list[sorted_index[ind]]  = res + 1
			ind+=1
		else:
			break
	if ind >= m:
		break
for i in res_list:
	print(i)

