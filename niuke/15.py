n=2
m=2
k=2



lst = [0] * (m+n)

def f(n,m,k):
	for i in range(m,m+n+1):
		if i == m:
			num_ = 0
			num = 1
		else:
			num_ = num
			num = num * i / (i-m)
		if num >= k:
			lst[-i] = 1
			return k-num_

	return -1

for m_ in range(m,0,-1):
	k = f(n,m_,k)
	if k == -1:
		break


if k == -1:
	print(-1)
else:
	str_ = ''
	for a in lst:
		if a == 0:
			str_ += 'a'
		else:
			str_ += 'z'
	print(str_)



