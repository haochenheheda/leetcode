n,m = map(int,raw_input().strip().split())
lst = map(int,raw_input().strip().split())
lst1 = [i for i in lst]
tp = [raw_input().strip() for _ in range(m)]
for s in tp:
	if s[0] == '2':
		_,x,v = map(int,s.split())
		while v > 0 and x <= n:
			lst1[x-1] = lst1[x-1] - min(v,lst1[x-1])
			v = v - lst1[x-1]
			x += 1

	else:
		_,k = map(int,s.split())
		print(lst[k-1] - lst1[k-1])