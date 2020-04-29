import sys  
sys.setrecursionlimit(1000000)
m,n,k = map(int,raw_input().strip().split())
num = 1
tmp = [0,0]
searched = [[False] * n for _ in range(m)]
searched[0][0] = True

def dt(x,y):
	num = 0
	while x > 0:
		num += x%10
		x /= 10
	while y > 0:
		num += y%10
		y /= 10	
	return num
def dfs(tmp,searched):
	global num
	y,x = tmp
	if y-1 >= 0 and searched[y-1][x] == False and dt(x,y-1) <= k:
		num += 1
		searched[y-1][x] = True
		dfs([y,x],searched)
	if x-1 >= 0 and searched[y][x-1] == False and dt(x-1,y) <= k:
		num += 1
		searched[y][x-1] = True
		dfs([y,x-1],searched)
	if x+1 < n and searched[y][x+1] == False and dt(x+1,y) <= k:
		num += 1
		searched[y][x+1] = True
		dfs([y,x+1],searched)
	if y+1 < m and searched[y+1][x] == False and dt(x,y+1) <= k:
		num += 1
		searched[y+1][x] = True
		dfs([y+1,x],searched)

dfs([0,0],searched)
print(num)



