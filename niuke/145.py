n = int(raw_input().strip())
for _ in range(n):
	n,m = map(int,raw_input().strip().split())
	if n == 1 and m == 2:
		print(1)
	elif n == 1 and m != 1:
		print(m - 2)
	elif n != 1 and m == 1:
		print(n - 2)
	else:

		print((m-2) * (n-2))