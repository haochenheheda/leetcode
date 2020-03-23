x,y = map(int,raw_input().strip().split())
x += 1
y += 1
dp = [[0] * x for _ in range(y)]
for i in range(x):
	dp[0][i] = 1
for i in range(y):
	dp[i][0] = 1

for i in range(1,x):
	for j in range(1,y):
		dp[j][i] = dp[j-1][i] + dp[j][i-1]

print(dp[-1][-1])
