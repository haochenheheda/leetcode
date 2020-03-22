x = [2,3,3,5]
limit = 6
x.sort()
l = 0
r = len(x)-1
num_ = 0
while True:
	if x[l] + x[r] <= limit:
		num_ += 1
		l += 1
		r -= 1
	else:
		num_ += 1
		r -= 1
	if l > r:
		break
print(num_)

