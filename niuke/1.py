while True:
	try:
		n,m = raw_input().split()
		n = int(n)
		m = int(m)
		di = []
		pi = []
		map_ = {}
		for i in range(n):
			while True:
				tmp = raw_input()
				if tmp != '':
					break
			tmp_di,tmp_pi = tmp.split()
			tmp_di = int(tmp_di)
			tmp_pi = int(tmp_pi)
			di.append(tmp_di)
			pi.append(tmp_pi)
			map_[tmp_di] = tmp_pi

		di.sort()
		ai = [int(i) for i in raw_input().split()]
		ai_sorted = [i for i in ai]
		ai_sorted.sort()


n_ind = 0
tmp_v = 0
value_map = {}
for one_ai in ai_sorted:
	while True:
		if n_ind >= len(di) or one_ai < di[n_ind]:
			value_map[one_ai] = tmp_v
			break
		if one_ai >= di[n_ind]:
			if tmp_v < map_[di[n_ind]]:
				tmp_v = map_[di[n_ind]]
			n_ind += 1



for one_ai in ai:
	print(value_map[one_ai])
	except:
		break

