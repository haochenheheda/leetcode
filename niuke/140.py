import sys
sys.setrecursionlimit(100000)
n = int(raw_input().strip())

lst = list(map(int,raw_input().strip().split()))

def dfs(left,tmp,lst,re):
	# print(left)
	# if left == 1:
	# 	print(lst,tmp,re)
	if left == 1:
		return re
	if left/2 + 1 < max(lst):
		return ''
	for l in range(len(lst)):
		if l != tmp and lst[l] > 0:
			lst[l] = lst[l] - 1
			x = dfs(left-1,l,lst,re + [l+1])
			if x != '':
				return x
			lst[l] = lst[l] + 1
	return '-'

if n == 1 and lst[0] > 1:
	print('-')
else:
	left = sum(lst)
	tmp = None
	re = []
	re = dfs(left,tmp,lst,re)
	if re == '-':
		print(re)
	else:
		print(' '.join(map(str,re)))


