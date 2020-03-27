import sys
# lines = sys.stdin.readlines()
lines = open('input.txt','r').readlines()
map_ = {}
for i in range(len(lines)-1):
	n,m = lines[i].strip().split('#')
	n = int(n)
	num = int(m,n)
	if map_.has_key(num):
		map_[num] = -1
	else:
		map_[num] = [i,lines[i]]

re = []
for _,v in map_.items():
	if v != -1:
		re.append(v)
if len(re) == 0:
	print('None')
else:
	re.sort()
	for i in re:
		print(i[1].strip())
