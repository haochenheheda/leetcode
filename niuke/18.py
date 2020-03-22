import bisect
n = 5
size_ = [[2,2],[2,4],[3,3],[2,5],[4,5]]
size_ = sorted(size_,key = lambda x:x[0])
w_ = [i[0] for i in size_]
h_ = [i[1] for i in size_]

# v = []
# for i in range(len(h_)):
# 	pos = bisect.bisect(v, h_[i])
# 	if pos < len(v):
# 	    v[pos] = h_[i]
# 	else:
# 	    v.append(h_[i])
# 	print(v)
# print len(v)
# w_set = list(set(w_))

# h_used = []
# start_ind = 0

# for w in w_set:
# 	w_ind = bisect.bisect_right(w_,w)
# 	h_slice = h_[start_ind:w_ind]
# 	start_ind = w_ind

# 	h_slice.sort()
# 	h_used += h_slice

f = []
f += [1]
for i in range(1,n):
	tmp = 1
	for k in range(0,i):
		if h_[k] <= h_[i]:
			if tmp < f[k] + 1:
				tmp = f[k] + 1
		else:
			if tmp < f[k]:
				tmp = f[k]
	f += [tmp]
print(f[-1])

