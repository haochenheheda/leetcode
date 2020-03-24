lst = list(map(int,raw_input().strip()[1:-1].split(',')))
for i in range(3):
	for j in range(0,len(lst)-1-i):
		if lst[j+1] < lst[j]:
			lst[j+1],lst[j] = lst[j],lst[j+1]

print(lst[-3])