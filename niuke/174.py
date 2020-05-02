x,y = map(int,raw_input().strip().split())
if 2 * x < y:
	print(0)
else:
	e = y/2 + int(y%2)
	if x < y:
		print(x-e+1)
	else:
		print(y-e)
