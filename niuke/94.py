lst = list(map(int,raw_input().strip().split(',')))
max_ind = lst.index(max(lst))
sum_ = 0
incre_tmp = lst[0]
decre_tmp = lst[-1]
for i in range(max_ind + 1):
	if lst[i] <= incre_tmp:
		sum_ += (incre_tmp - lst[i])
	else:
		incre_tmp = lst[i]

for i in range(len(lst)-1,max_ind,-1):
	if lst[i] <= decre_tmp:
		sum_ += (decre_tmp - lst[i])
	else:
		decre_tmp = lst[i]

print(sum_)
# stack = [lst[0]]
# sum_ = 0
# for i in range(1,len(lst)):
# 	if lst[i]>=stack[0]:
# 		for s in stack:
# 			sum_+= (stack[0] - s)
# 		stack = [lst[i]]
# 	else:
# 		for j in range(len(stack)-1,0,-1):
# 			if stack[j] >= lst[i]:
# 				break
# 			else:
# 				sum_+= (lst[i] - stack[j])
# 				stack[j] = lst[i]
# 		stack.append(lst[i])
# print(sum_)

