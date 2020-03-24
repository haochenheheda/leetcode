lst = list(map(int,raw_input().strip()[1:-1].split(',')))
map_ = {}
max_ = 0
re = None
for l in lst:

	if not map_.has_key(l):
		map_[l] = 1
		if max_ == 0:
			max_ = 1
			re = l
	else:
		map_[l] += 1
		if map_[l] > max_:
			max_ = map_[l]
			re = l
print(re)