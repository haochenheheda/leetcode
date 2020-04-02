lst = list(map(int,raw_input().strip().split()))
n = lst[0]
lst = lst[1:]

k_list = [0] * len(lst)
tmp_ind = 0
k_list[0] = 1
for ind in range(1,len(lst)):
	if lst[ind] > lst[ind-1]:
		k_list[ind] = k_list[ind-1]+1
		tmp_ind = ind
	elif lst[ind] < lst[ind-1]:
		k_list[ind] = 1
		for k in range(ind-1,tmp_ind,-1):
			k_list[k] += 1
		if k_list[tmp_ind] <= k_list[tmp_ind+1]:
			k_list[tmp_ind] += 1
	else:
		k_list[ind] = 1
		tmp_ind = ind
print(sum(k_list))
