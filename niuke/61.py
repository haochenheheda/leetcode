a,b = raw_input().strip().split(';')
len_a = len(a)
len_b = len(b)
if len_a != len_b:
	print('false')
else:
	flag = False
	for i in range(len_a):
		if a[:i] == b[-i:] and a[i:] == b[:-i]:
			flag = True
			break
	if flag:
		print('true')
	else:
		print('false')

