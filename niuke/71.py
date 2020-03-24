lst = list(map(int,raw_input().strip().split()))
lst.sort()

count = 0
tmp = None
s_c = 0
for lst_ in lst:
	if lst_ != tmp:
		if tmp != None:
			if s_c%(tmp+1):
			
				count += (s_c + tmp + 1 - s_c%(tmp+1))
			else:
				count += s_c
		s_c = 1
		tmp = lst_
	else:
		s_c += 1
if s_c%(tmp+1):

	count += (s_c + tmp + 1 - s_c%(tmp+1))
else:
	count += s_c

print(count)