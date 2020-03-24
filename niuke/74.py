lst = raw_input().strip()
len_ = len(lst)
dp = [[-1] * (len_+1) for _ in range(len_)]
for i in range(len_):
	dp[i][i] = 0
	dp[i][i+1] = 1

max_ = 1
l = 0
r = 1
for i in range(2,len_+1):
	for j in range(i-1):
		if lst[i-1] != lst[j]:
			dp[j][i] = -1
		if lst[i-1] == lst[j]:
			if dp[j+1][i-1] != -1:
				dp[j][i] = dp[j+1][i-1] + 2
			else:
				dp[j][i] = -1
		if dp[j][i] > max_:
			max_ = dp[j][i]
			l = j
			r = i
print(lst[l:r])