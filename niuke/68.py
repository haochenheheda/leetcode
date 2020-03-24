import sys
lines = open('input.txt','r').readlines()
t = int(lines[0].strip())
for t_ in range(t):
	lst = list(map(int,lines[t_*2 + 2].strip().split()))
	re = []

	for lst_ in lst:
		if not lst_ in re:
			re.append(lst_)
		else:
			re.pop(re.index(lst_))
			re.append(lst_)
	out = ''
	for re_ in re[::-1]:
		out += str(re_) + ' '
	print(out.strip())
