import sys
lines = sys.stdin.readlines()
# lines = open('input.txt','r').readlines()
m,n = map(int,lines[0].strip().split())

matrix = [list(map(int,i.strip().split())) for i in lines[1:-1]]
x = int(lines[-1].strip())

m = 2
n = 3
matrix = [[2,3,5],[3,4,7]]
x = 4


flag = False
j = m-1
i = 0
while True:
	if j < 0 or i > n-1:
		break
	if matrix[j][i] == x:
		flag = True
		break
	elif matrix[j][i] < x:
		i = i+1
	else:
		j = j-1
if flag:
	print('true')
else:
	print('false')



# flag = False
# for m_ in matrix:
# 	if x in m_:
# 		flag = True
# 		break
# if flag:
# 	print('true')
# else:
# 	print('false')




# flag = False
# tmp = n
# for i in range(m):
# 	if matrix[i][-1] < x:
# 		continue
# 	else:
# 		lst = matrix[i]
# 		l = 0
# 		r = tmp - 1
# 		while True:
# 			if l == r:
# 				if lst[l] == x:
# 					flag = True
# 				else:
# 					tmp = r
# 				break
# 			mid = (l + r)/2
# 			if lst[mid] == x:
# 				flag = True
# 				break
# 			elif lst[mid] > x:
# 				r = mid
# 			else:
# 				l = mid + 1


# 		if flag == True:
# 			break

# if flag:
# 	print('true')
# else:
# 	print('false') 






# flag = False
# for s in range(m+n-2):
# 	for j in range(s-min(m-1,s),min(n-1,s)+1):
# 		if matrix[s-j][j] == x:
# 			flag = True
# 			break
# 	if flag == True:
# 		break
# if flag:
# 	print('true')
# else:
# 	print('false') 





