import bisect
# x = 'xadbbcax'
# x = 'aaa'
x = '123321123321123321'
# x = 'aaaaabbbbaaacccddefdasfdsafdsafdshfkdslfhdlsakhfieosoafhiwolasfhioelsahfioelshfoialewjafdhisoafhiehaflsdhifhealsdhfieohalfdhsaiofhealskhdfiehighalfdjasioehiohfeioafhsdfaaaaabbbbaaacccddefdasfdsafdsafdshfkdslfhdlsakhfieosoafhiwolasfhioelsahfioelshfoialewjafdhisoafhiehaflsdhifhealsdhfieohalfdhsaiofhealskhdfiehighalfdjasioehiohfeioafhsdfaaaaabbbbaaacccddefdasfdsafdsafdshfkdslfhdlsakhfieosoafhiwolasfhioelsahfioelshfoialewjafdhisoafhiehaflsdhifhealsdhfieohalfdhsaiofhealskhdfiehighalfdjasioehiohfeioafhsdfaaaaabbbbaaacccddefdasfdsafdsafdshfkdslfhdlsakhfieosoafhiwolasfhioelsahfioelshfoialewjafdhisoafhiehaflsdhifhealsdhfieohalfdhsaiofhealskhdfiehighalfdjasioehiohfeioafhsdfaaaaabbbbaaacccddefdasfdsafdsafdshfkdslfhdlsakhfieosoafhiwolasfhioelsahfioelshfoialewjafdhisoafhiehaflsdhifhealsdhfieohalfdhsaiofhealskhdfiehighalfdjasioehiohfeioafhsdfaaaaabbbbaaacccddefdasfdsafdsafdshfkdslfhdlsakhfieosoafhiwolasfhioelsahfioelshfoialewjafdhisoafhiehaflsdhifhealsdhfieohalfdhsaiofhealskhdfiehighalfdjasioehiohfeioafhsdfaaaaabbbbaaacccddefdasfdsafdsafdshfkdslfhdlsakhfieosoafhiwolasfhioelsahfioelshfoialewjafdhisoafhiehaflsdhifhealsdhfieohalfdhsaiofhealskhdfiehighalfdjasioehiohfeioafhsdfaaaaabbbbaaacccddefdasfdsafdsafdshfkdslfhdlsakhfieosoafhiwolasfhioelsahfioelshfoialewjafdhisoafhiehaflsdhifhealsdhfieohalfdhsaiofhealskhdfiehighalfdjasioehiohfeioafhsdf'



n = len(x)
dp = [[0] * n for _ in range(n)]

for r in range(n):
	for l in range(r,-1,-1):
		if r == l:
			dp[l][r] = 1
		else:
			if x[l] == x[r]:
				dp[l][r] = dp[l+1][r-1] + 2
			else:
				dp[l][r] = max(dp[l+1][r],dp[l][r-1	])

print(dp[0][n-1])


# stack = {}
# max_key = 1
# stack[1] = [0]

# nn = len(x)
# for i in range(1,nn):
# 	drop_ind = max_key - (nn - i) * 2
# 	keys = stack.keys()
# 	keys.sort()
# 	keys = keys[bisect.bisect_left(keys,drop_ind):]
# 	for k in keys[::-1]:
# 		tmp_n = k + 2
# 		last_lst = stack[tmp_n - 2]
# 		last_start_ind = last_lst[0]
# 		for serach_ind in range(last_start_ind - 1,-1,-1):
# 			if x[serach_ind] == x[i]:
# 				if stack.has_key(tmp_n):
# 					if stack[tmp_n][0] < serach_ind:
# 						stack[tmp_n] = [serach_ind] + last_lst + [i]
# 				else:
# 					stack[tmp_n] = [serach_ind] + last_lst + [i]
# 					if max_key < tmp_n:
# 						max_key = tmp_n
# 				break
# 	if x[i-1] == x[i]:
# 		stack[2] = [i-1,i]
# 		if max_key < 2:
# 			max_key = 2
# 	stack[1] = [i]

# print(max_key)