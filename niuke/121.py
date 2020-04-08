lst = raw_input().strip()
num_map = {}
for l in lst:
	num_map[l] = num_map.setdefault(l,0) + 1

tmp_len = 0
tmp_map = {}
re = []
for l in lst:
	tmp_len += 1
	tmp_map[l] = tmp_map.setdefault(l,0) + 1
	flag = True
	for k,v in tmp_map.items():
		if v < num_map[k]:
			flag = False
			break
	if flag:
		re.append(tmp_len)
		tmp_len = 0
		tmp_map = {}
print(' '.join(map(str,re)))

