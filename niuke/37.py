lst = list(map(int,raw_input().strip().split(',')))
len_ = len(lst)

dp = [0] * len_
dp[0] = lst[0]
dp[1] = lst[1]
for n in range(2,len_):
	dp[n] = min(dp[n-1],dp[n-2]) + lst[n]
print(min(dp[-1],dp[-2]))