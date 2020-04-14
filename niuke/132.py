n,k = map(int,raw_input().strip().split())
lst = list(map(int,raw_input().strip().split()))
lst.sort()
c = {}
for l in lst:
	c[l] = c.setdefault(l,0) + 1
if k == 1:
	print(len(c.keys()))
else:
	num = n
	for l in c.keys():
		if l*k not in c.keys():
			continue
		if c[l]==0 or c[l*k]==0:
			continue
		t = min(c[l],c[l*k])
		c[l] -= t
		c[l*k] -= t
		num -=t
	print(num)
# #ind_map = {k:i for i,k in enumerate(lst)}
# #max_num = 0
# select_map = {}
# ind = 0
# num = 0
# def dfs(ind,select_set,num):
# 	if ind >= n-2:
# 		return num
# 	tmp = lst[ind]
# 	if tmp%k!=0 or (not tmp/k in select_set.keys()):
# 		select_set[tmp] = select_set.setdefault(tmp,0) + 1
# 		num += 1
# 		return dfs(ind+1,select_set,num)
# 	else:
# 		select_set1 = select_set.copy()
# 		num1 = dfs(ind+1,select_set,num)
# 		num = num - select_set1.setdefault(tmp/k,0) + 1
# 		select_set1.pop(tmp/k)
# 		select_set[tmp] = select_set.setdefault(tmp,0) + 1
# 		num2 = dfs(ind+1,select_set1,num)
# 		return max(num1,num2)

# print(dfs(0,select_map,0))