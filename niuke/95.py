lst = list(map(int,raw_input().strip().split(',')))
x = lst[-1]
# sum_ = 0
# for i in range(len(lst)-2):
# 	for j in range(i+1,len(lst)-1):
# 		if lst[i] + lst[j] == x:
# 			sum_ += (i + j)
# print(sum_)
sum_ = 0
map_ = {}
for i in range(len(lst)-1):
	if map_.has_key(lst[i]):
		sum_ += (sum(map_[lst[i]]) + len(map_[lst[i]])*i)
	if map_.has_key(x - lst[i]):
		map_[x - lst[i]].append(i)
	else:
		map_[x - lst[i]] = [i]
print(sum_)
		