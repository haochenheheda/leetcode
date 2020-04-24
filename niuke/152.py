k = int(raw_input().strip())
for _ in range(k):
	n = int(raw_input().strip())
	lst = map(int,raw_input().strip().split())
	max_ = max(lst)
	min_ = min(lst)
	x = (max_ - min_)/2.
	flag = True
	for l in lst:
		if l != max_ and l != min_ and l != min_ + x:
			flag = False
			break
	if flag:
		print('YES')
	else:
		print('NO')