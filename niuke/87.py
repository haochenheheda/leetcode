import sys
# lines = sys.stdin.readlines()
while True:
	try:
		n,m = map(int,raw_input().strip().split())
		map_ = {}
		c_set = [0] * (n+1)
		remain = set(range(1,n+1))

		for _ in range(m):
			a,b = map(int,raw_input().strip().split())
			if not map_.has_key(a):
				map_[a] = [b]
			else:
				map_[a].append(b)
			c_set[b] += 1

		re = ''
		while remain:
			for i in remain:
				if c_set[i] == 0:
					re += (str(i) + ' ')
					if map_.has_key(i):
						sub = map_[i]
						for sub_ in sub:
							c_set[sub_] -= 1
					break
			remain.remove(i)
		print(re[:-1])
	except:
		break


