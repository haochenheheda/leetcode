n,k = map(int,raw_input().strip().split())
lst = map(int,raw_input().strip().split())
l = 0
r = 0
max_ = 0
while r < n:
	if lst[r] == 1:
		r += 1
	else:
		if k > 0:
			k -= 1
			r += 1
		else:
			max_ = max(max_,r-l)
			while l<r and lst[l] == 1:
				l += 1
			l += 1
			r += 1
max_ = max(max_,r-l)
print(max_)

