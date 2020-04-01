import sys
# lines = sys.stdin.readlines()
lines = open('input.txt','r').readlines()
n = int(lines[0].strip())
lst = list(map(int,lines[1].strip().split()))
x = int(lines[2].strip())



dp = 1
for l in lst:
	dp |= (dp << l)
print(dp >> x & 1)



# dp = [0] * (x+1)
# dp[0] = 1
# for i in range(n):
# 	for j in range(x,n-1,-1):
# 		dp[j] = max(dp[j],dp[j-lst[i]])
# print(dp[-1]) 


# re = [0]

# flag = False
# for ind in range(n):
# 	tmp = []
# 	for re_ in re:
# 		if re_ + lst[ind] == x:
# 			flag = True
# 			break
# 		elif re_ + lst[ind] < x:
# 			tmp.append(re_ + lst[ind])

# 	if flag == True:
# 		break
# 	re += tmp

# if flag == True:
# 	print(1)
# else:
# 	print(0)

			
