import sys
n,m = map(int,raw_input().strip().split())
map_ = {}
lst = []
for _ in range(n):
	x,y = map(int,raw_input().strip().split())
	lst.append([x,y])
	map_[x] = map_.setdefault(x,0) + 1

def find_max(map_):
	max_ = 0
	max_k = None
	for k,v in map_.items():
		if v >= max_:
			max_ = v
			max_k = k
	return max_k,max_

def find_ind(max_,lst):
	min1 = sys.maxint
	ind1 = 0
	min2 = sys.maxint
	ind2 = 0
	for i in range(len(lst)):
		if lst[i][1] < min1 and lst[i][0] != 1:
			min1 = lst[i][1]
			ind1 = i
		if lst[i][1] < min2 and lst[i][1] == max_:
			min2 = lst[i][1]
			ind2 = i
	return ind1,ind2

def dfs(cost,map_,lst):
	max_k,max_ = find_max(map_) 
	if max_k == 1:
		return cost
	else:
		ind1,ind2 = find_ind(max_,lst)
		map_[1] = map_.setdefault(1,0) + 1

		map_[lst[ind1][0]] -= 1
		tmp = lst[ind1][1]
		lst[ind1][1] = sys.maxint
		x1 = dfs(cost + tmp,map_,lst)
		x2 = sys.maxint
		if ind1 != ind2:
			map_[lst[ind1][0]] += 1
			lst[ind1][1] = tmp
			map_[lst[ind2][0]] -= 1
			tmp = lst[ind2][1]
			lst[ind2][1] = sys.maxint
			x2 = dfs(cost + tmp,map_,lst)
		return min(x1,x2)

print(dfs(0,map_,lst))

