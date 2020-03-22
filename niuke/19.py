n = 100

# def f(n):
# 	if n == 1:
# 		return 1
# 	if n == 0:
# 		return 1
# 	lst = []
# 	tmp = 1
# 	for i in range(20):
# 		if tmp <= n:
# 			lst.append(tmp)
# 			tmp *=2
# 		else:
# 			break

# 	re = 0
# 	for i in lst:
# 		re += f(n - i)
# 	return re 

# print(f(n))

map_ = {}
for n_ in range(1000):
	if n_ < 2:
		map_[n_] = 1
		continue
	lst = []
	tmp = 1
	while True:
		if tmp <= n_:
			lst.append(tmp)
			tmp *=2
		else:
			break
	re = 0
	for i in lst:
		re += map_[n_ - i]
	map_[n_] = re
print(map_[n])
