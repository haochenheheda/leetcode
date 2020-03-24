n = int(raw_input().strip())
lst = raw_input().strip()
k = (n - 1)/3
ind = 0
re = ''
for k_ in range(k):
	str_ = ''
	str_ += ' ' * k_
	str_ += lst[ind]
	ind += 1
	str_ += ' ' * (2 * k - 2 * k_ - 1)
	str_ += lst[ind]
	ind += 1
	str_ += '\n'
	re += str_
for i in range(ind,len(lst)):
	str_ = ' ' * k + lst[i] + '\n'
	re += str_
print(re)