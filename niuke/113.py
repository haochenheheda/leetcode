import sys
# lines = sys.stdin.readlines()
lines = open('input.txt','r').readlines()
x = int(lines[0].strip())
lst = [int(i.strip()) for i in lines[1:]]
s = set(lst)
l = 0
r = 0
map_ = {}
s_ = set()
while True:
	s_.add(lst[r])
	map_[lst[r]] = map_.setdefault(lst[r],0) + 1
	if s_ == s:
		break
	r += 1
while True:
	if map_[lst[l]] > 1:
		map_[lst[l]] -= 1
		l += 1
	else:
		break
out_min = r-l
out_lst = [[l+1,r+1]]

for r_ in range(r+1,len(lst)):
	map_[lst[r_]] += 1
	while True:
		if map_[lst[l]] > 1:
			map_[lst[l]] -= 1
			l += 1
		else:
			break
	if r_-l == out_min:
		out_lst.append([l+1,r_+1])
	elif r_-l < out_min:
		out_min = r_-l
		out_lst = [[l+1,r_+1]]

p = ''
for l in out_lst:
	l = str(l).strip().split()
	l = l[0] + l[1]
	p += (l + ' ')

print(str(out_min+1)+ ' ' + str(len(out_lst)))
print(p[:-1])