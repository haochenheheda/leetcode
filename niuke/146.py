t = int(raw_input().strip())
for _ in range(t):
	n,k = map(int,raw_input().strip().split())
	print('0 ' + str(max(min(n-k,k-1),0)))