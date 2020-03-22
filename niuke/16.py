n = 3
d = [4,1,2]

sum_ = sum(d)
sum_1 = 0
for i in range(n):
	sum_1 += d[i]
	if sum_1 >= sum_/2:
		pl = i+1
		pr = i+1
		sum_l = sum_1
		sum_r = sum_ - sum_l
		break
while True:
	if sum_l == sum_r:
		print(sum_l)
		break
	elif sum_l < sum_r:
		pr += 1
		sum_r -= d[pr-1]
	else:
		pl -= 1
		sum_l -= d[pl]
	if pl == 0 or pr == n + 1:
		print(0)
		break




