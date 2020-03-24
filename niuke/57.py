lst = raw_input().strip()
stack = []
flag = True
for i in lst:
	if i == '(':
		stack.append('(')
	elif i == '[':
		stack.append('[')
	elif i == ')':
		if len(stack) > 0 and stack[-1] == '(':
			stack.pop(-1)
		else:
			flag = False
			break
	elif i == ']':
		if len(stack) > 0 and stack[-1] == '[':
			stack.pop(-1)
		else:
			flag = False
			break
if flag:
	print('true')
else:
	print('false')
