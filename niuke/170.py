s1,s2 = raw_input().strip().split(',')
dp = [[0] * (len(s2)+1) for _ in range(1+len(s1))]
max_ = 0
for i in range(1,1+len(s1)):
	for j in range(1,1+len(s2)):
		if s1[i-1] != s2[j-1]:
			dp[i][j] = 0
		else:
			dp[i][j] = 1 + dp[i-1][j-1]
			max_ = max(max_,dp[i][j])
print(max_)
