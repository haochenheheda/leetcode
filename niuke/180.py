n = int(raw_input().strip())
dp = [[0] * (121) for _ in range(n+1)]
for i in range(1,n+1):
	p,a,q,b = map(int,raw_input().strip().split())
	for j in range(1,121):
		tmp = dp[i-1][j]
		if j >= p:
			tmp = max(tmp,dp[i-1][j-p] + a)
		if j >= q:
			tmp = max(tmp,dp[i-1][j-q] + b)
		dp[i][j] = tmp
print(dp[n][-1])