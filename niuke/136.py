s = raw_input().strip()

op_stack = []
re_stack = []
for i,s_ in enumerate(s):
	if i == 0:
		re_stack.append(s_)
	elif i == 1:
		op_stack.append(s_)
	elif s_ == '+' or s_ == '-' or s_ == '*' or s_ == '/':
		op_stack.append(s_)
	else:
		re_stack.append(s_)
		if len(op_stack) > 0 and (op_stack[-1] == '*' or op_stack[-1] == '/'):
			re_stack.append(op_stack.pop(-1))
		if i == len(s) - 1 or s[i+1] == '+' or s[i+1] == '-':
			if len(op_stack) > 0:
				re_stack.append(op_stack.pop(-1))
print(''.join(re_stack)) 