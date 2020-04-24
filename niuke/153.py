import sys
n = int(raw_input().strip())
s = set()
lst = []
min_ = sys.maxint
for _ in range(n):
	a,b = map(int,raw_input().strip().split())
	lst.append([a,b])
	min_ = min(min_,max(a,b))
s = [2]
z = [False] * (min_ + 1)
for i in range(3,min_+1,2):
	if not z[i]:
		for j in range(i+i,min_+1,i):
			z[j] = True
	if not z[i]:
		s.append(i)

for a,b in lst:
	if len(s) == 0:
		break
	for i in range(len(s)-1,-1,-1):
		if a%s[i] == 0 or b%s[i] == 0:
			break
		else:
			s.pop(-1)
if len(s) == 0:
	print(-1)
else:
	print(s[-1])


