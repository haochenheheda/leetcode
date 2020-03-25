import sys
# m,n,x,y,k = [int(i.strip()) for i in sys.stdin.readlines()]
m,n,x_,y_,k_ = [int(i.strip()) for i in open('input.txt','r').readlines()]

# res = 0
# def move(m,n,x,y,k):
# 	global res
# 	if k == 0:
# 		return
# 	for x_,y_ in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
# 		if x_ < 0 or x_ >= m or y_ < 0 or y_ >= n:
# 			res += 1
# 		else:
# 			move(m,n,x_,y_,k-1)

# move(m,n,x,y,k)
# print(res)

dp = [[[0] * (n + 2) for _ in range(m+2)] for _ in range(k_+1)]
for k in range(1,k_+1):
	for x in range(1,m+1):
		for y in range(1,n+1):
			dp[k][x][y] = dp[k-1][x-1][y] + dp[k-1][x+1][y] + dp[k-1][x][y-1] + dp[k-1][x][y+1] + int(x==1) + int(x==m) + int(y==1) + int(y==n)
print(dp[k_][x_+1][y_+1])			