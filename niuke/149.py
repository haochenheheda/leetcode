x = raw_input().strip()
max_num = 0
for i in range(len(x)):
	tmp = 1
	ind = i
	while x[(ind+1)%len(x)] != x[ind]:
		tmp += 1
		ind = (ind + 1)%len(x)
		if tmp == len(x):
			break
	if tmp > max_num:
		max_num = tmp
print(max_num)

