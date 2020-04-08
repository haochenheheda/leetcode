lst = list(map(int,raw_input().strip().split(',')))
re = [0] * len(lst)
for i in range(len(lst)):
	if i == 0:
		re[i] = 1
	else:
		if lst[i] > lst[i-1]:
			re[i] = re[i-1] + 1
		else:
			re[i] = 1
for i in range(len(lst)-2,-1,-1):
	if lst[i] > lst[i+1]:
		re[i] = max(re[i],re[i+1] + 1)
print(sum(re))