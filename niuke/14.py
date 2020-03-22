import bisect
n = 3
k = 2
a = [5,8,5]
tmp = sorted(enumerate(a),key = lambda x:x[1])
s_a = [i for _,i in tmp]
ind_list = [i for i,_ in tmp]

op_list = []
op_time = 0
flag = -1
while True:
	if max(s_a) - min(s_a) <= 1:
		break
	if flag != 1:
		min_ind = bisect.bisect_left(s_a,min(s_a))
		min_num = bisect.bisect_right(s_a,min(s_a))

	max_ind = bisect.bisect_left(s_a,max(s_a))
	max_num = len(s_a) - max_ind
	if min(min_num,max_num) > k - op_time:
		break

	if min_num <= max_num:
		flag = 0
		op_time += min_num
		for i in range(min_num):
			op_list.append([ind_list[max_ind]+1,ind_list[min_ind]+1])
			s_a[min_ind] +=1
			s_a[max_ind] -=1
			min_ind+=1
			max_ind+=1
	else:
		flag = 1
		min_num -= max_num
		op_time += max_num
		for i in range(max_num):
			op_list.append([ind_list[max_ind]+1,ind_list[min_ind]+1])
			s_a[min_ind] += 1
			s_a[max_ind] -= 1
			min_ind+=1
			max_ind+=1

# print(max(s_a)-min(s_a),op_time,op_list)
print(str(max(s_a)-min(s_a)) + ' ' + str(op_time))
for st in op_list:
	print(str(st[0]) + ' ' + str(st[1]))



