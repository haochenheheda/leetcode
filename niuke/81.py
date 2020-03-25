t,n,w,v = raw_input().strip().split(',')
t = int(t)
n = int(n)
w = list(map(int,w.split()))
v = list(map(int,v.split()))
dp = [[0] * (t+1) for _ in range(n + 1)]
for t_ in range(1,t+1):
	for i in range(1,n+1):
		if w[i-1] > t_:
			dp[i][t_] = dp[i-1][t_]
		else:
			dp[i][t_] = max(dp[i-1][t_],dp[i-1][t_-w[i-1]]+v[i-1])
print(dp[-1][-1])
