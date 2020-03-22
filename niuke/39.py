lst = list(map(int,raw_input().strip().split()))

len_ = len(lst)
max_ = 0
buy_ind = 0
buy_v = lst[0]
for i in range(1,len_):
	if lst[i] - buy_v > max_:
		max_ = lst[i] - buy_v
	if lst[i] < buy_v:
		buy_v = lst[i]
		buy_ind = i


print(max_)