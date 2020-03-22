
line = '.X..'
la_num = 0
la_stat = 2
for ind,stat in enumerate(line):
	if stat == 'X':
		if la_stat <2:
			la_stat += 1
		continue
	if la_stat == 2:
		la_num +=1
		la_stat = 0
	else:
		la_stat += 1
print(la_num)
