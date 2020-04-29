s = raw_input().strip()
num_stack = []
op_stack = []
ops = {'+':0,'-':1,'*':2,'(':3,')':4,'x':5}
pri = [['>','>','<','<','>','>'],
		['>','>','<','<','>','>'],
		['>','>','>','<','>','>'],
		['<','<','<','<','=','>']]
s = s + 'x'
ind = 0
tmp = ''
while ind < len(s):
	s_ = s[ind]
	if ord(s_) >= 48 and ord(s_) <= 57:
		tmp += s_
		# num_stack.append(int(s_))
		ind += 1
	else:
		if tmp != '':
			num_stack.append(int(tmp))
			tmp = ''
		if op_stack == []:
			op_stack.append(s_)
			ind += 1
		else:
			last_op = op_stack[-1]
			this_op = s_
			if pri[ops[last_op]][ops[this_op]] == '<':
				op_stack.append(this_op)
				ind += 1
			elif pri[ops[last_op]][ops[this_op]] == '>':
				num1 = num_stack.pop(-1)
				num2 = num_stack.pop(-1)
				if last_op == '+':
					re = num1 + num2
				elif last_op == '-':
					re = num2 - num1
				elif last_op == '*':
					re = num1 * num2
				num_stack.append(re)
				op_stack.pop(-1)
			elif pri[ops[last_op]][ops[this_op]] == '=':
				op_stack.pop(-1)
				ind += 1

print(num_stack[-1])

