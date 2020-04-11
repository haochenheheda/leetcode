lst1 = list(map(int,raw_input().strip().split()))
lst2 = list(map(int,raw_input().strip().split()))
ind1 = 0
ind2 = 0
re = []
while ind1 < len(lst1) and ind2 < len(lst2):
	if lst1[ind1] < lst2[ind2]:
		re.append(lst1[ind1])
		ind1 += 1
	else:
 		re.append(lst2[ind2])
		ind2 += 1
re = re + lst1[ind1:] + lst2[ind2:]
print(' '.join(map(str,re)))