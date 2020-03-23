n = 2
lst = [1,2]

out = 0
def merge(lst,len_):
	global out
	if len_ <= 1:
		return lst
	l = 0
	r = len_-1
	mid = (l+r)/2
	lst1 = merge(lst[:mid+1],mid+1)
	lst2 = merge(lst[mid+1:],len_-mid-1)

	ind1 = 0
	ind2 = 0

	lst = []
	while ind1 <= mid and ind2 <= len_ - mid - 2:
		if lst1[ind1] <= lst2[ind2]:
			lst.append([lst1[ind1]]) 
			ind1 += 1
		else:
			lst.append([lst2[ind2]])
			ind2 += 1
			out += (mid - ind1 + 1)
	lst = lst + lst1[ind1:] + lst2[ind2:]
	return lst


merge(lst,n)
print(out)




# num_ = 0
# for i in range(len(lst)-1):
# 	for j in range(i + 1,len(lst)):
# 		if lst[i] > lst[j]:
# 			num_ += 1
# print(num_)


# num_ = 0
# for i in range(len(lst)-1,0,-1):
# 	for j in range(0,i):
# 		if lst[j] > lst[j+1]:
# 			tmp = lst[j]
# 			lst[j] = lst[j+1]
# 			lst[j+1] = tmp
# 			num_+=1

# print(num_)