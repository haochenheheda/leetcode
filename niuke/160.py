s1 = 'intrinsic'
s2 = 'intrusive'

# dp = [[0] * (len(s1)+1) for _ in range(len(s2)+1)]
# for i in range(1,len(s2)+1):
# 	for j in range(1,len(s1)+1):
# 		if s2[i-1] == s1[j-1]:
# 			dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]+1)
# 		else:
# 			dp[i][j] = max(dp[i-1][j],dp[i][j-1])
# for i in range(len(s2)+1):
# 	print(dp[i])
# print(max(len(s1),len(s2)) - dp[-1][-1])

def count(s1,s2):
	if s1 == '':
		return len(s2)
	if s2 == '':
		return len(s1)
	if s1[0] == s2[0]:
		return count(s1[1:],s2[1:])
	else:
		return min(count(s1[1:],s2),count(s1,s2[1:]),count(s1[1:],s2[1:]))+1
print(count(s1,s2))