a,b = raw_input().strip().split()
flag = False
map_1 = {}
for a_ in a:
	if map_1.has_key(a_):
		map_1[a_] += 1
	else:
		map_1[a_] = 1
for b_ in b:
	if map_1.has_key(b_):
		map_1[b_] -= 1
		if map_1[b_] == 0:
			map_1.pop(b_)
	if map_1 == {}:
		print('true')
		flag = True
		break

if flag == False:
	print('false')

