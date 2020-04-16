import sys
q = int(raw_input().strip())
stack = []
for _ in range(q):
	s = raw_input().strip()
	if s[0] == '0':
		op = 0
	elif s[0] == '2':
		op = 2
	else:
		op,num = map(int,s.split())

	if op == 0:
		print(stack[-1][1])
	elif op == 1:
		if stack == []:
			min_ = num
		else:
			min_ = min(stack[-1][1],num)
		stack.append([num,min_])

	else:
		print(stack.pop(-1)[0])
