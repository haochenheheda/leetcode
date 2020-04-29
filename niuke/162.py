s = raw_input().strip()
l = 0
r = 0
re = 0
map_ = {}
while r < len(s):
	if map_.setdefault(s[r],0) == 0:
		map_[s[r]] += 1
	elif map_.setdefault(s[r],0) == 1:
		re = max(re,r-l)
		while s[l] != s[r]:
			map_[s[l]] -= 1
			l += 1
		l += 1
	r += 1
re = max(re,r-l)
print(re)