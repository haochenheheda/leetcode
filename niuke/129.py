a,b = map(int,raw_input().strip().split())
tmp = 0
a_sum = 0
b_sum = 0
while tmp ** 2 <= b:
	if tmp %2 == 0:
		if tmp ** 2 <= a:
			a_sum += min(a,(tmp+1)**2) - tmp ** 2
		b_sum += min(b+1,(tmp+1)**2) - tmp ** 2
	tmp += 1
print(b_sum - a_sum)
