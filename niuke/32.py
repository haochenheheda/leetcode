import sys
# lst = list(map(int,raw_input().strip().split(',')))
lst = [3,-5,7,-2,8]


#################solution2###################
if max(lst) <= 0:
	print(0)
else:
	tmp = 0
	if lst[0] >= 0:
		flag =1
	else:
		flag = 0
	merge_lst = []
	for i in lst:
		if i >= 0 and flag == 1:
			tmp += i
		if i < 0 and flag == 0:
			tmp += i
		if i >= 0 and flag == 0:
			merge_lst.append(tmp)
			tmp = i
			flag = 1
		if i < 0 and flag == 1:
			merge_lst.append(tmp)
			tmp = i
			flag = 0
	merge_lst.append(tmp)


	len_ = len(merge_lst)
	dp_yes = [0] * len_
	dp_no = [0] * len_
	dp_yes[0] = merge_lst[0]
	dp_no[0] = 0
	for i in range(1,len_):
		dp_yes[i] = max(dp_yes[i-1] + merge_lst[i],merge_lst[i])
		dp_no[i] = max(dp_yes[i-1],dp_no[i-1])
	print(max(dp_yes[len_-1],dp_no[len_-1]))

#################solution1###################
# if max(lst) <= 0:
# 	print(0)
# else:
# 	zheng_num = 0
# 	zheng_sum = 0
# 	tmp = 0
# 	if lst[0] >= 0:
# 		flag =1
# 	else:
# 		flag = 0
# 	merge_lst = []
# 	for i in lst:
# 		if i >= 0 and flag == 1:
# 			tmp += i
# 		if i < 0 and flag == 0:
# 			tmp += i
# 		if i >= 0 and flag == 0:
# 			merge_lst.append(tmp)
# 			tmp = i
# 			flag = 1
# 		if i < 0 and flag == 1:
# 			zheng_num += 1
# 			zheng_sum += tmp
# 			merge_lst.append(tmp)
# 			tmp = i
# 			flag = 0
# 	if tmp >= 0:
# 		zheng_num += 1
# 		zheng_sum += tmp
# 	merge_lst.append(tmp)

# 	for _ in range(zheng_num-1):

# 		zheng_min = 100000000
# 		fu_max = -1000000000
# 		for i in merge_lst:
# 			if i >= 0 and i < zheng_min:
# 				zheng_min = i
# 			if i < 0 and i > fu_max:
# 				fu_max = i
# 		if zheng_min < -fu_max:
# 			ind = merge_lst.index(zheng_min)

# 			merge_lst = merge_lst[:max(0,ind-1)] + [sum(merge_lst[max(0,ind-1):ind + 2])] + merge_lst[ind+2:]


# 		else:
# 			ind = merge_lst.index(fu_max)
# 			merge_lst = merge_lst[:max(0,ind-1)] + [sum(merge_lst[ind-1:ind + 2])] + merge_lst[ind+2:]
# 		# print(merge_lst)
# 	print(max(merge_lst))

