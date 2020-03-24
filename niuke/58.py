x = raw_input().strip()
out = ''
if x[0] == '-':
	x = x[1:]
	out += '-'
out += x[::-1]
print(out)