n,d = map(int,raw_input().strip().split())
lst = map(int,raw_input().strip().split())
i,j = 0,2
re = 0
while j < len(lst):
	if lst[j] - lst[i] <= d:
		re += (j-i-1)*(j-i)/2
		j += 1
	else:
		i += 1
print(re % 99997867)
