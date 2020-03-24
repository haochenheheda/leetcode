n,m = map(int,raw_input().strip().split())
re = [[0] * m for _ in range(n)]
ind = 1
for s in range(m + n - 1):
	for j in range(min(s,m-1),s-min(s,n-1)-1,-1):
		re[s-j][j] = ind
		ind += 1

for re_ in re:
	out = ''
	for re__ in re_:
		out += (str(re__) + ' ')
	print(out.strip())