n = 4
lst = [[4,7],[2,4],[0,2],[3,6]]

lst = sorted(lst,key = lambda x: x[1])


sl = [lst[0][1]-1,lst[0][1]]
for l,r in lst[1:]:
	if l > sl[-1]:
		sl.append(r-1)
		sl.append(r)
	elif l == sl[-1]:
		sl.append(r)
	else:
		pass
print(len(sl))

# sl = [0] * 100000
# for l,r in lst:
# 	if sum(sl[l:r+1]) >= 2:
# 		continue
# 	elif sum(sl[l:r+1]) == 1:
# 		sl[r] = 1
# 	else:
# 		if r - l > 0:
# 			sl[r] = 1
# 			sl[r-1] = 1
# 		else:
# 			sl[r] = 1

# print(sum(sl))


