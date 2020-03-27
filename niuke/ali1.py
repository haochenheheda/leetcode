lst = ['abcdef','aaa','zzz','abc']
map_ = {}
for l in lst:
	b = l[0]
	e = l[-1]
	if map_.has_key((b,e)):
		if len(l) > map_[(b,e)]:
			map_[(b,e)] = len(l)
	else:
		map_[(b,e)] = len(l)

	for k in map_.keys():
		if b >= k[1]:
			if map_.has_key((k[0],e)):
				if map_[(k[0],e)] < len(l) + map_[k]:
					map_[(k[0],e)] = len(l) + map_[k]
			else:
				map_[(k[0],e)] = len(l) + map_[k]

		if e <= k[0]:
			if map_.has_key((b,k[1])):
				if map_[(b,k[1])] < len(l) + map_[k]:
					map_[(b,k[1])] = len(l) + map_[k]
			else:
				map_[(b,k[1])] = len(l) + map_[k]
print(max(map_.values()))