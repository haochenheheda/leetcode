def j(n,lst):
	l_lst = []
	r_lst = []
	for i in range(1,len(lst)):
		l = min(lst[i-1],lst[i])
		r = max(lst[i-1],lst[i])
		for (l_,r_) in zip(l_lst,r_lst):
			if (l > l_ and l < r_ and r > r_) or (r > l_ and r < r_ and l < l_):
				return 'y'
		l_lst.append(l)
		r_lst.append(r)
	return 'n'

# def jj(n,lst):
# 	if n == 1:
# 		return 'n'
# 	else:
# 		l = min(lst[0],lst[1])
# 		r = max(lst[0],lst[1])
# 		l_ = lst[0]
# 		r_ = lst[0]
# 		for i in range(2,len(lst)):
# 			if lst[i] > l_ and lst[i] < r_:
# 				return 'n'
# 			if lst[i] > l and lst[i] < r:
				
t = int(raw_input().strip())
for _ in range(t):
	n = int(raw_input().strip())
	lst = list(map(int,raw_input().strip().split()))
	print(j(n,lst))
