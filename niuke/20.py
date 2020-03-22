n = 7
m = 2
a = [1,2,3,-2,3,-10,3]

sum_a = []
num_z = 0
for i,a_ in enumerate(a):
	if i == 0:
		tmp = a_
		flag = a_ > 0
	else:
		if a_ > 0 and flag == 1:
			tmp += a_
		if a_ > 0 and flag == 0:
			flag = 1
			sum_a.append(tmp)
			num_z += 1
			tmp = a_
		if a_ < 0 and flag == 0:
			tmp += a_
		if a_ < 0 and flag == 1:
			flag = 0
			sum_a.append(tmp)
			tmp = a_
	if i == len(a) - 1:
		if tmp != 0:
			sum_a.append(tmp)
		if tmp > 0:
			num_z += 1
if sum_a[0] < 0:
	sum_a = sum_a[1:]
if sum_a[-1] < 0:
	sum_a = sum_a[:-1]

sum_ = 0
for a_ in sum_a:
	if a_ > 0:
		sum_ += a_

if m >= num_z:
	print(sum_)
else:
	dp_no = [[0] * len(sum_a) for i in range(m+1)]
	dp_yes = [[0] * len(sum_a) for i in range(m+1)]
	if sum_a[0] > 0:
		for m_ in range(1,m+1):
			dp_yes[m_][0] = sum_a[0]
	for i in range(1,len(sum_a)):
		for j in range(1,m+1):
			dp_no[j][i] = max(dp_yes[j][i-1],dp_no[j][i-1])
			dp_yes[j][i] = max(dp_no[j-1][i-1]+sum_a[i],dp_yes[j][i-1]+sum_a[i])
	print(max(dp_yes[m][len(sum_a)-1],dp_no[m][len(sum_a)-1]))

	

# if m >= num_z:
# 	print(sum_)
# else:
# 	for _ in range(num_z - m):
# 		min_z = 10000
# 		max_f = -10000
# 		for i,a_ in enumerate(sum_a):
# 			if a_ > 0 and a_ < min_z:
# 				min_z = a_
# 				min_z_ind = i
# 			if a_ < 0 and a_ > max_f:
# 				max_f = a_
# 				max_f_ind = i
# 		if min_z > - max_f:
# 			sum_a = sum_a[:max_f_ind - 1] + [sum(sum_a[max_f_ind-1:max_f_ind+2])] + sum_a[max_f_ind + 2:]
# 			sum_ += max_f
# 		else:
# 			sum_ -= min_z
# 			if min_z_ind == 0:
# 				sum_a = sum_a[2:]
# 			elif min_z_ind == len(sum_a) - 1:
# 				sum_a = sum_a[:-2]
# 			else:
# 				sum_a = sum_a[:min_z_ind - 1] + [sum(sum_a[min_z_ind-1:min_z_ind+2])] + sum_a[min_z_ind + 2:]

# 	print(sum_)

		


