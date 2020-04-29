lst = map(int,raw_input().strip().split(','))
tmp = 0
width = 1
flag = True
while tmp + width < len(lst) - 1:
	for i in range(width):
		if lst[i+tmp] < lst[2*i+tmp+width] or lst[i+tmp] > lst[2*i+1+tmp+width]:
			flag = False
			break
	tmp += width
	width *= 2

	if flag == False:
		break
if flag:
	print('True')
else:
	print('False')