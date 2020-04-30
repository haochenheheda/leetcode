lst = map(int,raw_input().strip().split(','))
l = 0
r = len(lst)-1
while r-l>1:
	m = (l+r)/2
	if lst[m] == m:
		l = m
	else:
		r = m
if lst[r] - lst[l] == 2:
	print(lst[l] + 1)
elif r == len(lst)-1:
	print(lst[r] + 1)
else:
	print(lst[l] - 1)