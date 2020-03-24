lst1 = list(map(int,raw_input().strip().split()))
lst2 = list(map(int,raw_input().strip().split()))

re = []
ind1 = 0
ind2 = 0
while True:
	if ind1 >= len(lst1) or ind2 >= len(lst2):
		break
	if lst1[ind1] < lst2[ind2]:
		re.append(lst1[ind1])
		ind1 += 1
	else:
		re.append(lst2[ind2])
		ind2 += 1
re += (lst1[ind1:] + lst2[ind2:])
str_ = ''
for r_ in re:
	str_ += (str(r_) + ' ')
print(str_.strip())
