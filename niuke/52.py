t = 7
init = 0
sum_ = 0


while True:
	init += 1
	sum_+= init
	if t <= sum_:
		if (t%2 == 0 and sum_%2 == 0) or (t%2 == 1 and sum_%2 == 1):
			print(init)
			break


# max_ = 2*(t-1) + 1
# map_ = {}
# map_[0] = 0
# start = [0]
# for k in range(1,max_):
# 	start_ = []
# 	for s in start:
# 		map_[s + k] = k
# 		start_.append(s+k)

# 		map_[s - k] = k
# 		start_ += [s-k]
# 	start = start_

# 	if map_.has_key(t):
# 		break
# if map_.has_key(t) and map_[t] < max_:
# 	print(map_[t])
# else:
# 	print(max_)
