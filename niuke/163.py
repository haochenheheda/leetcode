n = int(raw_input().strip())
r = 0
while n > 0:
	r += n&1
	n = n >> 1
print(r)