import sys
lines = open('input.txt','r').readlines()
# lines = sys.stdin.readlines()

k,n = list(map(int,lines[0].strip().split()))
matrix = [list(map(int,line.strip().split())) for line in lines[1:]]

stack = [matrix[0][0]]
ind = [(0,0)]
for i in range(1,k+1):
	re = min(stack)
	ind_ = stack.index(re)
	y,x = ind[ind_]
	stack.pop(ind_)
	ind.pop(ind_)
	if y < n-1:
		stack.append(matrix[y+1][x]) 
		ind.append((y+1,x))
	if x < n-1:
		stack.append(matrix[y][x+1]) 
		ind.append((y,x+1))
print(re)
