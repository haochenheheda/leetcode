n,k,w = map(int,raw_input().strip().split())

# if n >= k + w:
# 	print('1.00000')
# else:
# 	dp = [0] * (k + w)
# 	for i in range(k,n+1):
# 		dp[i] = 1
# 	for i in range(k-1,-1,-1):

# 		dp[i] = sum(dp[i+1:i+w+1])/float(w)
# 	str_ = str(round(dp[0],5))
# 	print(str_ + '0' * (7 - len(str_)))

if n >= k + w:
	print('1.00000')
else:
	dp = [0] * (k + w)
	for i in range(k,n+1):
		dp[i] = 1
	to_remove = 0
	sum_ = sum(dp[k+1:k+w+1])/float(w)
	for i in range(k-1,-1,-1):
		to_add = dp[i+1]/float(w)
		sum_ = sum_ + to_add - to_remove
		dp[i] = sum_
		to_remove = dp[i+w]/float(w)

	str_ = str(round(dp[0],5))
	print(str_ + '0' * (7 - len(str_)))






