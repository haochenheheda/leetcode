x = '1925'
len_ = len(x)
dp = [0] * (len_ + 1)
dp[0] = 1
dp[1] = 1
for i in range(2,len_ + 1):
	if int(x[i-2:i]) <= 26:
		dp[i] = dp[i-1] + dp[i-2]
	else:
		dp[i] = dp[i-1]
print(dp[-1])