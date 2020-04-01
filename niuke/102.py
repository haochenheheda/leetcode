import sys
# lines = sys.stdin.readlines()
lines = open('input.txt','r').readlines()
n,m = map(int,lines[0].strip().split())
lst = list(map(int,lines[1].strip().split()))



dp = [[sys.maxint] * (m+1) for _ in range(n+1)]
sum_ = []
for i in range(n):
	sum_.append(sum(lst[:i+1]))

for i in range(1,n+1):
	dp[i][1] = sum_[i-1]


for j in range(2,m+1):
	for i in range(j,n+1):
		for k in range(1,i-j+2):
			dp[i][j] = min(dp[i][j],max(dp[i-k][j-1],sum_[i-1] - sum_[i-k-1]))
print(dp[n][m])
# for i in range(1,n+1):
# 	print(dp[i][2])




# l = max(lst)
# r = sum(lst)

# ans = r
# while l<=r:
# 	mid = (l+r)/2
# 	m_count = 1
# 	tmp = 0
# 	for i in lst:
# 		tmp += i
# 		if tmp > mid:
# 			m_count += 1
# 			tmp = i
# 	if m_count <= m:
# 		ans = min(ans,mid)
# 		r = mid-1
# 	else:
# 		l = mid + 1
# print(ans)
	
