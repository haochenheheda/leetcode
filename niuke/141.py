import sys
n = int(raw_input().strip())
lst = list(map(int,raw_input().strip().split()))
lst.sort()
max_ = -sys.maxint
min_ = sys.maxint
for i in range(n/2):
	max_ = max(max_,lst[i] + lst[n-i-1])
	min_ = min(min_,lst[i] + lst[n-i-1])
print(max_-min_)