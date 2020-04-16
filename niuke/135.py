x1,x2 = raw_input().strip().split()
# if len(x1) < len(x2):
# 	x1,x2 = x2,x1
x1 = x1[::-1]
x2 = x2[::-1]
ind = 0
tmp = 0
re = ''
while True:
	for ind1 in range(ind+1):
		ind2 = ind - ind1
		if ind1 >= len(x1):
			break
		if ind2 >= len(x2):
			continue
		num1 = int(x1[ind1])
		num2 = int(x2[ind2])
		tmp += num1 * num2
	re += str(tmp%10)
	tmp = tmp/10
	if ind == len(x1) + len(x2) - 2:
		break
	ind += 1
if tmp != 0:
	re += str(tmp)[::-1]
print(re[::-1])
