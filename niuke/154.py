n = int(raw_input().strip())
l = 1
r = n/10
def compare(n,m):
	sum1 = 0
	sum2 = 0
	while n > 0:
		sum1 += min(n,m)
		n -= min(n,m)
		sum2 += n/10
		n -= n/10
	return sum1 >= sum2

while l < r:
	m = (l+r)/2
	if compare(n,m):
		r = m
	else:
		l = m + 1
print(l)