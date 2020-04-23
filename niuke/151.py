while True:
	try:
		n,k = map(int,raw_input().strip().split())
		str_ = raw_input().strip()
		map_ = {}
		for s in str_:
			map_[s] = map_.setdefault(s,0) + 1
		t = map_.values()
		t.sort()
		t = t[::-1]
		score = 0
		ind = 0
		while k > 0:
			tmp = min(t[ind],k)
			score += tmp ** 2
			k -= tmp
			ind += 1
		print(score)
	except:
		break