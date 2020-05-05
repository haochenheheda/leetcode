n = int(raw_input().strip())
for _ in range(n):
	s = raw_input().strip()
	j = 0
	statu = 0
	statu1 = 0
	re = ''
	while j < len(s):
		if j == 0:
			re += s[j]
			j += 1
			statu = 1
			continue

		if statu == 2 and s[j-1] == s[j]:
			j += 1
			continue
		if statu1 == 1 and s[j-1] == s[j]:
			j += 1
			continue

		re += s[j]
		if s[j-1] == s[j]:
			statu += 1
		else:
			if statu == 2 and statu1 == 0:
				statu1 = 1
			else:
				statu = 1
				statu1 = 0
		j+=1
	print(re)
