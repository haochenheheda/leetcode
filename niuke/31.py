str_ = '-1+2+-3'
last_s = 'o'
num = ''
op = '+'
sum_ = 0
for s in str_:
	if s == '+' or s == '-':
		if last_s == 'o':
			num += s
			last_s = 'n'
		elif last_s == 'n':
			num_int = int(num)
			if op == '+':
				sum_ += num_int
			else:
				sum_ -= num_int
			op = s
			last_s = 'o'
			num = ''
	else:
		last_s = 'n'
		num += s
num_int = int(num)
if op == '+':
	sum_ += num_int
else:
	sum_ -= num_int
print(sum_)
