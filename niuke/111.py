n = int(raw_input().strip())
dp = [0] * (n+1)
dp[0] = 1
for i in range(1,n+1):
	if i < 3:
		dp[i] = dp[i-1]
	else:
		dp[i] = dp[i-1] + dp[i-3]

print(dp[n])