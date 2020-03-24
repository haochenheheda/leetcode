n = int(raw_input().strip())
for _ in range(n):
	h,m,s = map(int,raw_input().strip().split(':'))

	re = ''
	if h > 23:
		re += ('0' + str(h%10))
	else:
		re += (str(h/10) + str(h%10))
	re += ':'
	if m > 59:
		re += ('0' + str(m%10))
	else:
		re += (str(m/10) + str(m%10))
	re += ':'
	if s > 59:
		re += ('0' + str(s%10))
	else:
		re += (str(s/10) + str(s%10))
	print(re)