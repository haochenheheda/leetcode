import sys
# lines = sys.stdin.readlines()
lines = open('input.txt','r').readlines()
n = int(lines[0].strip())
lst = [int(i.strip()) for i in lines[1:]]
dp = [[0] * len(lst) for _ in range(len(lst))]
for i in range(len(lst)):
	dp[i][i] = lst[i]
for r in range(len(lst)):
	for l in range(r-1,-1,-1):
		dp[l][r] = max(lst[l] - dp[l+1][r],lst[r] - dp[l][r-1])
for r in range(len(lst)):
	for l in range(len(lst)-1,r,-1):
		dp[l][r] = max(lst[l] - dp[(l+1)%len(lst)][r],lst[r] - dp[l][(r-1)%len(lst)])
max_ = dp[0][len(lst)-1]
for l in range(len(lst)-1):
	r = (l + len(lst) - 1)%n
	max_ = max(max_,dp[l][r])

print(max(max_,-max_))

