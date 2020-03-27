n = int(raw_input().strip())
if n == 1:
	print(0)
elif n == 2:
	print(1)
else:
	sum_ = 2
	f = 1
	g = 1
	while sum_ < n:
		tmp = g
		g += f
		f = tmp
		sum_ += g
	print(sum_ - g)
