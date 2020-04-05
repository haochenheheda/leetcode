str_ = raw_input().strip()
stack = 0
max_ = 0 
for s in str_:
	if s == '[':
		stack += 1
		if stack > max_:
			max_ = stack
	elif s == ']':
		stack -= 1

print(max_)