# import bisect
# x = int(raw_input().strip())

# dp = [0] * (x+1)
# lst = []
# for i in range(1,x):
# 	if i ** 3 <= x:
# 		lst.append(i ** 3)
# 	else:
# 		break

# for i in range(1,x+1):
# 	dp[i] = min([dp[i-j] for j in lst[:bisect.bisect_right(lst,i)]])+1
# print(dp[-1])


x = int(raw_input().strip())
def pp(x):
	lst = set()
	i = 1
	while i ** 3 <= x:
		lst.add(i ** 3)
		i+=1

	t = set()
	t.add(x)
	count = 0
	flag = False
	while t:
		n = set()
		count += 1
		for t_ in t:
			if t_ in lst:
				print(count)
				flag = True
				break
			for l_ in lst:
				if t_ - l_ > 0:
					n.add(t_ - l_)
			if flag == True:
				break
		t = n
		if flag == True:
			break
pp(x)