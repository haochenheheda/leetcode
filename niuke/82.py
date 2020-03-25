x = int(raw_input().strip())
if x == 1:
	print(1)
elif x == 2:
	print(2)
else:
	dp = [0] * x
	dp[0] = 1
	dp[1] = 2
	for i in range(2,x):
		dp[i] = dp[i-1] + dp[i-2]
	print(dp[-1])