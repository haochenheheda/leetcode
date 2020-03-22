import sys
l,r = [int(i) for i in sys.stdin.readline().strip().split()]
group = (r-1)/3 - (l-1)/3 - 1
if l%3==1:
	h = 2
if l%3==2:
	h = 2
if l%3==0:
	h = 1
if r%3==1:
	t = 0
if r%3==2:
	t = 1
if r%3==0:
	t = 2
print(group * 2 + h + t)