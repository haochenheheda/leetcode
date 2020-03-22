lst = raw_input().strip()
c_num = 0
d_num = 0
c_swap_time_sum = 0
d_swap_time_sum = 0

for s in lst:
	if s == 'C':
		c_num += 1
		c_swap_time_sum += d_num
	else:
		d_num += 1
		d_swap_time_sum += c_num
print(min(c_swap_time_sum,d_swap_time_sum))
