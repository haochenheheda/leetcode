import sys
n,x1,y1,x2,y2 = map(int,raw_input().strip().split())
lst = []
for _ in range(n):
	x,y = map(int,raw_input().strip().split())
	d1 = (x1 - x) ** 2 + (y1 - y) ** 2
	d2 = (x2 - x) ** 2 + (y2 - y) ** 2
	lst.append([d1,d2])

min_ = sys.maxint
lst = sorted(lst,key = lambda l:l[0])
for i in range(len(lst)):
	max2 = 0
	for j in range(i+1,len(lst)):
		max2 = max(max2,lst[j][1])
	max12 = lst[i][0] + max2
	min_ = min(min_,max12)
print(min_)