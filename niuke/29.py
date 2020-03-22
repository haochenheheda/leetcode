x = 'aabcb'
len_ = len(x)
num = 0
root = []
for i in range(len_):
	root.append([i])
	num += 1
	if i < len_ - 1:
		if x[i+1] == x[i]:
			root.append([i,i+1])
			num += 1
for root_ in root:
	l = root_[0]
	r = root_[-1]
	while True:
		if l > 0 and r < len_ - 1 and x[l-1] == x[r+1]:
			l -= 1
			r += 1
			num += 1
		else:
			break
print(num)

