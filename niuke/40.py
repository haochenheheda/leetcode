p = [3,6,7,11]
h = 8
start_k = sum(p)/h + 1

while True:
	h_sum = 0
	for p_ in p:
		h_ = p_/start_k
		if p_%start_k:
			h_ += 1
		h_sum += h_
		if h_sum > h:
			break
	if h_sum <= h:
		break
	start_k += 1
print(start_k)
