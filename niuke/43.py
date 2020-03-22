g = [1,2,3]
s = [1,1]
g.sort()
g.reverse()
s.sort()
s.reverse()
ind_g = 0
num_ = 0
flag = False
for s_ in s:
	while True:
		if ind_g == len(g):
			flag = True
			break
		if g[ind_g] > s_:
			ind_g += 1
		else:
			num_ += 1
			ind_g += 1
			break
	if flag == True:
		break
print(num_)


