n,x = map(int,raw_input().strip().split())
lst = list(map(int,raw_input().strip().split()))
num = 0
if not x in lst:
	lst.append(x)
	num += 1
	n += 1
lst.sort()
r_add_num = 0
l_add_num = 0
while True:
	if lst[(n + r_add_num + l_add_num -1)/2 - l_add_num] == x:
		break
	elif lst[(n + r_add_num + l_add_num -1)/2 - l_add_num] < x:
		r_add_num += 1
	else:
		l_add_num += 1
print(r_add_num + l_add_num + num)
