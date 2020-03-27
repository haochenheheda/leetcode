lst = list(map(int,raw_input().strip().split()))
j = []
o = []
for l in lst:
	if l%2:
		j.append(l)
	else:
		o.append(l)
print(' '.join(map(str,o+j)))