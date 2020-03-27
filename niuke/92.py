lst = list(map(int,raw_input().strip().split()))
if len(lst) == 1:
	print(lst[0])
else:
	flag = False
	for i in range(1,len(lst)):
		if lst[i] < lst[i-1]:
			print(lst[i])
			flag = True
			break
	if flag == False:
		print(lst[0])