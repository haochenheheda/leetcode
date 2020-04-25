n = int(raw_input().strip())
lst = map(int,raw_input().strip().split())
stack = {}
num = [0] * n
s = [-1] * n
e = [-1] * n
x = [0] * n
for i,l in enumerate(lst):
	if s[l-1] == -1:
		s[l-1] = i
	else:
		e[l-1] = i
		num[l-1] = e[l-1]- s[l-1] - x[l-1] - 1
		for ind in range(s[l-1]+1,e[l-1]):
			x[lst[ind]-1] += 1
print(sum(num))
