n,x = map(int,raw_input().strip().split())
lst = map(int,raw_input().strip().split())

dp = [[0] * (x+1) for _ in range(n+1)]
for i in range(x+1):
	dp[0][i] = 1000000
for i in range(1,n+1):
	for j in range(1,x+1):
		if lst[i-1] >= j:
			dp[i][j] = min(lst[i-1],dp[i-1][j])
		else:
			dp[i][j] = min(dp[i-1][j],lst[i-1] + dp[i-1][j-lst[i-1]])
print(dp[i][j])