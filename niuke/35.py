x = int(raw_input().strip())
if x == 1:
	print(1)
else:
	out = 1
	sum_ = 1
	tmp = 1

	while True:
		tmp *= 2
		sum_ += tmp
		out += 1
		if x <= sum_:
			break
	print(out)