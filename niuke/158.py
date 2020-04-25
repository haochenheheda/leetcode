x,y = map(int,raw_input().strip().split(','))
if x == y:
	print(0)
else:
	dp = [-1] * 201
	dp[x+100] = 0
	def iter(x_lst,num):
		if dp[y+100] != -1:
			return dp[y+100]
		n_lst = []
		for x in x_lst:
			if x < 100 and dp[x+100+1] == -1:
				n_lst.append(x+1)
				dp[x+100+1] = num + 1
			if x > -100 and dp[x+100-1] == -1:
				n_lst.append(x-1)
				dp[x+100-1] = num + 1
			if x * 2 <= 100 and x * 2 >= -100 and x != 0 and dp[x*2+100] == -1:
				n_lst.append(x*2)
				dp[x*2+100] = num + 1
		iter(n_lst,num+1)

	iter([x],0)
	print(dp[y+100])

