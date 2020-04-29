lst = map(int,raw_input().strip().split())
flag = True
num = 1
for i in range(1,len(lst)):
	if lst[i-1] <= lst[i]:
		continue
	else:
		flag = False
		break
if flag == True:
	print(1)
else:
	flag = True
	if i == 1 or lst[i-2] <= lst[i]:
		lst[i-1] = lst[i]
		for j in range(i,len(lst)):
			if lst[i-1] <= lst[i]:
				continue
			else:
				flag = False
				break
	else:
		lst[i] = lst[i-1]
		for j in range(i,len(lst)):
			if lst[i-1] <= lst[i]:
				continue
			else:
				flag = False
				break		
	if flag:
		print(1)
	else:
		print(0)

