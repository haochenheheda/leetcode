def j(x1,x,y,t0,t1,t2,s):
	t = 0
	while True:
		if t%t0 == 0:
			s -= x1
			if s <= 0:
				return 'NO'
		if t%t1 == 0:
			s -= y
			if s <= 0:
				return 'YES'
		if t%t2 == 0:
			s -= x
			if s <= 0:
				return 'YES'
		t += 1
		print(t,s)
t = int(raw_input().strip())
for _ in range(t):
	s = int(raw_input().strip())
	n,d,x,y = map(int,raw_input().strip().split())
	t0,t1,t2 = map(int,raw_input().strip().split())
	x1 = n * d
	print(j(x1,x,y,t0,t1,t2,s))
