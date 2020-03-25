x,y = map(int,raw_input().strip().split())
out = ''
while True:
	out += str(x%y)
	x = x/y
	if x == 0:
		break
print(out[::-1])