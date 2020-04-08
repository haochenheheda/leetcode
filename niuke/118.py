while True:
	try:
		lst = list(map(int,raw_input().strip().split(',')))
		left_num = 0
		flag = True
		for l in lst:
			for b in range(7,-1,-1):
				if l>>b&1 == 0:
					break
			if b == 7:
				if left_num == 0:
					continue
				else:
					flag = False
					break
			elif b < 6:
				if left_num == 0:
					left_num = 6 - b
				else:
					flag = False
					break
			elif b == 6:
				if left_num > 0:
					left_num -= 1
				else:
					flag = False
					break

		if left_num > 0:
			flag = False
		if flag:
			print('true')
		else:
			print('false')
	except:
		break
