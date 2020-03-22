a = int(input())
if a in [0,1,2,4]:
    print -1
else:
    count = a // 7
    res = a % 7
    if res in [1,3,5]:
        count += 1
    if res in [2,4,6]:
        count += 2
    print count

# x = int(raw_input().strip())
# dp = [0] * max((x + 1),8)
# dp[0] = 0
# dp[1] = -1
# dp[2] = -1
# dp[3] = 1
# dp[4] = -1
# dp[5] = 1
# dp[6] = 2
# dp[7] = 1

# if x<= 7:
# 	print(dp[x])
# else:
# 	for x_ in range(8,x+1):
# 		tmp3 = dp[x_-3]
# 		tmp5 = dp[x_-5]
# 		tmp7 = dp[x_-7]
# 		used = []
# 		if tmp3 != -1:
# 			used += [tmp3]
# 		if tmp5 != -1:
# 			used += [tmp5]
# 		if tmp7 != -1:
# 			used += [tmp7]

# 		if len(used) == 0:
# 			dp[x_] = -1
# 		else:
# 			dp[x_] = min(used) + 1
# 	print(dp[x])