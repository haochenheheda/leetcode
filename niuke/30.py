x = 'aaabccccccdd'
tmp = ''
num = 0
out = ''
for x_ in x:
	if x_ == tmp:
		num += 1
	else:
		if num > 0:
			out += (str(num) + tmp)
		tmp = x_
		num = 1
out += (str(num) + tmp)
print(out)
