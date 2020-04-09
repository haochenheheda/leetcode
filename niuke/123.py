x,y = map(int,raw_input().strip().split())
dp = [[0] * (x+1) for _ in range(y+1)]
for i in range(x+1):
	dp[0][i] = 1
for i in range(y+1):
	dp[i][0] = 1
for x_ in range(1,x+1):
	for y_ in range(1,y+1):
		dp[y_][x_] = dp[y_-1][x_] + dp[y_][x_-1]
print(dp[y][x])