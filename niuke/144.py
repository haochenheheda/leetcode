x = int(raw_input().strip())
print(x/5 + int(x%5>0))
# if x <= 5:
# 	print(1)
# else:
# 	dp = [0] * (x + 1)
# 	for i in range(6):
# 		dp[i] = 1
# 	for i in range(6,x+1):
# 		dp[i] = min(dp[i-1],dp[i-2],dp[i-3],dp[i-4],dp[i-5]) + 1
# 	print(dp[x])