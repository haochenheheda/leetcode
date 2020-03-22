lst = ["a","ab","abc","cd","bcd","abcd"]
len_ = len(lst)
max_ = 0
for i in range(len_-1):
	tmp1 = lst[i]
	len_1 = len(tmp1)
	for j in range(i+1,len_):
		tmp2 = lst[j]
		len_2 = len(tmp2)
		if len_1 * len_2 <= max_:
			continue

		flag = True
		for ind1 in range(len_1):
			for ind2 in range(len_2):
				if tmp1[ind1] == tmp2[ind2]:
					flag = False
					break
			if flag == False:
				break
		if flag == True:
			max_ = len_1 * len_2

print(max_)
