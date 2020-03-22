n = 43487
k = 0

num = 0
if k == 0:
	print(n ** 2)
else:
	for y in range(k + 1,n + 1):
		num += (n/y)*(y-k) + max(0,(n%y)-k+1)
	print(num)