n,k = map(int,raw_input().strip().split())
lst = map(int,raw_input().strip().split())

# num = 0
# for i in range(n):
# 	print(lst[i] * 2 + 1 + min(0,i - lst[i]) + min(0,n-i-1-lst[i]))
# 	if lst[i] * 2 + 1 + min(0,i - lst[i]) + min(0,n-i-1-lst[i]) >= k:
# 		num += 1
# print(num)

dp = [0] * (n + 1)
for i in range(n):
	l = max(i-lst[i],0)
	r = min(i+lst[i],n-1)
	dp[l] += 1
	dp[r+1] -= 1
sum_ = 0
re = 0
for i in range(n):
	sum_ += dp[i]
	if sum_ >= k:
		re += 1
print(re)