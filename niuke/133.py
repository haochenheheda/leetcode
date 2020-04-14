c,x = map(int,raw_input().strip().split())
lst = list(map(int,raw_input().strip().split()))
l = 0
r = 0
num = 0
sum_ = 0
while True:
	while r < c and sum_ < x:
		sum_ += lst[r]
		r += 1
	if sum_ < x:
		break
	num += (c - r + 1)
	sum_ -= lst[l]
	l += 1
print(num)
